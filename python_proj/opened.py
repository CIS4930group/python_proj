#if you want to see whats stored in the database, run this program instead of run.py
import shelve

s = shelve.open('users.db')
existing = s['key1']
s.close()

print existing
