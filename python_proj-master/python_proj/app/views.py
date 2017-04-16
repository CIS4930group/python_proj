from flask import render_template, request, flash, make_response
import requests
import re
from app import app
from app.recipescraper import getFood

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

@app.route('/signin.html')
def signup():
    return render_template('signin.html')

@app.route('/register.html')
def register():
    return render_template('register.html')