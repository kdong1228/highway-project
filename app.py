from flask import Flask
from flask import Flask, render_template     # render_template 이라는 부품을 추가로 가져옵니다.

app = Flask(__name__)

@app.route('/')
def index():  # <-- 'def'로 시작하는 함수
    
    # index.html 파일을 찾아서 사용자에게 보여줍니다.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)