import dbop
import graphop
from bottle import route, run

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

run(host='localhost', port=8081)