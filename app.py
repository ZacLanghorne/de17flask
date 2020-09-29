from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to my AWESOME webpage!'


if __name__ == '__main__':
    app.run()
