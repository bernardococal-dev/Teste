from flask import Flask, render_template
import os

app = Flask(__name__)

# Configurar pasta de imagens estática
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
