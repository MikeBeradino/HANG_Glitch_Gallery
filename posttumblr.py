import pytumblr
from tumblr_keys import *    #this imports the content in our tumblr_keys.py file

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

client.create_photo('hang-glitch-gallery', state="published", tags=["testing", "ok"], data="glitched/gm38.jpg")