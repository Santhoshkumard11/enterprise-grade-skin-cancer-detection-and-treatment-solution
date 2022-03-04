# Flask utils
from flask import Flask, render_template
# Define a flask app
app = Flask(__name__)


# home page of our flask web app
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
