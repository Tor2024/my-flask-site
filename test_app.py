from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Привет! Сайт работает!'

if __name__ == '__main__':
    print("Запуск тестового сервера на порту 5000...")
    print("Откройте http://127.0.0.1:5000 в браузере")
    app.run(host='0.0.0.0', port=5000, debug=True)
