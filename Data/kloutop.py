import keys
import dbop
from klout import *

# Set the Klout auth key
api = Klout(keys.getKey('Klout', 'key'),secure=True)

# Grab scores for each klout user currently in sql. Sets -1 for
# scores that are unavailable
def updateScores():
    users = dbop.getUsersForKloutUpdate()
    for user in users:
        try:
            print user[1]
            id = api.identity.klout(screenName=user[1]).get('id')
            score = api.user.score(kloutId=id).get('score')
            dbop.updateKloutScore(user[0], score)
        # TODO: expand the error handling a bit to register a difference between
        # unavailable klout score and other problems such as auth failure or
        # service interruption
        except:
            dbop.updateKloutScore(user[0], -1)