// Обработка форм и функциональность сайта
document.addEventListener('DOMContentLoaded', function() {
    let currentDate = new Date();
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();
    let selectedDate = null;
    let selectedTime = null;

    // Инициализация элементов календаря
    const monthYearDisplay = document.querySelector('.flex.justify-between.items-center.mb-4 h4');
    const calendarDays = document.querySelectorAll('.calendar-day');
    const timeSlotsContainer = document.querySelector('.time-slots-container');
    const selectedDateInput = document.getElementById('selected-date');
    const selectedTimeInput = document.getElementById('selected-time');
    
    // Переводим сообщения для формы записи
    const MSG_REQUIRED_FIELDS = 'Bitte füllen Sie alle Pflichtfelder aus';
    const MSG_SELECT_DATE_TIME = 'Bitte wählen Sie Datum und Uhrzeit';
    const MSG_SUCCESS = 'Ihre Anfrage wurde erfolgreich gesendet! Wir werden Sie in Kürze kontaktieren, um den Termin zu bestätigen.';
    const MSG_ERROR = 'Fehler beim Senden des Formulars: ';
    
    // Функция для обновления отображения месяца и года
    function updateMonthYearDisplay() {
        const monthNames = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 
                          'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
        monthYearDisplay.textContent = `${monthNames[currentMonth]} ${currentYear}`;
    }
    
    // Функция для обновления календаря
    async function updateCalendar() {
        const firstDay = new Date(currentYear, currentMonth, 1);
        const lastDay = new Date(currentYear, currentMonth + 1, 0);
        const daysInMonth = lastDay.getDate();
        const startingDay = firstDay.getDay() || 7;
        
        updateMonthYearDisplay();
        
        calendarDays.forEach(day => {
            day.textContent = '';
            day.className = 'calendar-day';
        });
        
        let dayCounter = 1;
        for (let i = 0; i < 42; i++) {
            if (i >= startingDay - 1 && dayCounter <= daysInMonth) {
                const date = new Date(currentYear, currentMonth, dayCounter);
                const dateString = formatDateForAPI(date);
                const dayElement = calendarDays[i];
                dayElement.textContent = dayCounter;
                
                if (isPastDate(date) && !isToday(date)) {
                    dayElement.classList.add('text-gray-400');
                } else if (isWeekend(date) || isGermanHoliday(date)) {
                    dayElement.classList.add('booked');
                } else {
                    // Проверяем, есть ли занятые слоты на эту дату
                    getBlockedSlots(dateString).then(blockedSlots => {
                        if (blockedSlots.length > 0) {
                            dayElement.classList.add('partially');
                        } else {
                            dayElement.classList.add('available');
                        }
                    });
                }
                
                dayCounter++;
            }
        }
    }
    
    // Функция для проверки, является ли день выходным
    function isWeekend(date) {
        const day = date.getDay();
        return day === 0 || day === 6; // 0 - воскресенье, 6 - суббота
    }
    
    // Функция для проверки, является ли день рабочим
    function isWorkingDay(date) {
        return !isWeekend(date);
    }
    
    // Функция для проверки, является ли дата прошедшей
    function isPastDate(date) {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        return date < today;
    }
    
    // Функция для проверки, является ли время прошедшим
    function isPastTime(time, date) {
        const now = new Date();
        const [hours, minutes] = time.split(':').map(Number);
        const slotTime = new Date(date);
        slotTime.setHours(hours, minutes, 0, 0);
        return slotTime < now;
    }
    
    // Функция для получения доступных временных слотов
    function getAvailableTimeSlots(date) {
        const slots = [];
        const startMorning = 9; // 09:00
        const endMorning = 13; // 13:00
        const startAfternoon = 14; // 14:00
        const endAfternoon = 17; // 17:00
        
        // Добавляем утренние слоты
        for (let hour = startMorning; hour < endMorning; hour++) {
            const time = `${hour.toString().padStart(2, '0')}:00`;
            slots.push({
                time: time,
                available: !isPastTime(time, date)
            });
            const time30 = `${hour.toString().padStart(2, '0')}:30`;
            slots.push({
                time: time30,
                available: !isPastTime(time30, date)
            });
        }
        
        // Добавляем дневные слоты
        for (let hour = startAfternoon; hour < endAfternoon; hour++) {
            const time = `${hour.toString().padStart(2, '0')}:00`;
            slots.push({
                time: time,
                available: !isPastTime(time, date)
            });
            const time30 = `${hour.toString().padStart(2, '0')}:30`;
            slots.push({
                time: time30,
                available: !isPastTime(time30, date)
            });
        }
        
        return slots;
    }
    
    // Функция для отправки данных записи на сервер
    async function saveAppointment(appointmentData) {
        try {
            const response = await fetch('/api/appointments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(appointmentData)
            });

            if (!response.ok) {
                throw new Error('Ошибка при сохранении записи');
            }

            const result = await response.json();
            return result;
        } catch (error) {
            console.error('Ошибка:', error);
            throw error;
        }
    }

    // Функция для получения занятых слотов
    async function getBlockedSlots(date) {
        try {
            const response = await fetch('/api/appointments');
            if (!response.ok) {
                throw new Error('Ошибка при получении данных');
            }
            const data = await response.json();
            console.log('Получены данные с сервера:', data);
            
            // Проверяем наличие занятых слотов для указанной даты
            const blockedSlots = data.blocked_slots[date] || [];
            console.log('Занятые слоты для даты', date, ':', blockedSlots);
            
            return blockedSlots;
        } catch (error) {
            console.error('Ошибка при получении занятых слотов:', error);
            return [];
        }
    }

    // Обновляем функцию updateTimeSlots
    async function updateTimeSlots(dateString) {
        const slots = getAvailableTimeSlots(new Date(dateString));
        timeSlotsContainer.innerHTML = '';
        
        // Получаем занятые слоты
        const blockedSlots = await getBlockedSlots(dateString);
        console.log('Занятые слоты для даты', dateString, ':', blockedSlots);
        
        slots.forEach(slot => {
            const button = document.createElement('button');
            button.type = 'button';
            
            // Определяем классы в зависимости от статуса слота
            const isBlocked = blockedSlots.includes(slot.time);
            const isAvailable = slot.available && !isBlocked;
            
            button.className = `px-4 py-2 border rounded-md text-sm font-medium transition-colors ${
                isBlocked
                    ? 'border-red-200 text-red-500 bg-red-50 cursor-not-allowed' 
                    : isAvailable
                        ? 'border-primary text-primary hover:bg-primary/5' 
                        : 'border-gray-200 text-gray-400 cursor-not-allowed bg-gray-100'
            }`;
            
            button.textContent = slot.time;
            button.disabled = !isAvailable;
            
            if (isAvailable) {
                button.onclick = async function(e) {
                    e.preventDefault();
                    // Снимаем выделение со всех слотов
                    timeSlotsContainer.querySelectorAll('button').forEach(btn => {
                        btn.classList.remove('bg-primary', 'text-white');
                    });
                    // Выделяем выбранный слот
                    this.classList.add('bg-primary', 'text-white');
                    selectedTimeInput.value = this.textContent;
                };
            } else {
                // Добавляем иконку для занятых слотов
                const icon = document.createElement('i');
                icon.className = 'ri-lock-line ri-sm ml-1';
                button.appendChild(icon);
            }
            
            timeSlotsContainer.appendChild(button);
        });
    }
    
    // Функция для обновления отображения выбранной даты и времени
    function updateSelectedDateTimeDisplay() {
        const date = new Date(selectedDateInput.value);
        const time = selectedTimeInput.value;
        
        if (date && time) {
            // Устанавливаем правильный часовой пояс
            const localDate = new Date(date.getTime() + date.getTimezoneOffset() * 60000);
            const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            const formattedDate = localDate.toLocaleDateString('ru-RU', options);
            
            // Создаем контейнер для отображения, если его нет
            let displayContainer = document.getElementById('selected-date-time-display');
            if (!displayContainer) {
                displayContainer = document.createElement('div');
                displayContainer.id = 'selected-date-time-display';
                displayContainer.className = 'mt-4 p-4 bg-gray-50 rounded';
                appointmentForm.insertBefore(displayContainer, appointmentForm.firstChild);
            }
            
            displayContainer.textContent = `Выбрано: ${formattedDate}, ${time}`;
        }
    }
    
    // Функция для проверки, является ли дата сегодняшней
    function isToday(date) {
        const today = new Date();
        return date.getDate() === today.getDate() &&
               date.getMonth() === today.getMonth() &&
               date.getFullYear() === today.getFullYear();
    }
    
    // Функция для проверки немецких праздников
    function isGermanHoliday(date) {
        const year = date.getFullYear();
        const month = date.getMonth() + 1; // Добавляем 1, чтобы месяцы начинались с 1
        const day = date.getDate();
        
        // Список немецких праздников (фиксированные даты)
        const fixedHolidays = [
            { month: 1, day: 1 },   // Новый год (1 января)
            { month: 4, day: 25 },  // 25 апреля
            { month: 5, day: 1 },   // День труда (1 мая)
            { month: 10, day: 3 },  // День единства Германии (3 октября)
            { month: 12, day: 25 }, // Рождество (25 декабря)
            { month: 12, day: 26 }  // День подарков (26 декабря)
        ];
        
        // Проверка фиксированных праздников
        for (const holiday of fixedHolidays) {
            if (month === holiday.month && day === holiday.day) {
                return true;
            }
        }
        
        // Расчет подвижных праздников
        const easter = calculateEaster(year);
        const holidays = [
            { name: 'Karfreitag', offset: -2 },    // Страстная пятница
            { name: 'Ostermontag', offset: 1 },    // Пасхальный понедельник
            { name: 'Christi Himmelfahrt', offset: 39 }, // Вознесение
            { name: 'Pfingstmontag', offset: 50 }  // Пятидесятница
        ];
        
        for (const holiday of holidays) {
            const holidayDate = new Date(easter);
            holidayDate.setDate(easter.getDate() + holiday.offset);
            if (month === holidayDate.getMonth() && day === holidayDate.getDate()) {
                return true;
            }
        }
        
        return false;
    }
    
    // Функция для расчета даты Пасхи
    function calculateEaster(year) {
        const a = year % 19;
        const b = Math.floor(year / 100);
        const c = year % 100;
        const d = Math.floor(b / 4);
        const e = b % 4;
        const f = Math.floor((b + 8) / 25);
        const g = Math.floor((b - f + 1) / 3);
        const h = (19 * a + b - d - g + 15) % 30;
        const i = Math.floor(c / 4);
        const k = c % 4;
        const l = (32 + 2 * e + 2 * i - h - k) % 7;
        const m = Math.floor((a + 11 * h + 22 * l) / 451);
        const month = Math.floor((h + l - 7 * m + 114) / 31);
        const day = ((h + l - 7 * m + 114) % 31) + 1;
        
        return new Date(year, month - 1, day);
    }
    
    // Инициализация кнопок навигации
    const calendarSection = document.querySelector('.bg-white.p-6.rounded.shadow-sm.mb-8');
    if (calendarSection) {
        const prevButton = calendarSection.querySelector('button:has(.ri-arrow-left-s-line)');
        const nextButton = calendarSection.querySelector('button:has(.ri-arrow-right-s-line)');
        
        // Добавляем одинаковые стили для обеих кнопок
        [prevButton, nextButton].forEach(button => {
            if (button) {
                button.className = 'p-2 hover:bg-gray-100 rounded-full transition-colors';
            }
        });
        
        // Кнопка "назад"
        if (prevButton) {
            prevButton.addEventListener('click', function(e) {
                e.preventDefault();
                currentMonth--;
                if (currentMonth < 0) {
                    currentMonth = 11;
                    currentYear--;
                }
                updateCalendar();
            });
        }
        
        // Кнопка "вперед"
        if (nextButton) {
            nextButton.addEventListener('click', function(e) {
                e.preventDefault();
                currentMonth++;
                if (currentMonth > 11) {
                    currentMonth = 0;
                    currentYear++;
                }
                updateCalendar();
            });
        }
    }
    
    // Обработка выбора даты
    calendarDays.forEach(day => {
        day.addEventListener('click', function() {
            if (this.classList.contains('text-gray-400') || this.classList.contains('booked')) return;
            
            // Снимаем выделение со всех дней
            calendarDays.forEach(d => d.classList.remove('selected'));
            
            // Выделяем выбранный день
            this.classList.add('selected');
            
            // Получаем выбранную дату
            const selectedDay = parseInt(this.textContent);
            const selectedDate = new Date(currentYear, currentMonth, selectedDay);
            
            // Форматируем дату для сохранения
            const formattedDate = formatDateForAPI(selectedDate);
            selectedDateInput.value = formattedDate;
            
            // Обновляем доступные временные слоты
            updateTimeSlots(formattedDate);
        });
    });
    
    // Инициализация календаря
    updateCalendar();
    updateSelectedDateTimeDisplay();

    // Обработка отправки формы
    const appointmentForm = document.getElementById('appointment-form');
    if (appointmentForm) {
        appointmentForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Проверка обязательных полей
            const requiredFields = appointmentForm.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('border-red-500');
                } else {
                    field.classList.remove('border-red-500');
                }
            });
            
            if (!isValid) {
                alert(MSG_REQUIRED_FIELDS);
                return;
            }
            
            // Проверка выбора даты и времени
            if (!selectedDateInput.value || !selectedTimeInput.value) {
                alert(MSG_SELECT_DATE_TIME);
                return;
            }
            
            // Сбор данных формы
            const formData = {
                date: selectedDateInput.value,
                time: selectedTimeInput.value,
                client: {
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    phone: document.getElementById('phone').value
                },
                service: document.getElementById('service').value,
                message: document.getElementById('message').value
            };
            
            try {
                // Отправка данных на сервер
                const response = await fetch('/api/appointments', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
                
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || 'Ошибка при отправке формы');
                }
                
                const result = await response.json();
                
                // Показ сообщения об успехе
                const successMessage = document.createElement('div');
                successMessage.className = 'mt-4 p-4 bg-green-100 text-green-700 rounded';
                successMessage.textContent = MSG_SUCCESS;
                
                appointmentForm.appendChild(successMessage);
                
                // Очистка формы
                appointmentForm.reset();
                selectedDateInput.value = '';
                selectedTimeInput.value = '';
                
                // Удаление сообщения через 5 секунд
                setTimeout(() => {
                    successMessage.remove();
                }, 5000);
            } catch (error) {
                console.error('Ошибка:', error);
                alert(MSG_ERROR + error.message);
            }
        });
    }

    // Добавляем функцию форматирования даты для API
    function formatDateForAPI(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    // Вставка дней недели на немецком
    // Найти контейнер с днями недели и заменить их на немецкие
    const dayNames = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'];
    const weekRow = document.querySelectorAll('.grid.grid-cols-7.gap-1.text-center.mb-2 > div');
    if (weekRow && weekRow.length === 7) {
        dayNames.forEach((name, idx) => {
            weekRow[idx].textContent = name;
        });
    }
});
