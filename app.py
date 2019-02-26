from flask import Flask, url_for, request, render_template
from public.api.update import api

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/')
def index():
    return render_template('from.html')


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


@app.route('/request_type', methods=['GET', 'POST'])
def request_type():
    if request.method == 'POST':
        return 'post'
    else:
        return 'get'


# 测试URL请求
with app.test_request_context():
    a = url_for('login', b='djq')
    print(a, 'over')
    # 静态文件
    # b = url_for('static', filename='style.css')
    # print(b)


if __name__ == '__main__':
    app.run()
