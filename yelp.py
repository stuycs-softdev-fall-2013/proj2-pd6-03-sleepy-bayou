import oauth2

# Fill in these values
consumer_key = 'YQjC8cOZxSyb-x21hpoLxg'
consumer_secret = 'AJ6u905ojzMr9VkHDN_BkAbQrIA'
token = '4Q20XFJ24cB8SL1CRKWY_2kNYqGnk60y'
token_secret = '2hPhKm5s4kt8L5EicFD3h26cLh4'

def breakfast_search(searchkey, neighborhood):
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    url = 'http://api.yelp.com/v2/search?term=breakfast'+ '+' + searchkey + '&location=nyc' + '+' + neighborhood
    return oauth2.Request('GET', url, {})

def lunch_search(searchkey, neighborhood):
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    url = 'http://api.yelp.com/v2/search?term=lunch'+ '+' + searchkey + '&location=nyc' + '+' + neighborhood
    return oauth2.Request('GET', url, {})

def dinner_search(searchkey, neighborhood):
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    url = 'http://api.yelp.com/v2/search?termdinner'+ '+' + searchkey + '&location=nyc' + '+' + neighborhood
    return oauth2.Request('GET', url, {})

