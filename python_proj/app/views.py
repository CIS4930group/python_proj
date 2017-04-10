from flask import render_template, request, flash
from app import app
from app.forms import Drop
from app.recipescraper import getFood
import requests, re

@app.route('/', methods=['GET', 'POST'])
def index():
    info=[]
    if request.method == 'POST' and request.form['submit1'] == 'submitted':
        select = request.form.get('maindish')
        select2 = request.form.get('sidedish')
        select3 = request.form.get('vegetable')
        temps = getFood(select, select2, select3) #get url or string
        info.append(temps)
        temp = temps.rsplit('/', 2)[-2]
        temp2 = temp.replace("-", " ")
        info.append(temp2.title())
    return render_template('index.html', info=info)
