# Web-Scraping 101
Note that any activity that scrapes or collects data from online platforms should strictly adhere to the respective platform's terms of service, API usage guidelines, and any relevant laws or regulations.
_Don’t hardcode your credentials_

## Social Media Information:
1. **Use Official APIs**:
    - Many social media platforms, like Twitter, Facebook, and Instagram, offer Application Programming Interfaces (APIs). These allow developers to retrieve data in a structured manner. For instance, Twitter's API can be accessed using libraries like Tweepy in Python.
    - **Pros**: Structured, reliable, and typically includes metadata.
    - **Cons**: Often rate-limited, requires API keys, may have costs associated, and might not provide access to all data.

2. **Web Scraping**:
    - Tools like Scrapy, Beautiful Soup (for Python), or Puppeteer (for JavaScript) can be used to scrape social media pages. This method involves downloading the webpage content and extracting the desired information.
    - **Pros**: Can potentially retrieve more data than allowed by APIs.
    - **Cons**: Fragile (can break if the website structure changes), might violate terms of service, and can be resource-intensive.

3. **Third-party Data Providers**:
    - There are services and platforms that collate and provide social media data for research or business purposes. These platforms often have arrangements with social media networks or employ large-scale scraping to collect data.
    - **Pros**: Ready-to-use datasets, often extensive and comprehensive.
    - **Cons**: Can be expensive, might not be up-to-date, and depends on third-party terms and conditions.

## News Information:
1. **News APIs**:
    - Various news agencies and aggregators offer APIs that allow users to fetch the latest news, headlines, and articles. Examples include the NewsAPI, Event Registry, or the GDELT Project.
    - **Pros**: Structured data, real-time or near real-time access, includes metadata.
    - **Cons**: May be rate-limited, requires API keys, might have costs associated.

2. **Web Scraping**(applies to general websites as well): 
    - As with social media, news websites can be scraped using tools like Scrapy, Beautiful Soup, or Puppeteer. Additionally, RSS feeds can be an excellent source for news articles and updates.
    - **Pros**: Customizable, can retrieve news from sources that don't offer APIs.
    - **Cons**: Might violate terms of service, can be fragile and resource-intensive, potential ethical considerations.

3. **Pre-curated Datasets**:
    - There are repositories and datasets available online that consist of news articles and metadata. Examples include the _Kaggle_ platform or academic datasets.
    - **Pros**: Ready-to-use, extensive datasets, often labeled or categorized.
    - **Cons**: Might not be current, data might not cover recent events, depends on third-party terms and conditions.

Practice ethics, legality, and terms of service. Always encourage students to respect these considerations and obtain permissions where required.
- - - -
## Twitter Scraping Example
Certainly! Let's start by demonstrating how to fetch tweets using the Tweepy library and Twitter's official API.

#### Prerequisites:
1. Install tweepy:
```
pip install tweepy
```

2. Obtain API credentials from the Twitter Developer platform:
   - Create an application at [Twitter Developer Console](https://developer.twitter.com/).
   - Once the application is created, you'll get:
     - API Key
     - API Secret Key
     - Access Token
     - Access Token Secret

#### Example Code:

```python
import tweepy

# Twitter API Credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Tweepy
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

# Fetch recent tweets from a specific user
user_name = 'twitter_handle'  # e.g., 'elonmusk'
tweets = api.user_timeline(screen_name=user_name, count=10)  # Fetches the 10 most recent tweets

for tweet in tweets:
    print(tweet.text)  # Print the content of each tweet

# If you want to search tweets based on a keyword:
query = 'machine learning'
for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(10):  # Fetches 10 tweets with the keyword
    print(tweet.text)
```

- - - -
## Reddit Scraping Example
Certainly! Reddit's official API is another excellent resource for gathering data. The Python library `PRAW` (Python Reddit API Wrapper) provides a friendly interface to interact with Reddit's API.

#### Prerequisites:
1. Install PRAW:
```
pip install praw
```

2. Set up a Reddit App:
   - Log in to your Reddit account and navigate to: [Reddit App Preferences](https://www.reddit.com/prefs/apps)
   - Click "Create App" or "Create Another App".
   - Fill out the required fields: name, App type (choose script for personal use), description (can be left blank), permissions, etc.
   - After creating the app, you will have:
     - `client_id` (right below the app name)
     - `client_secret`

#### Example Code:

```python
import praw

# Reddit App Credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
USER_AGENT = 'YOUR_APP_NAME by /u/YOUR_REDDIT_USERNAME'

# Authenticate with PRAW
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Fetch top 10 posts from a specific subreddit
subreddit_name = 'MachineLearning'
subreddit = reddit.subreddit(subreddit_name)

for post in subreddit.top(limit=10):
    print(post.title)  # Print the title of each post
    print(post.url)    # Print the URL of each post

# Search for posts containing a specific keyword across all of Reddit
query = 'artificial intelligence'
for post in reddit.subreddit('all').search(query, limit=10):
    print(post.title)
    print(post.url)
```

Note Reddit's API has rate limits. `PRAW` respects these limits and will wait accordingly before making more requests if you hit them.
- - - -
## News (NYT) Scraping Example
Many major news platforms provide their APIs to allow developers to access and distribute their content. Below are some well-known news services that offer APIs:

1. **The New York Times (NYT)**: The NYT provides several APIs that give access to different types of news data, from articles to movie reviews.
   
2. **BBC**: While the BBC doesn't have a public API for all of its news content, they do offer an RSS feed which can be parsed and used similarly to an API for many purposes.

3. **Currents API**: Offers the latest news published in various blogs, news websites, magazines, and newspapers.

4. **Event Registry**: Collects news articles from numerous sources globally and offers an API to search and analyze them.

5. **Guardian**: The Guardian offers an open platform that allows access to their articles, images, podcasts, and videos.

6. **Bing News Search**: Part of Microsoft's Cognitive Services, Bing News Search provides an API to search the web for news articles.

Let's proceed with an example for **The New York Times (NYT)**, one of the most reputable news sources with a comprehensive API:

## The New York Times API:

#### Prerequisites:
1. Register on [The New York Times Developer Portal](https://developer.nytimes.com/).
2. Create a new App to access the "Article Search API".
3. Get your API key for the App.

#### Example Code:

```python
import requests

# NYT API Key
API_KEY = 'YOUR_NYT_API_KEY'

# Base URL for Article Search API
BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# Parameters for the request
params = {
    'q': 'technology',  # Search term
    'api-key': API_KEY,
    'page': 0  # Fetch the first page of results
}

response = requests.get(BASE_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    docs = response.json().get('response').get('docs')
    for doc in docs:
        print(doc['headline']['main'])  # Print the headline of the article
        print(doc['web_url'])           # Print the URL of the article
else:
    print(f"Error {response.status_code}: Unable to fetch data from The New York Times API")
```

Always ensure you're following the terms of use for each API. Most news platforms impose limits on the number of requests, the volume of data retrieved, and how that data can be displayed or redistributed.
- - - -
## RSS Feed Scraping Example
RSS (Really Simple Syndication) feeds are a great way to fetch news updates from websites without having to resort to web scraping. They provide data in a structured XML format, which can be easily parsed to extract relevant information.

Here's a simple example using Python to fetch and parse an RSS feed. We'll use the `feedparser` library, which simplifies the process.

#### Prerequisites:
1. Install the required library:
```
pip install feedparser
```

#### Example Code:

```python
import feedparser

# URL of the RSS feed
RSS_FEED_URL = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'  # For instance, The New York Times homepage feed

# Parse the RSS feed
feed = feedparser.parse(RSS_FEED_URL)

# Loop through each entry/item in the feed
for entry in feed.entries:
    print(entry.title)       # Print the title of the article
    print(entry.link)        # Print the URL/link of the article
    print(entry.description) # Print the description or summary of the article
    print('---------------------')

# If you're interested in the feed metadata (like feed title, feed link, etc.):
print(feed.feed.title)       # Print the title of the feed (e.g., "NYT > Top Stories")
print(feed.feed.link)        # Print the link of the feed
```

You can easily adapt the above code to work with other news websites or blogs by changing the `RSS_FEED_URL` to point to the desired RSS feed. Keep in mind that while RSS feeds provide a structured way to access content, they might not contain the full content of the articles or all the details you might find on the actual website. They usually contain titles, summaries, and links to the full articles.
