import MySQLdb
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.cfg')

# SQL db config
host = config.get('SQL','host')
user = config.get('SQL','user')
passwd = config.get('SQL','passwd')
dbname = config.get('SQL','dbname')

# Open the db connection, open a new cursor object. Commits must be made manually
# by calling commit() below.
db = MySQLdb.connect(host=host,user=user,passwd=passwd,db=dbname)
cursor = db.cursor()

def getTopUsers():
    cursor.execute("""SELECT users.screen_name,SUM(tweets.retweets) AS rt_sum
                    FROM users JOIN tweets ON users.id = tweets.user_id
                    WHERE tweets.retweeted = 0
                    GROUP BY users.screen_name
                    ORDER BY rt_sum DESC LIMIT 10""")
    return cursor.fetchall()

def getTopTweets():
    cursor.execute("SELECT tweets.id,tweets.retweets FROM tweets ORDER BY tweets.retweets DESC LIMIT 10")
    return cursor.fetchall()

def getTopKloutScores():
    cursor.execute("SELECT users.screen_name,users.klout_score FROM users ORDER BY users.klout_score DESC LIMIT 10")
    return cursor.fetchall()

# Close the db when we're done.
def close():
    db.close()