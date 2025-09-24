from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():  # <-- 'def'로 시작하는 함수
    return "Hello, my highway project is running!"  # <-- 함수 안에 'return' 구문

if __name__ == '__main__':
    app.run(debug=True)