# Commands that can be used in tandem with the sentimental analysis. Remember to put them into main

# Prints information on the most recent 20 tweets
print(df.head(20))

# Get average length of all tweets
print(np.mean(df['len']))

# Get number of likes for the most liked tweet
print(np.max(df['likes']))

# Get number of retweets for the most retweeded tweet
print(np.max(df['retweets']))

# Time Series
time_likes = pd.Series(data=df['likes'].values, index=df['date'])
time_likes.plot(figsize=(15, 4), label="likes", legend=True)

time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
time_retweets.plot(figsize=(15, 4), label="retweets", legend=True)
plt.show()
