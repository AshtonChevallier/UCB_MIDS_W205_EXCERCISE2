import tweepy

consumer_key = "Ha7USGl0eAZdqZbipGDP0db6X";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "9mZs4qXWNmogspjDzPaTLGNMz8lVz3MtOnTa7subyQHFcDy5NA";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "29976503-Dww5FXR8g6zJrYkxLo7QRt3JGRml5xAgahTEw12m5";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "RmjaKzbqJVAvSVgMb0zjFBwqP2VhXNd1girU9Y5O5TBJ6";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
