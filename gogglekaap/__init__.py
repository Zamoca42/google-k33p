from flask import Flask
from flask import render_template

def create_app():
    print('run: create_app()')
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app