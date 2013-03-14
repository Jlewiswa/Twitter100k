import dbop
import graphop
from bottle import route, run

# On requests to /, collect data from sql and apply it to the html template
# then return it for the user to see
@route('/')
def index():
    dbTweets = dbop.getTweetsByHour()
    tweets = None
    nodata = 'nodata.png'
    if len(dbTweets) < 24:
        tweets = nodata
    else:
        tweets = graphop.getLineGraph(dbTweets,'1ab2e8','e34703')
    file = open('graph_template.html','r').read()
    scoresPage = file.format(tweets=tweets)
    return scoresPage

# start up the server on load
run(host='localhost', port=8081)