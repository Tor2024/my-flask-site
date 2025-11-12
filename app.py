from flask import Flask, send_from_directory, send_file, request, jsonify
import os
import socket
import json
from datetime import datetime, timedelta
import requests
import logging

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)


# Путь к файлу с данными
DATA_DIR = 'data'
APPOINTMENTS_FILE = os.path.join(DATA_DIR, 'appointments.json')
VISITS_FILE = os.path.join(DATA_DIR, 'visits.json')
TELEGRAM_CONFIG_FILE = os.path.join(DATA_DIR, 'telegram_config.json')

# Создаем директорию для данных, если её нет
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Инициализация файла, если его нет
if not os.path.exists(APPOINTMENTS_FILE):
    with open(APPOINTMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump({"appointments": [], "blocked_slots": {}}, f, ensure_ascii=False)

# Инициализация файла для посещений, если его нет
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, 'w', encoding='utf-8') as f:
        json.dump({"visits": {}}, f, ensure_ascii=False)

# Словарь соответствий value → название услуги
SERVICE_LABELS = {
    'wartung': 'Wartung',
    'diagnose': 'Fahrzeugsdiagnose',
    'motor': 'Motorreparatur',
    'getriebe': 'Getriebereparatur',
    'fahrwerk': 'Reparatur von Fahrwerk und Aufhängung',
    'bremsen': 'Bremsenservice',
    'elektrik': 'Autoelektrik und Elektronik',
    'karosserie': 'Karosseriereparatur und Lackierung',
    'klima': 'Klimaanlagenservice',
    'reifen': 'Reifenmontage und Auswuchten'
}

# Функции для работы с данными
def read_appointments():
    with open(APPOINTMENTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_appointments(data):
    # Создаем резервную копию
    backup_file = os.path.join(DATA_DIR, 'backups', 
                              f'appointments_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    if not os.path.exists(os.path.dirname(backup_file)):
        os.makedirs(os.path.dirname(backup_file))
    
    # Сохраняем резервную копию
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(read_appointments(), f, ensure_ascii=False)
    
    # Сохраняем новые данные
    with open(APPOINTMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def read_visits():
    with open(VISITS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_visits(data):
    with open(VISITS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def read_telegram_config():
    if not os.path.exists(TELEGRAM_CONFIG_FILE):
        # Значения по умолчанию (пустые)
        return {'token': '', 'chat_id': ''}
    with open(TELEGRAM_CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_telegram_config(config):
    try:
        with open(TELEGRAM_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False)
        return True, None
    except Exception as e:
        logger.error(f"Ошибка при сохранении telegram_config: {e}")
        return False, str(e)

import requests

def send_telegram_message(message):
    config = read_telegram_config()
    token = config.get('token')
    chat_id = config.get('chat_id')
    if not token or not chat_id:
        logger.error('Не задан token или chat_id для Telegram')
        return
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logger.info(f"Telegram message sent: {message}")
        else:
            logger.error(f"Ошибка при отправке Telegram сообщения: {response.text}")
    except Exception as e:
        logger.error(f"Ошибка при отправке Telegram сообщения: {e}")

@app.route('/')
def index():
    # Регистрируем посещение главной страницы
    visits_data = read_visits()
    today_str = datetime.now().strftime('%Y-%m-%d')
    visits_data['visits'][today_str] = visits_data['visits'].get(today_str, 0) + 1
    save_visits(visits_data)
    try:
        return send_from_directory('.', 'index.html')
    except Exception as e:
        return f"Ошибка при загрузке страницы: {str(e)}", 500

@app.route('/static/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('static', path)
    except Exception as e:
        return f"Ошибка при загрузке статического файла: {str(e)}", 500

# API endpoints
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    data = read_appointments()
    # Добавляем человекочитаемое название услуги для админки
    for appt in data.get('appointments', []):
        appt['service_label'] = SERVICE_LABELS.get(appt['service'], appt['service'])
    return jsonify(data)

@app.route('/api/admin/blocked_slots', methods=['POST'])
def update_blocked_slots():
    try:
        data = request.json
        date = data.get('date')
        time = data.get('time')
        action = data.get('action') # 'block', 'unblock', 'block_all', 'block_range'

        if not date or not action:
            return jsonify({'error': 'Дата и действие обязательны'}), 400

        appointments_data = read_appointments()
        all_slots = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30"]

        if action == 'block':
            if not time:
                return jsonify({'error': 'Время обязательно для блокировки одного слота'}), 400
            if date not in appointments_data['blocked_slots']:
                appointments_data['blocked_slots'][date] = []
            if time not in appointments_data['blocked_slots'][date]:
                appointments_data['blocked_slots'][date].append(time)
                appointments_data['blocked_slots'][date].sort()
        elif action == 'unblock':
            if not time:
                return jsonify({'error': 'Время обязательно для разблокировки одного слота'}), 400
            if date in appointments_data['blocked_slots'] and time in appointments_data['blocked_slots'][date]:
                appointments_data['blocked_slots'][date].remove(time)
                if not appointments_data['blocked_slots'][date]:
                    del appointments_data['blocked_slots'][date]
        elif action == 'block_all':
            # Блокируем все слоты, которые не заняты пользователем
            booked_slots = [appt['time'] for appt in appointments_data['appointments'] if appt['date'] == date]
            slots_to_block = [slot for slot in all_slots if slot not in booked_slots]
            appointments_data['blocked_slots'][date] = booked_slots + slots_to_block
            appointments_data['blocked_slots'][date].sort()
        elif action == 'block_range':
            start_time = data.get('start_time')
            end_time = data.get('end_time')

            if not start_time or not end_time:
                return jsonify({'error': 'start_time и end_time обязательны для блокировки диапазона'}), 400

            # Получаем индексы временных слотов
            try:
                start_index = all_slots.index(start_time)
                end_index = all_slots.index(end_time)
            except ValueError:
                return jsonify({'error': 'Неверный формат времени'}), 400

            if start_index > end_index:
                return jsonify({'error': 'Время начала должно быть раньше времени окончания'}), 400

            # Получаем слоты в диапазоне
            range_slots = all_slots[start_index:end_index + 1]

            # Проверяем, есть ли уже забронированные слоты в диапазоне
            booked_slots_in_range = [appt['time'] for appt in appointments_data['appointments']
                                   if appt['date'] == date and appt['time'] in range_slots]

            if booked_slots_in_range:
                return jsonify({
                    'error': f'Следующие слоты уже забронированы: {", ".join(booked_slots_in_range)}'
                }), 400

            # Добавляем слоты в заблокированные
            if date not in appointments_data['blocked_slots']:
                appointments_data['blocked_slots'][date] = []

            for slot in range_slots:
                if slot not in appointments_data['blocked_slots'][date]:
                    appointments_data['blocked_slots'][date].append(slot)

            appointments_data['blocked_slots'][date].sort()
        elif action == 'unblock_range':
            start_time = data.get('start_time')
            end_time = data.get('end_time')

            if not start_time or not end_time:
                return jsonify({'error': 'start_time и end_time обязательны для разблокировки диапазона'}), 400

            # Получаем индексы временных слотов
            try:
                start_index = all_slots.index(start_time)
                end_index = all_slots.index(end_time)
            except ValueError:
                return jsonify({'error': 'Неверный формат времени'}), 400

            if start_index > end_index:
                return jsonify({'error': 'Время начала должно быть раньше времени окончания'}), 400

            # Получаем слоты в диапазоне
            range_slots = all_slots[start_index:end_index + 1]

            # Удаляем слоты из заблокированных
            if date in appointments_data['blocked_slots']:
                appointments_data['blocked_slots'][date] = [
                    slot for slot in appointments_data['blocked_slots'][date]
                    if slot not in range_slots
                ]
                # Если больше нет заблокированных слотов на эту дату, удаляем дату
                if not appointments_data['blocked_slots'][date]:
                    del appointments_data['blocked_slots'][date]
        else:
            return jsonify({'error': 'Неизвестное действие. Используйте "block", "unblock", "block_all", "block_range" или "unblock_range"'}), 400

        save_appointments(appointments_data)
        return jsonify({'success': True, 'blocked_slots': appointments_data['blocked_slots']})

    except Exception as e:
        logger.error(f"Ошибка при обновлении заблокированных слотов: {e}")
        return jsonify({'error': 'Внутренняя ошибка сервера: ' + str(e)}), 500

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        
        # Валидация данных
        required_fields = ['date', 'time', 'client', 'service']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Pflichtfeld fehlt: {field}'}), 400
        
        client_fields = ['name', 'email', 'phone']
        for field in client_fields:
            if field not in data['client'] or not str(data['client'][field]).strip():
                return jsonify({'error': f'Pflichtfeld des Kunden fehlt oder ist leer: {field}'}), 400
        
        # Проверка формата даты
        try:
            datetime.strptime(data['date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Ungültiges Datumsformat'}), 400
        
        # Проверка формата времени
        try:
            datetime.strptime(data['time'], '%H:%M')
        except ValueError:
            return jsonify({'error': 'Ungültiges Zeitformat'}), 400
        
        # Проверка email
        if '@' not in data['client']['email']:
            return jsonify({'error': 'Ungültiges E-Mail-Format'}), 400
        
        # Чтение существующих записей
        appointments_data = read_appointments()
        
        # Проверка на дубликаты
        for appointment in appointments_data['appointments']:
            if (appointment['date'] == data['date'] and 
                appointment['time'] == data['time']):
                return jsonify({'error': 'Dieser Termin ist bereits vergeben'}), 400
        
        # Добавление новой записи
        new_appointment = {
            'id': f"{data['date']}_{data['time']}_{datetime.now().timestamp()}",
            'date': data['date'],
            'time': data['time'],
            'client': data['client'],
            'service': data['service'],
            'message': data.get('message', ''),
            'status': 'ожидает',
            'created_at': datetime.now().isoformat()
        }
        
        appointments_data['appointments'].append(new_appointment)
        
        # Обновление заблокированных слотов
        if data['date'] not in appointments_data['blocked_slots']:
            appointments_data['blocked_slots'][data['date']] = []
        appointments_data['blocked_slots'][data['date']].append(data['time'])
        
        # Сохранение данных
        save_appointments(appointments_data)
        
        # Отправка уведомления в Telegram
        service_label = SERVICE_LABELS.get(data['service'], data['service'])
        message = (
            f"Neue Anfrage!\n"
            f"Name: {data['client']['name']}\n"
            f"E-Mail: {data['client']['email']}\n"
            f"Telefon: {data['client']['phone']}\n"
            f"Leistung: {service_label}\n"
            f"Datum: {data['date']}\n"
            f"Uhrzeit: {data['time']}\n"
            f"Nachricht: {data.get('message', '').strip() or '—'}"
        )
        send_telegram_message(message)
        
        return jsonify({
            'success': True,
            'message': 'Termin erfolgreich erstellt',
            'appointment_id': new_appointment['id']
        })
        
    except Exception as e:
        return jsonify({'error': 'Interner Serverfehler: ' + str(e)}), 500

@app.route('/admin')
def admin():
    try:
        return send_from_directory('.', 'admin.html')
    except Exception as e:
        return f"Ошибка при загрузке админ-панели: {str(e)}", 500

@app.route('/access_denied')
def access_denied():
    # Отдаем статическую страницу "Доступ запрещен"
    return send_from_directory(app.root_path, 'access_denied.html')

@app.route('/api/admin/appointments', methods=['GET'])
def admin_get_appointments():
    try:
        data = read_appointments()
        print(f"Загружены записи: {data}")
        return jsonify(data)
    except Exception as e:
        print(f"Ошибка при загрузке записей: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/appointments/<appointment_id>/status', methods=['PUT'])
def update_appointment_status(appointment_id):
    try:
        data = request.get_json()
        new_status = data.get('status')
        
        if not new_status:
            return jsonify({'error': 'Статус не указан'}), 400
            
        appointments = read_appointments()
        found = False
        
        for appointment in appointments['appointments']:
            if appointment['id'] == appointment_id:
                appointment['status'] = new_status
                found = True
                break
                
        if not found:
            return jsonify({'error': 'Запись не найдена'}), 404
            
        save_appointments(appointments)
        return jsonify({'message': 'Статус успешно обновлен', 'status': new_status})
        
    except Exception as e:
        print(f"Ошибка при обновлении статуса: {str(e)}")
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/appointments/<appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        appointments = read_appointments()
        found = False
        
        # Ищем запись для удаления
        for i, appointment in enumerate(appointments['appointments']):
            if appointment['id'] == appointment_id:
                # Удаляем время из заблокированных слотов
                if appointment['date'] in appointments['blocked_slots']:
                    appointments['blocked_slots'][appointment['date']] = [
                        time for time in appointments['blocked_slots'][appointment['date']]
                        if time != appointment['time']
                    ]
                    # Если больше нет заблокированных слотов на эту дату, удаляем дату
                    if not appointments['blocked_slots'][appointment['date']]:
                        del appointments['blocked_slots'][appointment['date']]
                
                # Удаляем запись
                del appointments['appointments'][i]
                found = True
                break
                
        if not found:
            return jsonify({'error': 'Запись не найдена'}), 404
            
        save_appointments(appointments)
        return jsonify({'message': 'Запись успешно удалена'})
        
    except Exception as e:
        print(f"Ошибка при удалении записи: {str(e)}")
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/analytics', methods=['GET'])
def analytics():
    # Получаем период в днях (30 или 365)
    period = request.args.get('period', default=30, type=int)
    # Подсчет заказов
    data = read_appointments()
    appointments = data.get('appointments', [])
    start_date = datetime.now().date() - timedelta(days=period)
    count_appt = 0
    for appt in appointments:
        try:
            appt_date = datetime.strptime(appt['date'], '%Y-%m-%d').date()
            if appt_date >= start_date:
                count_appt += 1
        except:
            continue
    # Подсчет посещений
    visits_raw = read_visits().get('visits', {})
    count_visits = 0
    for date_str, cnt in visits_raw.items():
        try:
            d = datetime.strptime(date_str, '%Y-%m-%d').date()
            if d >= start_date:
                count_visits += cnt
        except:
            continue
    return jsonify({'appointments': count_appt, 'visits': count_visits})

# API для получения и обновления настроек Telegram
@app.route('/api/telegram_config', methods=['GET'])
def get_telegram_config():
    config = read_telegram_config()
    return jsonify(config)

@app.route('/api/telegram_config', methods=['POST'])
def update_telegram_config():
    data = request.json
    if not data or 'token' not in data or 'chat_id' not in data:
        return jsonify({'error': 'Необходимы token и chat_id'}), 400
    success, error = save_telegram_config({'token': data['token'], 'chat_id': data['chat_id']})
    if not success:
        return jsonify({'error': f'Ошибка сохранения: {error}'}), 500
    return jsonify({'success': True})

def find_free_port(start_port=8080, max_port=9000):
    for port in range(start_port, max_port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.close()
            return port
        except OSError:
            continue
    raise RuntimeError("Не удалось найти свободный порт")

if __name__ == '__main__':
    try:
        port = find_free_port()
        print(f"Запуск сервера на порту {port}...")
        print(f"Сайт будет доступен по адресу: http://localhost:{port}")
        print("Для остановки сервера нажмите Ctrl+C")
        app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
    except Exception as e:
        print(f"Ошибка при запуске сервера: {str(e)}")
