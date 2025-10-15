from flask import Flask, flash, redirect, url_for
import sqlite3, time
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)
DB_PATH = "Flask_PWA_Programming_For_The_Web_Task_Template/Database/data_source.db"
app.secret_key = "ThisMessageIsReallySecretAndThereIsAbsolutelyNoWayYouWillGuessThisIfYouDoThenYouAreLikeSomeFifteenthDimensionalBeingAndAlsoIfYouAreReadingThisThenDidYouKnowThatWaitActuallyNevermindForgetWhatYouSawAndAnywaysTheEnd"

TrueUsername = ""
ProgramLang = ""
Filter = ""

def connection():
   conn = sqlite3.connect(DB_PATH)
   conn.row_factory = sqlite3.Row
   return conn

@app.route('/index.html', methods=['GET','POST'])
@app.route('/', methods=['POST', 'GET'])
def index():
   global TrueUsername,ProgramLang
   if request.method == "POST":
      if request.form["typing"].strip() == "LoggingOut":
         TrueUsername = ""
         ProgramLang = ""

      elif request.form["typing"].strip() == "LoginChange":
         Old_Pas = request.form["oldpassword"].strip()
         New_Pas = request.form["newpassword"].strip()
         conn = connection()
         cursor = conn.cursor()
         users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (TrueUsername,))
         row = users.fetchall()
         if row[0]["Passcode"] == Old_Pas:
            if any(character.isupper for character in New_Pas):
               if any(character.isdigit for character in New_Pas):
                  if any(character in "!@#$%^&*()" for character in New_Pas):
                     cursor.execute("UPDATE UserTable SET Passcode = ? WHERE Username = ?", (New_Pas,TrueUsername))
                     conn.commit()
                     cursor.close()
                     return render_template('/index.html', Success="", UserNamed=TrueUsername)
                  else:
                     return render_template('/index.html', Success="The new password did not contain special characters.", UserNamed=TrueUsername)
               else:
                  return render_template('/index.html', Success="The new password did not contain any numbers.", UserNamed=TrueUsername)
            else:
               return render_template('/index.html', Success="The new password did not contain any capital letters.", UserNamed=TrueUsername)
         else:
            return render_template('/index.html', Success="The password inputted was not correct.", UserNamed=TrueUsername)
   
   if TrueUsername != "":
      return render_template('/index.html', UserNamed=TrueUsername)
   return render_template('/index.html')

@app.route('/ask_and_answer.html', methods=['GET','POST'])
@app.route('/', methods=['POST', 'GET'])
def ask_and_answer():
   global TrueUsername,ProgramLang
   if request.method == "POST":
      if request.form["typing"].strip() == "ChangeProgramLang":
         if (TrueUsername != ""):
            conn = connection()
            cursor = conn.cursor()
            ProgramLang = request.form["ChangeLan"].strip()
            cursor.execute("UPDATE UserTable SET Programming_language = ? WHERE Username = ?", (ProgramLang,TrueUsername))
            conn.commit()
            cursor.close()
            return render_template('/partials/ask_and_answer.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang,Variable=request.form["ChangePage"].strip())
         else:
            ProgramLang = request.form["ChangeLan"].strip()
            return render_template('/partials/ask_and_answer.html', ProgramLangu=ProgramLang,Variable=request.form["ChangePage"].strip())

      elif request.form["typing"].strip() == "LoggingOut":
         TrueUsername = ""
         ProgramLang = ""

      elif request.form["typing"].strip() == "LoginChange":
         Old_Pas = request.form["oldpassword"].strip()
         New_Pas = request.form["newpassword"].strip()
         conn = connection()
         cursor = conn.cursor()
         users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (TrueUsername,))
         row = users.fetchall()
         if row[0]["Passcode"] == Old_Pas:
            if any(character.isupper for character in New_Pas):
               if any(character.isdigit for character in New_Pas):
                  if any(character in "!@#$%^&*()" for character in New_Pas):
                     cursor.execute("UPDATE UserTable SET Passcode = ? WHERE Username = ?", (New_Pas,TrueUsername))
                     conn.commit()
                     cursor.close()
                     return render_template('/partials/ask_and_answer.html', Success="", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
                  else:
                     return render_template('/partials/ask_and_answer.html', Success="The new password did not contain special characters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
               else:
                  return render_template('/partials/ask_and_answer.html', Success="The new password did not contain any numbers.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
            else:
               return render_template('/partials/ask_and_answer.html', Success="The new password did not contain any capital letters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
         else:
            return render_template('/partials/ask_and_answer.html', Success="The password inputted was not correct.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
         
   if TrueUsername != "":
      return render_template('/partials/ask_and_answer.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang)
   return render_template('/partials/ask_and_answer.html', ProgramLangu=ProgramLang)

@app.route('/homepage.html', methods=['GET','POST'])
@app.route('/', methods=['POST', 'GET'])
def homepage():
   global TrueUsername,ProgramLang
   if request.method == "POST":
      if request.form["typing"].strip() == "LoggingOut":
         TrueUsername = ""
         ProgramLang = ""

      elif request.form["typing"].strip() == "LoginChange":
         Old_Pas = request.form["oldpassword"].strip()
         New_Pas = request.form["newpassword"].strip()
         conn = connection()
         cursor = conn.cursor()
         users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (TrueUsername,))
         row = users.fetchall()
         if row[0]["Passcode"] == Old_Pas:
            if any(character.isupper for character in New_Pas):
               if any(character.isdigit for character in New_Pas):
                  if any(character in "!@#$%^&*()" for character in New_Pas):
                     cursor.execute("UPDATE UserTable SET Passcode = ? WHERE Username = ?", (New_Pas,TrueUsername))
                     conn.commit()
                     cursor.close()
                     return render_template('/partials/homepage.html', Success="", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
                  else:
                     return render_template('/partials/homepage.html', Success="The new password did not contain special characters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
               else:
                  return render_template('/partials/homepage.html', Success="The new password did not contain any numbers.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
            else:
               return render_template('/partials/homepage.html', Success="The new password did not contain any capital letters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
         else:
            return render_template('/partials/homepage.html', Success="The password inputted was not correct.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
         
   if TrueUsername != "":
      return render_template('/partials/homepage.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang)
   return render_template('/partials/homepage.html', ProgramLangu=ProgramLang)

@app.route('/messages.html', methods=['GET','POST'])
@app.route('/', methods=['POST', 'GET'])
def messages():
   global TrueUsername,ProgramLang

   if request.method == "POST":
      if request.form["typing"].strip() == "TheDeleteMessage":
         execution = request.form["whatToDelete"].strip()
         conn = connection()
         cursor = conn.cursor()
         cursor.execute("DELETE FROM Answers WHERE Message_ID = ?", (execution,))
         cursor.execute("DELETE FROM Messages WHERE Message_ID = ?", (execution,))
         conn.commit()
         cursor.close()

      if request.form["typing"].strip() == "SendingMessage":
         adding = request.form["inputmessage"].strip()
         conn = connection()
         cursor = conn.cursor()
         userData = dbHandler.userTable()
         messageData = dbHandler.messageTable()
         MyUserId = ""
         MyMessages = []
         if TrueUsername != "":
            for usersdatas in userData:
               if usersdatas[1] == TrueUsername:
                  MyUserId = usersdatas[0]
                  break
            for messagesdatas in messageData:
               if (messagesdatas[1] == MyUserId) and (messagesdatas[4] == ProgramLang):
                  MyMessages.append(messagesdatas)

         if MyUserId != "":
            for messagesMy in MyMessages:
               if messagesMy[2] != adding:
                  ""
               else:
                  break
            else:
               cursor.execute("INSERT INTO Messages (User_ID, Message_Text, Programming_language) VALUES (?,?,?)", (MyUserId,adding,ProgramLang))
         conn.commit()
         cursor.close()

   userData = dbHandler.userTable()
   messageData = dbHandler.messageTable()
   answerData = dbHandler.answerTable()
   
   if TrueUsername != "":
      for usersdatas in userData:
         if usersdatas[1] == TrueUsername:
            MyUserId = usersdatas[0]
            break
      MyMessages = []
      MyAnswers = []
      for messagesdatas in messageData:
         if (messagesdatas[1] == MyUserId) and (messagesdatas[4] == ProgramLang):
            MyMessages.append(messagesdatas)
            MyMessageAnswers = []
            for answersdatas in answerData:
               if (answersdatas[1] == messagesdatas[0]):
                  MyMessageAnswers.append(answersdatas)
            MyAnswers.append(MyMessageAnswers)

   if request.method == "POST":

      if request.form["typing"].strip() == "LoggingOut":
         TrueUsername = ""
         ProgramLang = ""

      elif request.form["typing"].strip() == "LoginChange":
         Old_Pas = request.form["oldpassword"].strip()
         New_Pas = request.form["newpassword"].strip()
         conn = connection()
         cursor = conn.cursor()
         users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (TrueUsername,))
         row = users.fetchall()
         if row[0]["Passcode"] == Old_Pas:
            if any(character.isupper for character in New_Pas):
               if any(character.isdigit for character in New_Pas):
                  if any(character in "!@#$%^&*()" for character in New_Pas):
                     cursor.execute("UPDATE UserTable SET Passcode = ? WHERE Username = ?", (New_Pas,TrueUsername))
                     conn.commit()
                     cursor.close()
                     return render_template('/partials/messages.html', Success="", UserNamed=TrueUsername, ProgramLangu=ProgramLang)
                  else:
                     return render_template('/partials/messages.html', Success="The new password did not contain special characters.", UserNamed=TrueUsername, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,ProgramLangu=ProgramLang)
               else:
                  return render_template('/partials/messages.html', Success="The new password did not contain any numbers.", UserNamed=TrueUsername, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,ProgramLangu=ProgramLang)
            else:
               return render_template('/partials/messages.html', Success="The new password did not contain any capital letters.", UserNamed=TrueUsername, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,ProgramLangu=ProgramLang)
         else:
            return render_template('/partials/messages.html', Success="The password inputted was not correct.", UserNamed=TrueUsername, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,ProgramLangu=ProgramLang)
         
   if TrueUsername != "":
      return render_template('/partials/messages.html', UserNamed=TrueUsername, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,ProgramLangu=ProgramLang)
   return render_template('/partials/messages.html', ProgramLangu=ProgramLang)

@app.route('/login.html', methods=['GET','POST'])
@app.route('/', methods=['POST', 'GET'])
def login():
   global TrueUsername,ProgramLang
   if request.method == "POST":
      if request.form["typing"].strip() == "LoggingOut":
         TrueUsername = ""
         ProgramLang = ""

      elif request.form["typing"].strip() == "LoginChange":
         Old_Pas = request.form["oldpassword"].strip()
         New_Pas = request.form["newpassword"].strip()
         conn = connection()
         cursor = conn.cursor()
         users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (TrueUsername,))
         row = users.fetchall()
         if row[0]["Passcode"] == Old_Pas:
            if any(character.isupper for character in New_Pas):
               if any(character.isdigit for character in New_Pas):
                  if any(character in "!@#$%^&*()" for character in New_Pas):
                     cursor.execute("UPDATE UserTable SET Passcode = ? WHERE Username = ?", (New_Pas,TrueUsername))
                     conn.commit()
                     cursor.close()
                     return render_template('/partials/login.html', Success="", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
                  else:
                     return render_template('/partials/login.html', Success="The new password did not contain special characters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
               else:
                  return render_template('/partials/login.html', Success="The new password did not contain any numbers.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
            else:
               return render_template('/partials/login.html', Success="The new password did not contain any capital letters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
         else:
            return render_template('/partials/login.html', Success="The password inputted was not correct.", UserNamed=TrueUsername,ProgramLangu=ProgramLang)
         
   if TrueUsername != "":
      return render_template('/partials/login.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang)
   
   if request.method == "POST":
      username = request.form["username"].strip()
      passcode = request.form["password"].strip()
      type = request.form["Type"].strip()

      conn = connection()
      cursor = conn.cursor()
      users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (username,))

      if type == "Login":
         row = users.fetchall()
         cursor.close()
         if (username != "") and (passcode != ""):
            if len(row) > 0:
               if row[0]["Passcode"] == passcode:
                  TrueUsername = username
                  ProgramLang = row[0]["Programming_language"]
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

@app.route('/signin.html', methods=['GET','POST'])
@app.route('/', methods=['POST', 'GET'])
def signin():
   global TrueUsername,ProgramLang,Filter

   if request.method == "POST":

      if request.form["typing"].strip() == "DeleteFilter":
         Filter = ""

      if request.form["typing"].strip() == "SendingAnswer":
         userData = dbHandler.userTable()
         if TrueUsername != "":
            for usersdatas in userData:
               if usersdatas[1] == TrueUsername:
                  MyUserId = usersdatas[0]
                  break
         text = request.form["inputanswer"].strip()
         idmes = request.form["messageid"].strip()

         if TrueUsername != "":
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Answers (Message_ID, User_ID, Answer_Text) VALUES (?,?,?)", (idmes,MyUserId,text))
            conn.commit()
            cursor.close()

      if request.form["typing"].strip() == "SearchingMessage":
         Filter = request.form["SearchMes"].strip()

         userData = dbHandler.userTable()
         messageData = dbHandler.messageTable()
         answerData = dbHandler.answerTable()

         if TrueUsername != "":
            for usersdatas in userData:
               if usersdatas[1] == TrueUsername:
                  MyUserId = usersdatas[0]
                  break
            MyMessages = []
            MyAnswers = []
            for messagesdatas in messageData:
               if (messagesdatas[4] == ProgramLang) and (Filter.lower() in messagesdatas[2].lower()):
                  MyMessages.append(messagesdatas)
                  MyMessageAnswers = []
                  for answersdatas in answerData:
                     if (answersdatas[1] == messagesdatas[0]):
                        MyMessageAnswers.append(answersdatas)
                  MyAnswers.append(MyMessageAnswers)
            return render_template('/partials/signin.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
         else:
            MyMessages = []
            MyAnswers = []
            for messagesdatas in messageData:
               if (messagesdatas[4] == ProgramLang) and (Filter.lower() in messagesdatas[2].lower()):
                  MyMessages.append(messagesdatas)
                  MyMessageAnswers = []
                  for answersdatas in answerData:
                     if (answersdatas[1] == messagesdatas[0]):
                        MyMessageAnswers.append(answersdatas)
                  MyAnswers.append(MyMessageAnswers)
            return render_template('/partials/signin.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, users_data=userData, myanswers=MyAnswers,VarFilter=Filter)


   userData = dbHandler.userTable()
   messageData = dbHandler.messageTable()
   answerData = dbHandler.answerTable()
   
   if TrueUsername != "":
      for usersdatas in userData:
         if usersdatas[1] == TrueUsername:
            MyUserId = usersdatas[0]
            break
   MyMessages = []
   MyAnswers = []
   for messagesdatas in messageData:
      if (messagesdatas[4] == ProgramLang) and (Filter in messagesdatas[2]):
         MyMessages.append(messagesdatas)
         MyMessageAnswers = []
         for answersdatas in answerData:
            if (answersdatas[1] == messagesdatas[0]):
               MyMessageAnswers.append(answersdatas)
         MyAnswers.append(MyMessageAnswers)


   if request.method == "POST":
      if request.form["typing"].strip() == "LoggingOut":
         TrueUsername = ""
         ProgramLang = ""

      elif request.form["typing"].strip() == "LoginChange":
         Old_Pas = request.form["oldpassword"].strip()
         New_Pas = request.form["newpassword"].strip()
         conn = connection()
         cursor = conn.cursor()
         users = cursor.execute("SELECT * FROM UserTable WHERE Username = ?", (TrueUsername,))
         row = users.fetchall()
         if row[0]["Passcode"] == Old_Pas:
            if any(character.isupper for character in New_Pas):
               if any(character.isdigit for character in New_Pas):
                  if any(character in "!@#$%^&*()" for character in New_Pas):
                     cursor.execute("UPDATE UserTable SET Passcode = ? WHERE Username = ?", (New_Pas,TrueUsername))
                     conn.commit()
                     cursor.close()
                     return render_template('/partials/signin.html', Success="", UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
                  else:
                     return render_template('/partials/signin.html', Success="The new password did not contain special characters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
               else:
                  return render_template('/partials/signin.html', Success="The new password did not contain any numbers.", UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
            else:
               return render_template('/partials/signin.html', Success="The new password did not contain any capital letters.", UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
         else:
            return render_template('/partials/signin.html', Success="The password inputted was not correct.", UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
   
   if TrueUsername != "":
      return render_template('/partials/signin.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang, mymessages=MyMessages, myanswers=MyAnswers, users_data=userData,VarFilter=Filter)
   return render_template('/partials/signin.html', UserNamed=TrueUsername,ProgramLangu=ProgramLang,VarFilter=Filter,mymessages=MyMessages, myanswers=MyAnswers, users_data=userData)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)

