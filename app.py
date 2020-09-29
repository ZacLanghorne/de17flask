from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to my AWESOME webpage!'

@app.route('/consultant/<string:cohort>/<string:consultant>')
def consultant(cohort: str,consultant: str):
    return f'This is the consultant portal for {consultant} in cohort: {cohort}.'

@app.route('/client')
def client():
    return 'This is the client portal.'


if __name__ == '__main__':
    app.run()
