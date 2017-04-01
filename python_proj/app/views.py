from flask import render_template, request, flash
from app import app
from app.forms import Drop
#from app.factbook_scraper import get_info

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['submit1'] == 'submitted':
        select = request.form.get('maindish')
        select2 = request.form.get('sidedish')
        select3 = request.form.get('vegetable')
        print(select + " " + select2 + " " + select3)
    return render_template('index.html')


'''
@app.route('/search', methods=['GET', 'POST'])
def search():
    info = None
    form = Drop()
    if form.validate_on_submit():
        country = form.main.data
        #info = get_info(country)
    return render_template('search.html', title='Search for a country', form=form, info=info)
'''
