import MySQLdb
import ConfigParser

# Grab data from the config file
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

# Query sql for tweets, retweets, and hours. Then group by hour and show a
# total count for tweets and retweets for each hour available. Set to PST,
# exclude datetimes that haven't been set.
def getTweetsByHour():
    cursor.execute("""SELECT COUNT(*), SUM(retweeted = 1),
                    HOUR( CONVERT_TZ( created, '+00:00', '-08:00' ) ) AS crt
                    FROM tweets WHERE created > 0
                    GROUP BY crt ORDER BY crt""")
    return cursor.fetchall()

# Close the db when we're done. Probably won't get called, but it should.
def close():
    db.close()