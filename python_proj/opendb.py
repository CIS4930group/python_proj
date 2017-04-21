#if you want to see whats stored in the database, run this program instead of run.py
import shelve

s = shelve.open('users.db')
for user in s:
	print user, s[user] 		#prints username, then password and favorites

s.close()


