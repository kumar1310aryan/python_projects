from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    # Get the sentiment polarity
    sentiment_polarity = blob.sentiment.polarity
    
    # Determine the sentiment category
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, sentiment_polarity

if __name__ == "__main__":
    # Get user input
    user_text = input("Please enter the text you want to analyze the sentiment of: ")
    
    # Analyze the sentiment of the user input
    sentiment, polarity = analyze_sentiment(user_text)
    
    # Print the sentiment analysis result
    print(f"Detected sentiment: {sentiment}")
    print(f"Sentiment polarity: {polarity}")
