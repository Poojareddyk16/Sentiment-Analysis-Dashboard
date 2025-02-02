import tweepy
import pandas as pd
from textblob import TextBlob
import datetime
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only required once)
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    
    # Classify sentiment using compound thresholds
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return compound, sentiment

# ----------------------------
# Twitter (X) API v2 setup
# ----------------------------
BEARER_TOKEN = ""  # Replace with your actual Bearer Token

client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

# ----------------------------
# Define a list of tech companies using Twitter handles
# ----------------------------
tech_handles = ["@Apple", "@Samsung", "@NVIDIA", "@Google", "@Microsoft"]

# Build a query that targets these handles (using OR) and excludes retweets.
# This query returns tweets in English.
query = "(" + " OR ".join(tech_handles) + ") -is:retweet lang:en"

# ----------------------------
# Fetch recent tweets using the search_recent_tweets endpoint.
# ----------------------------
# Here we request the "created_at" field
response = client.search_recent_tweets(query=query, tweet_fields=["created_at"], max_results=100)

tweets = response.data if response.data is not None else []
tweets_data = []

# Helper function: identify which companies are mentioned in a tweet
def detect_companies(tweet_text, companies):
    found = [comp for comp in companies if comp.lower() in tweet_text.lower()]
    return ", ".join(found) if found else None

# ----------------------------
# Process each tweet
# ----------------------------
for tweet in tweets:
    text = tweet.text
    created_at = tweet.created_at  # datetime object
    tweet_id = tweet.id
    
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)
    polarity, sentiment = analyze_sentiment_vader(text)
    subjectivity = analysis.sentiment.subjectivity

    # Determine which companies are mentioned in the tweet
    companies_mentioned = detect_companies(text, tech_handles)
    
    tweets_data.append({
        "tweet_id": tweet_id,
        "created_at": created_at,
        "text": text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment": sentiment,
        "companies_mentioned": companies_mentioned,
        "analysis_date": datetime.datetime.now()
    })

# ----------------------------
# Create a DataFrame and derive additional columns
# ----------------------------
df = pd.DataFrame(tweets_data)

# Derive the tweet date (for time-series aggregation in Tableau)
if not df.empty:
    df['created_date'] = df['created_at'].dt.date
else:
    print("No tweets fetched. Please check your query or API access.")

# ----------------------------
# Export the final table to CSV for Tableau import
# ----------------------------
output_csv = "tech_sentiment_data.csv"
df.to_csv(output_csv, index=False)
print(f"Data exported successfully to {output_csv}")
