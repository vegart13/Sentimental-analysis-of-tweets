# Sentimental-analysis-of-tweets
Using tweepy, textblob, numpy and pandas the program analyses the sentimentality of each tweet from a twitter user.

Remember to sign up for the Twitter API here: 
https://developer.twitter.com/en
You will first need to create an account, verified with email if you don't have one already. If you do just login in and create new application.

Note that the twitter API limits users in the timespan you are able to retrieve tweets from. I found that it only goes as far back as a week, although it is a great way of playing around with Twitter's API. 

Set up correctly this program will: 
1. Authenticate with the twitter API 
2. Fetch tweets from the twitter API
3. Clean up fetched tweets 
4. Add information to a dataframe 
5. Judge sentimentality of each tweet
6. Display tweets with information you are interested in presenting
