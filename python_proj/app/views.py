from flask import render_template, request, flash
from app import app
from app.recipescraper import getFood

@app.route('/', methods=['GET', 'POST'])
def index():
    info=[]
    if request.method == 'POST':
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
                info.append(temp2.title())                  #make recipe name a title
        elif request.form['random'] == 'action':
            print("Pressed this")
    return render_template('index.html', info=info)
