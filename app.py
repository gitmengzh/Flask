from flask import Flask, request
import  random, time, base64
app = Flask(__name__)

users = {
    "xiaoming":"123456"
}
@ app.route('/index/<username>', methods = ['POST'])  # 指定路由，访问方法
def hello_word(username):
    return "hello %s" % username

def gen_token(uid):
    token = base64.b64encode((':'.join([str(uid), str(random.random()), str(time.time() + 7200)])).encode())
    # token = base64.b64encode([str(uid)+str(random.random())+str(time.time() + 7200)])
    # token = base64.b64encode(uid.encode('utf-8'))
    # users[uid].append(token)
    return token

def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(str.encode(':'))[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0
    return _token


@app.route('/login', methods = ['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).decode().split(':')
    if users.get(uid) == pw:
        return gen_token(uid)
    else:
        return 'error'


@app.route('/test1', methods=['POST', 'GET'])
def test():

    token = request.args.get('token')
    if verify_token(token) == 1:
        return "data"
    else:
        return 'error'


@app.route('/test2', methods=['POST', 'GET'])
def test2():
    aaa = request.headers
    response = ""
    for k, v in aaa.items():
        response += "%s : %s<br/>" % (k, v)
    return response


if __name__ == "__main__":
    app.run(debug=True)