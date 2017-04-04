from flask import render_template, request, flash
from app import app
from app.forms import Drop
from app.recipescraper import getFood

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['submit1'] == 'submitted':
        select = request.form.get('maindish')
        select2 = request.form.get('sidedish')
        select3 = request.form.get('vegetable')
        str1 = getFood(select, select2, select3) #get url or string
    return render_template('index.html')
