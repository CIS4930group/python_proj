import shelve

def storeUsers(user, passw):
	#tries to add to the DB if it exists
	try:
		s = shelve.open('users.db', writeback = True)
		if user in s['key1']: #replace matt with username
			s.close()
			return "failed"
		else:
			s['key1'][user] = passw #user and pass

	#creates the db if it does not already exist
	except KeyError:
		s = shelve.open('users.db')
		s['key1'] = {user : passw}


	s.close()
