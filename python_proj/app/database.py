import shelve
import re
import requests

def storeUsers(user, passw):
	#tries to add to the DB if it exists
	try:
		s = shelve.open('users.db', writeback = True)
		if user in s: #replace matt with username
			s.close()
			return "failed"
		else:
			s[user]['password'] = passw
			#s['key1']['loggedIn'] = False

	#creates the db if it does not already exist
	except KeyError:
		favList = [] #25 most recent recipes searched
		s = shelve.open('users.db')
		s[user] = {'password': passw, 'favorites': favList}


	s.close()

def storeFav(user, fav):
        try:
                print "username: ",user
                s = shelve.open('users.db', writeback = True)
                favList = s[user]['favorites']
                #prevents duplicates
                if fav in favList:
                  favList.remove(fav)
                  favlist.append(fav)
                #saves only the most recent 25 recipes. Printed oldest to newest
                if (len(favList) < 25):
                  favList.append(fav)
                else:
                  favList.append(fav)
                  favList.pop(0)
                s[user]['favorites'] = favList
                print("favs are ",s[user]['favorites'])
                s.close()
                print "success"
        except:
                print "failure"

def getFavs(user):
       s = shelve.open('users.db', writeback = True)
       favList = s[user]['favorites']
       fav = [("","")]
       for f in favList:
           temp = f.rsplit('/', 2)[-2]             #get name of recipe
           temp2 = temp.replace("-", " ")
           temp2 = temp2.title()
           if (f[7]=='a'):
              page = requests.get(f)
              link = re.search(r'itemprop="name">([^<]+)',page.text)
              if link:
                 temp2 = link.group(1)        

           tup = (f,temp2)
           fav.append(tup)
 
       s.close()
       fav.pop(0)
       return fav
