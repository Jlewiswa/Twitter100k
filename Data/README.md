Twitter100k - data
================

Collect tweets from twitter list members, and each member's klout score, where
available. Originally designed to pull 100,000 tweets from users of the twitter
team list.

External Dependencies
=====================
- python-mysqldb
- tweepy
- PyKlout

New
=======
- Now collects 'created' datetime stamp
- Retweeted flag can now be set (mostly) accurately by running dbop.setRetweetedFlags()

Open Issues
===========

- mysql transactions are pretty slow, and seem to be holding up the tweet gathering,
    see about running them on their own thread or something
- Klout error handling could be improved, it currently registers all exceptions
    as the user having 'opted out' of klout, but other conditions such as service
    interruption or throttling could occur.
- Twitter flow is pretty specific, it would be good to break up user and tweet collection