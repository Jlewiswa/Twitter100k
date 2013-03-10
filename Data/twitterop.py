import dbop
import keys
import tweepy
import datetime
import time

ckey = keys.getKey('Twitter','consumer_key')
csecret = keys.getKey('Twitter','consumer_secret')
akey = keys.getKey('Twitter','access_key')
asecret = keys.getKey('Twitter','access_secret')

list_slug = keys.getKey('Twitter', 'list_slug')
list_owner = keys.getKey('Twitter', 'list_owner')
tweets_per_user = keys.getKey('Twitter','tweets_per_user')
include_rts = bool(keys.getKey('Twitter', 'include_rts'))

# Set authentication info for twitter OAuth
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)

# Grab all members from the twitter team list, and the configurable quantity of
# tweets from each. Add the users and tweets to the db as we get them.

# Note: 80 tweets * 1250 users = 100k tweets. 100 tweets each accounts for users with
# lower usage
def getTweets():
    timeout = None
    api = tweepy.API(auth)
    cursor = tweepy.Cursor(api.list_members, list_owner, list_slug)
    for page in cursor.pages():
        print 'page',cursor.iterator.count
        pageDone = False
        while not pageDone:
            try:
                for item in page:
                    try:
                        print item.screen_name
                        dbop.addUser(item)
                        timeline = api.user_timeline(count=tweets_per_user, user_id = item.id, trim_user=True, include_rts=include_rts)
                        for tweet in timeline:
                            dbop.addTweet(tweet)
                    # Some twitter profiles are private, skip these
                    except tweepy.error.TweepError, e:
                        if e.reason == "Not authorized":
                            continue
                        else:
                            raise e
                    dbop.commit()
                pageDone = True
            # Twitter has rate limits. Wait them out here.
            except tweepy.error.TweepError, e:
                print e.reason
                timeout = datetime.datetime.now() + datetime.timedelta(minutes = 15)
                while datetime.datetime.now() < timeout:
                    time.sleep(1)