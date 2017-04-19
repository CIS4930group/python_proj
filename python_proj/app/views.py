from flask import render_template, request, flash, make_response
import requests
import re
import shelve
from app import app
from app.recipescraper import getFood
from app.database import storeUsers

@app.route('/', methods=['GET', 'POST'])
def index():
    info=[]
    if request.method == 'POST':
     #   if request.form['submit2'] == 'submitted':
     #       resp = make_response('')
     #       resp.set_cookie(temps,temp2)

        if request.form['submit1'] == 'submitted':
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

                 
                info.append(temp2)                  #make recipe name a title
        elif request.form['random'] == 'action':
            print("Pressed this")

    return render_template('index.html', info=info)

@app.route('/signin.html', methods=['GET', 'POST'])
def signin():
  if request.method == 'POST':
    if request.form['submit1'] == 'submitted':
      s = shelve.open('users.db')
      #checks if account has been created with the username being the key
      if str(request.form.get('inputName'))in s['key1']:
        #checks if the password input matched the username's password in the database
        if s['key1'][request.form.get('inputName')] == str(request.form.get('inputPassword')):
          print "sign in successful"
        else:
          print "Password is incorrect"
      else:
        print "account not registered"



  return render_template('signin.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    if request.form['submit1'] == 'submitted':
      user = str(request.form.get('inputName'))
      passw = str(request.form.get('inputPassword'))
      message = storeUsers(user, passw)
      #posts status of account creation in terminal
      if(message == 'failed'):
        print "Username is already taken, try again"
      else:
        print "Account successfully created"


  return render_template('register.html')
