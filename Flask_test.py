from flask import Flask, render_template,url_for
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        meme_data = response.json()
        meme_large = meme_data["preview"][-2]
        subreddit = meme_data["subreddit"]
        return meme_large, subreddit
    except requests.exceptions.RequestException as e:
        print(f"Error in request: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    # Return some default values or handle the error accordingly
    return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="100")
