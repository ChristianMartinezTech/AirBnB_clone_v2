#!/usr/bin/python3
"""script that starts a Flask web application
/hbnb: display “HBNB””"""


from flask import Flask

# Instanciating flask on app
app = Flask(__name__)

# Route home and decorator
@app.route('/', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)
def home():
    return("Hello HBNB!")


# Running flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
