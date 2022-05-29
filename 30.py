from flask import Flask, request

app = Flask("something")


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        a = 1 / 0
        return '<h1><div id="moshe"><li>mazda</li> <li>citroen</li> <li>chevrolet</li><li>ferari</li><</div></h1>'
    elif request.method == 'POST':
        return "saved new car"


@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)