from flask import render_template, request, flash, make_response, redirect, url_for
import requests
import re
import shelve
from app import app
from app.recipescraper import getFood
from app.database import storeUsers, storeFav, getFavs


userLoggedIn = False
currentUser = ""

@app.context_processor
def addUser():
  return dict(user=currentUser)

@app.route('/', methods=['GET', 'POST'])
def index():
  info=[]
  if request.method == 'POST':
   if request.form['submit1'] == 'submitted':
      print("go pressed")
      select = request.form.get('maindish')
      select2 = request.form.get('sidedish')
      select3 = request.form.get('vegetable')
      if not select or not select2 or not select3:    #make sure the user actually selected something
          info=[]
      else:
        temps = getFood(select, select2, select3)   #get url or string
        info.append(temps)
        temp = temps.rsplit('/', 2)[-2]             #get name of recipe
        temp2 = temp.replace("-", " ")
        temp2 = temp2.title()
        if (temps[7]=='a'):
           page = requests.get(temps)
           link = re.search(r'itemprop="name">([^<]+)',page.text)
           if link:
              temp2 = link.group(1)

        print("temps is ",temps)
        print("temp2 is ",temp2)
        temp3 = str(temps)
        if currentUser!="":
           message = storeFav(currentUser,temp3)
        else:
           print "not logged in"
     
        info.append(temp2)      
  return render_template('index.html', info=info)

@app.route('/signin.html', methods=['GET', 'POST'])
def signin():
  passwordm=""
  acctm=""
  if request.method == 'POST':
    if request.form['submit2'] == 'submitted':
      s = shelve.open('users.db')
      #checks if account has been created with the username being the key
      try:
        if str(request.form.get('inputName'))in s:
          #checks if the password input matched the username's password in the database
          if s[str(request.form.get('inputName'))]['password'] == str(request.form.get('inputPassword')):
            global userLoggedIn
            userLoggedIn = True
            global currentUser
            currentUser = str(request.form.get('inputName'))
            return redirect(url_for('index'))
          else:
            passwordm = "Password was not correct. Please try again."
            return render_template('signin.html', passwordm=passwordm, acctm=acctm)
        else:
          acctm = "Please create an account before logging in."
          return render_template('signin.html', passwordm=passwordm, acctm=acctm)
      #runs if the database has not been created, and therefore, no accounts have been created
      except KeyError:
        print "account not registered"
  return render_template('signin.html', passwordm=passwordm, acctm=acctm)



@app.route('/register.html', methods=['GET', 'POST'])
def register():
  mess = ""
  if request.method == 'POST':
    if request.form['submit3'] == 'submitted':
      user = str(request.form.get('inputName'))
      passw = str(request.form.get('inputPassword'))
      message = storeUsers(user, passw)
      #posts status of account creation in terminal
      if(message == 'failed'):
        mess = "Username is already taken, try again."
        return render_template('register.html', mess=mess)
      else:
        global userLoggedIn
        mess = ""
        userLoggedIn = True
        global currentUser
        currentUser = user
        return redirect(url_for('index'))
  return render_template('register.html', mess=mess)


@app.route('/recent.html', methods=['GET', 'POST'])
def favorites():  
    noRec = ""
    global userLoggedIn
    if userLoggedIn == False:
      return render_template('recent.html', userLoggedIn=userLoggedIn) 
    else:
      faves = getFavs(currentUser)
      if len(faves) == 0:
        noRec = "No recipes searched yet"
      return render_template('recent.html',faves=faves, noRec=noRec, userLoggedIn=userLoggedIn) 

@app.route('/signout.html', methods=['GET', 'POST'])
def signout():
  if request.method == 'POST':
    if request.form['submit4'] == 'submitted':
      global userLoggedIn
      userLoggedIn = False
      global currentUser
      currentUser = ""
      return redirect(url_for('index'))
  return render_template('signout.html')
