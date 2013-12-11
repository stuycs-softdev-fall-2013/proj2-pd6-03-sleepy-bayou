import oauth2
import json
import urllib
import urllib2

# Fill in these values 
def search(term, address):
    consumer_key = 'YQjC8cOZxSyb-x21hpoLxg'
    consumer_secret = 'AJ6u905ojzMr9VkHDN_BkAbQrIA'
    token = '4Q20XFJ24cB8SL1CRKWY_2kNYqGnk60y'
    token_secret = '2hPhKm5s4kt8L5EicFD3h26cLh4'
    consumer= oauth2.Consumer(consumer_key,consumer_secret)
    url= 'http://api.yelp.com/v2/search?term=%s&location=%s&limit=%d&format=json&radius_filter=400&category=food'%(term, address, 5)
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})
    
    token = oauth2.Token(token, token_secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    #connect
    try: 
        conn = urllib2.urlopen(signed_url)
        try:
            response =json.load(conn)
        finally:
            conn.close()
    except urllib2.HTTPError,error:
        response=json.load(error)
    results = []
    for places in response["businesses"]:
        results.append(places["name"])
    return results
