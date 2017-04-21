import shelve

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
		favList = []
		s = shelve.open('users.db')
		s[user] = {'password': passw, 'favorites': favList}


	s.close()

