#attempting to scrape recipes.com
from __future__ import print_function
import requests, re, sys
import random

def getFood(main, side, veg):
	mains = ['chicken', 'beef', 'turkey', 'shrimp', 'salmon', 'tofu', 'pork', 'vegetarian']
	sides =['rice', 'potatoe', 'quinoa', 'pasta', 'sweet potato', 'black beans', 'baked beans', 'corn']
	vegs = ['broccoli', 'green beans', 'peas', 'spinach', 'asparagus', 'kale', 'brussels sprouts', 'cauliflower']
	if main in mains:
		mainD = main
	else:
		mainD = random.choice(mains)
	if side in sides:
		sideD = side
	else:
		sideD = random.choice(sides)
	if veg in vegs:
		vegD = veg
	else:
		vegD = random.choice(vegs)
	
	print(mainD)
	print(sideD)
	print(vegD)

	url1 = ""
	url3 = ""

	if ' ' in sideD:
		temps = sideD.split(" ")
		url1 = "http://allrecipes.com/search/results/?wt=" + mainD + "%20" + temps[0] + "%20" + temps[1] + "%20"
		url3 = "http://www.recipe.com/search/?searchType=recipe&searchTerm=" + mainD + "+" + temps[0] + "+" + temps[1] + "+"
	else:
		url1 = "http://allrecipes.com/search/results/?wt=" + mainD + "%20" + sideD + "%20"
		url3 = "http://www.recipe.com/search/?searchType=recipe&searchTerm=" + mainD + "+" + sideD + "+"


	url2 = ""
	url4 = ""
	if ' ' in vegD:
		temps = vegD.split(" ")
		url2 = url1 + temps[0] + "%20" + temps[1] + "&sort=re"
		url4 = url3 + temps[0] + "+" + temps[1]
	else:
		url2 = url1 + vegD + "&sort=re"
		url4 = url3 + vegD


	main_page = requests.get(url2)
	link = re.findall(r'/recipe/(.*)/', main_page.text)
	urls = []
	for i in link:
		temp = "http://allrecipes.com/recipe/"
		url12 = temp + i.encode("utf-8")
		urls.append(url12)

	main_page2 = requests.get(url4)
	link2 = re.findall(r'<h3><a href="http://(.*)">', main_page2.text)
	for i in link2:
		temp = "http://" + i.encode("utf-8")
		if temp not in urls:
			urls.append(temp)

	if len(urls) != 0:
		return random.choice(urls)
	else:
		return "Sorry! No recipes exist for that combination!"

