import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = '***',
password = '***',
host = '***',
database = '***'
)
# required to input user information in place of ***

cursor = con.cursor()

word = input('Enter a word:')


query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if not results:
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '{}%' AND length(Expression)<{}".format(word[:-1],len(word)+1))
    results=cursor.fetchall()

if results:
	for result in results:
		print(result[0], ":", result[1])
else:
	print('no word found')