Twitter100k - webhost
================

Displays 3 graphs for data collected by Twitter100k_Data. The first shows the
top 10 users in the database, sorted by most retweeted content (currently broken
due to a bug with tweepy). The second shows the top 10 most retweeted tweets,
and the third shows the top 10 users by klout score.

External Dependencies
=====================
python-mysqldb
pygooglechart
bottlepy

Open Issues
===========
- Server loses connection to db after a bit. Should put some error handling in
- nodata.png isn't being displayed correctly, need to configure static files
- Garbled text on top 10 retweets graph. Those twitter IDs are really long.
    Use a horizontal graph?
- Graph y_range min/max values aren't always producing great visual results.
    Need to find a better way to calculate.