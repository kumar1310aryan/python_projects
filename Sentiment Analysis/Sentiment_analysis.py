from textblob import TextBlob

def analyze_sentiment(text):
    
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, sentiment_polarity

if __name__ == "__main__":
    user_text = input("Please enter the text you want to analyze the sentiment of: ")
    
    sentiment, polarity = analyze_sentiment(user_text)
    
    print(f"Detected sentiment: {sentiment}")
    print(f"Sentiment polarity: {polarity}")
