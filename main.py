from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])

def index():
   data = dbHandler.listExtension()
   return render_template('/index.html', content=data)

@app.route('/ask_and_answer.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def ask_and_answer():
   data = dbHandler.listExtension()
   return render_template('/partials/ask_and_answer.html', content=data)

@app.route('/homepage.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])

def homepage():
   data = dbHandler.listExtension()
   return render_template('/partials/homepage.html', content=data)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)

