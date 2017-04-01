#attempting to scrape recipes.com
from __future__ import print_function
import requests, re, sys
import random

mains = ['chicken', 'beef', 'turkey', 'shrimp', 'salmon', 'tofu', 'pork', 'vegetarian']
sides =['rice', 'potatoe', 'quinoa', 'pasta', 'sweet potato', 'black beans', 'baked beans', 'corn']
veg = ['broccoli', 'green beans', 'peas', 'spinach', 'asparagus', 'kale', 'brussels sprouts', 'cauliflower']

rand1 = random.choice(mains)
rand2 = random.choice(sides)
rand3 = random.choice(veg)

print(rand1)
print(rand2)
print(rand3)

url1 = ""
url3 = ""

if ' ' in rand2:
	temps = rand2.split(" ")
	url1 = "http://allrecipes.com/search/results/?wt=" + rand1 + "%20" + temps[0] + "%20" + temps[1] + "%20"
	url3 = "http://www.recipe.com/search/?searchType=recipe&searchTerm=" + rand1 + "+" + temps[0] + "+" + temps[1] + "+"
else:
	url1 = "http://allrecipes.com/search/results/?wt=" + rand1 + "%20" + rand2 + "%20"
	url3 = "http://www.recipe.com/search/?searchType=recipe&searchTerm=" + rand1 + "+" + rand2 + "+"


url2 = ""
url4 = ""
if ' ' in rand3:
	temps = rand3.split(" ")
	url2 = url1 + temps[0] + "%20" + temps[1] + "&sort=re"
	url4 = url3 + temps[0] + "+" + temps[1]
else:
	url2 = url1 + rand3 + "&sort=re"
	url4 = url3 + rand3


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
	print(random.choice(urls))
else:
	print("Sorry! No recipes exist for that combination!")

