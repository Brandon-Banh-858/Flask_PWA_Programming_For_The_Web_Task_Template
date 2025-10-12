from flask import Flask, flash, redirect, url_for
import sqlite3, time
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)
DB_PATH = "Flask_PWA_Programming_For_The_Web_Task_Template/Database/data_source.db"
app.secret_key = "ThisMessageIsReallySecretAndThereIsAbsolutelyNoWayYouWillGuessThisIfYouDoThenYouAreLikeSomeFifteenthDimensionalBeingAndAlsoIfYouAreReadingThisThenDidYouKnowThatWaitActuallyNevermindForgetWhatYouSawAndAnywaysTheEnd"

TrueUsername = ""

def connection():
   conn = sqlite3.connect(DB_PATH)
   conn.row_factory = sqlite3.Row
   return conn

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
   global TrueUsername
   if TrueUsername != "":
      return render_template('/partials/index.html', UserNamed=TrueUsername)
   return render_template('/index.html')

@app.route('/ask_and_answer.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def ask_and_answer():
   global TrueUsername
   if TrueUsername != "":
      return render_template('/partials/ask_and_answer.html', UserNamed=TrueUsername)
   return render_template('/partials/ask_and_answer.html')

@app.route('/homepage.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def homepage():
   global TrueUsername
   print(TrueUsername)
   if TrueUsername != "":
      return render_template('/partials/homepage.html', UserNamed=TrueUsername)
   return render_template('/partials/homepage.html')

@app.route('/messages.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def messages():
   global TrueUsername
   if TrueUsername != "":
      return render_template('/partials/messages.html', UserNamed=TrueUsername)
   return render_template('/partials/messages.html')

@app.route('/login.html', methods=['GET','POST','POST2'])
@app.route('/', methods=['POST', 'GET', 'POST2'])
def login():
   global TrueUsername
   if TrueUsername != "":
      return render_template('/partials/login.html', UserNamed=TrueUsername)
   
   if request.method == "POST":
      username = request.form["username"].strip()
      passcode = request.form["password"].strip()
      type = request.form["Type"].strip()

      conn = connection()
      cursor = conn.cursor()
      cursor = conn.cursor()
      users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (username,))

      if type == "Login":
         row = users.fetchall()
         cursor.close()
         if (username != "") and (passcode != ""):
            if len(row) > 0:
               if row[0]["Passcode"] == passcode:
                  TrueUsername = username
                  conn.commit()
                  conn.close()
                  return render_template('/partials/login.html', VarSend="Change")
               else:
                  return render_template('/partials/login.html', ErrorMessage="Sorry, this is the incorrect password.", VarSend="Valid")
            else:
               return render_template('/partials/login.html', ErrorMessage="Sorry, the user '" + str(username) + "' does not exist.", VarSend="Valid")
         else:
            return render_template('/partials/login.html', ErrorMessage="Please Input a username and password.", VarSend="Valid")


      else:
         row = users.fetchall()

         cursor.close()

         if (username != "") and (passcode != ""):
            if len(row) <= 0:
               if ("!" not in username) and ("@" not in username) and ("#" not in username) and ("$" not in username) and ("$" not in username) and ("%" not in username) and ("^" not in username) and ("&" not in username) and ("*" not in username) and ("(" not in username) and (")" not in username) and ("'" not in username) and ('"' not in username):
                  if any(character.isupper for character in passcode):
                     if any(character.isdigit for character in passcode):
                        if any(character in "!@#$%^&*()" for character in passcode):
                           if not any(character.isspace() for character in username):
                              conn.execute("INSERT INTO UserTable (Username, Passcode) VALUES (?,?)", (username,passcode))
                              TrueUsername = username
                              conn.commit()
                              conn.close()
                              return render_template('/partials/login.html', VarSend="Change")
                           else:
                              return render_template('/partials/login.html', ErrorMessage="Sorry, please ensure that your username contains no spaces.", VarSend="Valid")
                        else:
                           return render_template('/partials/login.html', ErrorMessage="Sorry, please ensure that your password contains atleast 1 special character.", VarSend="Valid")
                     else:
                        return render_template('/partials/login.html', ErrorMessage="Sorry, please ensure that your password contains atleast 1 number.", VarSend="Valid")
                  else:
                     return render_template('/partials/login.html', ErrorMessage="Sorry, please ensure that your password contains atleast 1 capital letter.", VarSend="Valid")
               else:
                  return render_template('/partials/login.html', ErrorMessage="Sorry, your username contains invalid characters. Please refuse to use any of the following: !@#$%^&*().", VarSend="Valid")
            else:
               return render_template('/partials/login.html', ErrorMessage="Sorry, the username '" + str(username) + "' has been taken. Please choose another username.", VarSend="Valid")
         else:
            return render_template('/partials/login.html', ErrorMessage="Please Input a username and password.", VarSend="Valid")

   return render_template('/partials/login.html', VarSend="Invalid")

@app.route('/signin.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def signin():
   global TrueUsername
   if TrueUsername != "":
      return render_template('/partials/signin.html', UserNamed=TrueUsername)
   return render_template('/partials/signin.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)

