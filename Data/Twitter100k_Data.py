import dbop
import twitterop
import kloutop

#Get twitter users from configured list and gather tweets for each
twitterop.getTweets()

#Set retweeted flags based on tweet text starting with "RT"
dbop.setRetweetedFlags()

#query sql db for users and update all user objects with klout score
kloutop.updateScores()

#close the db when we're done.
dbop.close()