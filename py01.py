from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    file = open('D:/study/python/01/hello.py','r')
    content = file.read();
    file.close();
    return 'Hello World!  ... ' + content


if __name__ == '__main__':
    app.run()
