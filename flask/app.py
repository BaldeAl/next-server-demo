from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur mon site!'

@app.route('/bonjour/<nom>')
def bonjour(nom):
    return f'Bonjour {nom}!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    app.run(host='0.0.0.0', port=port)