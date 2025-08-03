from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "positive", polarity
    elif polarity < -0.1:
        return "negative", abs(polarity)
    else:
        return "neutral", 0.0
