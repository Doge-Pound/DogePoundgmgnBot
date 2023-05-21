import tweepy
import time
import requests
from io import BytesIO

# Credentials (Insert your keys and tokens below)
api_key = "updatethekeys"
api_secret = "updatethekeys"
bearer_token = "updatethekeys"
access_token = "updatethekeys"
access_token_secret = "updatethekeys"

//will improved using dot env and integrated CHATGPT API 

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# This is so the bot only looks for the most recent tweets.
start_id = 1
initialisation_resp = api.mentions_timeline(count=1)
if len(initialisation_resp) > 0:
    start_id = initialisation_resp[0].id

while True:
    response = api.mentions_timeline(since_id=start_id)

    if len(response) > 0:
        for tweet in response:
            try:
                print(tweet.text)
                # Check if the tweet contains an ID
                text = tweet.text
                if "@doge_gm n" in text:
                    # Get the username of the person who was replied to
                    replied_to_username = tweet.in_reply_to_screen_name

                    # Get the ID of the tweet to reply to
                    if tweet.in_reply_to_status_id is not None:
                        reply_to_id = tweet.in_reply_to_status_id
                    else:
                        reply_to_id = tweet.id

                    id = text.split()[-1]
                    url = f"https://d3cvnrw4bpahxk.cloudfront.net/thedogepound/gn/{id}.png"
                    response = requests.get(url)
                    if response.status_code == 200:
                        # If the image is successfully fetched, reply with the image and message
                        media = api.media_upload(filename=f"{id}.png", file=BytesIO(response.content))
                        api.update_status(status=f"gn gn Doge! @{replied_to_username} from @{tweet.user.screen_name}", in_reply_to_status_id=reply_to_id, media_ids=[media.media_id])
                    else:
                        # If the image is not found, reply with an error message
                        api.update_status(status="Sorry, the image was not found.", in_reply_to_status_id=reply_to_id)
                elif "@doge_gm" in text:
                    # Get the username of the person who was replied to
                    replied_to_username = tweet.in_reply_to_screen_name

                    # Get the ID of the tweet to reply to
                    if tweet.in_reply_to_status_id is not None:
                        reply_to_id = tweet.in_reply_to_status_id
                    else:
                        reply_to_id = tweet.id

                    id = text.split()[-1]
                    url = f"https://d3cvnrw4bpahxk.cloudfront.net/thedogepound/gm/{id}.png"
                    response = requests.get(url)
                    if response.status_code == 200:
                        # If the image is successfully fetched, reply with the image and message
                        media = api.media_upload(filename=f"{id}.png", file=BytesIO(response.content))
                        api.update_status(status=f"Good morning Doge! @{replied_to_username} from @{tweet.user.screen_name}", in_reply_to_status_id=reply_to_id, media_ids=[media.media_id])
                    else:
                        # If the image is not found, reply with an error message
                        api.update_status(status="Sorry, the image was not found.", in_reply_to_status_id=reply_to_id)

                # Update the start ID to the most recent tweet so the bot doesn't reply to the same tweet twice
                if tweet.id > start_id:
                    start_id = tweet.id

            except tweepy.TweepError as error:
                print(f"Error: {error}")

    # Wait for 10 seconds before checking again
    time.sleep(15)

