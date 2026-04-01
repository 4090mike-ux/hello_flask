from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 여기에 내 데이터를 만든다!
    my_profile = {
        "name": "김현진",
        "age": 19,
        "school": "종로산업정보학교",
        "hobby": "게임",
        "phone": "010-0000-0000",
        "dream": "개발자"
    }

    return render_template('index.html', data=my_profile)

if __name__ == '__main__':
    app.run(debug=True)