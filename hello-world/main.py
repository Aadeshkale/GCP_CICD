import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Simple Hello web app for demo of GCP!'

@app.route('/display')
def dis():
    return 'Display info!'

@app.route('/config')
def config():
    # for cloud run when secrete mounted as volume
    # with open('/etc/secrets/dbconfig.json','r') as f:
    #         data = f.read()
    # return data

    # for app engine when secrete as env variable
    data = os.environ.get("SEC")
    info = os.environ['SEC']
    print("before")
    print(info)
    print(data)
    print("Afer")
    return str(info)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
