import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(user_agent="Comment Extraction (by /u/	{USERNAME})",
                     client_id="CLIENTID", client_secret="SECRET")

def classify(myReddit):

    sia = SentimentIntensityAnalyzer()

    myList = []
    okay = reddit.subreddit(myReddit).top(limit=100)
    for x in okay:
        myList.append(x.title)


    positive = 0
    negative = 0
    neutral = 0
    for y in myList:
        pos = sia.polarity_scores(y)["pos"]
        neg = sia.polarity_scores(y)["neg"]

        
        if pos > neg:
            positive+=1
        elif neg > pos:
            negative+=1
        else:
            neutral += 1

    print(str(positive) + "%" + " Positive" + "\n" + str(negative) + "%" + " Negative" + "\n" + str(neutral) + "%" + " Neutral")

sub_red = input("Enter a subreddit:")    
    
classify(sub_red)

    
