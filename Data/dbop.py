import MySQLdb
import keys

# Get SQL db config
host = keys.getKey('SQL','host')
user = keys.getKey('SQL','user')
passwd = keys.getKey('SQL','passwd')
dbname = keys.getKey('SQL','dbname')

# Open the db connection, open a new cursor object. Commits must be made manually
# by calling commit() below.
db = MySQLdb.connect(host=host,user=user,passwd=passwd,db=dbname)
db.autocommit(False)
cursor = db.cursor()

# Adds a twitter user to the sql db. Requires id and screen_name attributes
# klout score defaults to -1 so we know to update it later
def addUser(user):
    sql = "INSERT IGNORE INTO users (id,screen_name,klout_score) VALUES (%s,%s,%s)"
    cursor.execute(sql,(user.id,user.screen_name,-1))

# Get all id and screen_names with previously unset klout scores from the database.
# Used for updating klout score
def getUsersForKloutUpdate():
    cursor.execute("SELECT id,screen_name FROM users WHERE klout_score = -1")
    return cursor.fetchall()

# Add tweet content to sql. Includes user id, tweet id, tweet text, retweet_count
# and retweeted bool from the tweepy object. Retweeted bool is currently broken,
# only returns false
def addTweet(content):
    sql = "INSERT IGNORE INTO tweets (id,user_id,text,retweets,retweeted) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql,(content.id,content.user.id,content.text.encode('ascii', 'ignore'),content.retweet_count,int(content.retweeted)))

# Update sql with current klout score.
def updateKloutScore(userid,score):
    sql = "UPDATE users SET klout_score = %s WHERE id = %s"
    cursor.execute(sql,(score,userid))

# Commit changes made by the cursor above.
def commit():
    db.commit()

# Close the db when we're done.
def close():
    db.close()

# On creation of the class, make sure the tables we need are ready to go.
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id BIGINT NOT NULL PRIMARY KEY,
                        screen_name VARCHAR(50),
                        klout_score INT,
                        klout_reliability INT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS tweets (
                        id BIGINT NOT NULL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        text VARCHAR(255),
                        retweets INT,
                        retweeted TINYINT(1))""")
commit()