import dbop
import graphop
from bottle import route, run

# On requests to /, collect data from sql and apply it to the html template
# then return it for the user to see
@route('/')
def index():
    dbTopUsers = dbop.getTopUsers()
    dbTopTweets = dbop.getTopTweets()
    dbTopKlout = dbop.getTopKloutScores()
    topUsers = None
    topTweets = None
    topKlout = None
    nodata = 'nodata.png'
    if len(dbTopUsers) < 10:
        topUsers = nodata
    else:
        topUsers = graphop.getGraph(dbTopUsers,'1ab2e8')
    if len(dbTopTweets) < 10:
        topTweets = nodata
    else:
        topTweets = graphop.getGraph(dbTopTweets,'1ab2e8')
    if len(dbTopKlout) < 10:
        topKlout = nodata
    else:
        topKlout = graphop.getGraph(dbTopKlout,'e34703')
    file = open('graph_template.html','r').read()
    scoresPage = file.format(top_users=topUsers,top_tweets=topTweets,top_klout=topKlout)
    return scoresPage

# start up the server on load
run(host='localhost', port=8081)