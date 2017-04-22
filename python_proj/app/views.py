from flask import render_template, request, flash, make_response, redirect, url_for
import requests
import re
import shelve
from app import app
from app.recipescraper import getFood
from app.database import storeUsers, storeFav, getFavs


userLoggedIn = False
currentUser = ""
@app.route('/', methods=['GET', 'POST'])
def index():
        info=[]
        if request.method == 'POST':
             '''
             if request.form['submit1'] == 'faved':
                 print("faved pressed")
                 s = shelve.open('users.db')
                 if userLoggedIn:
                    favorite = ""
                    #favorite = str(request.form.get('info'))
                    print favorite
                    if favorite!="":
                       print(currentUser)
                       message = storeFav(currentUser,favorite)
                       print message
             '''





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
                 
                    info.append(temp2)                  #make recipe name a title
             elif request.form['random'] == 'action':
                print("Pressed this")

        
        return render_template('index.html', info=info)

@app.route('/signin.html', methods=['GET', 'POST'])
def signin():
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
            print "user is "+str(currentUser)+"."
            print "sign in successful"
            #return render_template('index.html')
            return redirect(url_for('index'))
          else:
            print "Password is incorrect"
        else:
          print "account not registered"
      #runs if the database has not been created, and therefore, no accounts have been created
      except KeyError:
        print "account not registered"



  return render_template('signin.html')



@app.route('/register.html', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    if request.form['submit3'] == 'submitted':
      user = str(request.form.get('inputName'))
      passw = str(request.form.get('inputPassword'))
      message = storeUsers(user, passw)
      #posts status of account creation in terminal
      if(message == 'failed'):
        print "Username is already taken, try again"
      else:
        print "Account successfully created"
        global userLoggedIn
        userLoggedIn = True
        global currentUser
        currentUser = user
	return redirect(url_for('index'))

  return render_template('register.html')


@app.route('/favorites.html', methods=['GET', 'POST'])
def favorites():  
  #if request.method == 'POST':

    if userLoggedIn == False:
      return redirect(url_for('signin'))

    faves = getFavs(currentUser)
    print(faves)
    return render_template('favorites.html',faves=faves) 

