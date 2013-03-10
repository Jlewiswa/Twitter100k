import dbop
import twitterop
import kloutop

#Get twitter users from configured list and gather tweets for each
twitterop.getTweets()

#query sql db for users and update all user objects with klout score
kloutop.updateScores()

#close the db when we're done.
dbop.close()