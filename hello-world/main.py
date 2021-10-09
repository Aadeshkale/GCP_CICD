from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Simple Hello web app for demo of GCP!'

@app.route('/display')
def dis():
    return 'Display info!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
