from flask import render_template
from app import app
from app.forms import CountrySearch
#from app.factbook_scraper import get_info

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

'''@app.route('/search', methods=['GET', 'POST'])
def search():
    info = None
    form = CountrySearch()
    if form.validate_on_submit():
        country = form.country_name.data
        #info = get_info(country)
    return render_template('search.html', title='Search for a country', form=form, info=info)
'''
