# task1_data_collection.py
import requests  # type: ignore
import time

# Base URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header 
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Store categorized data
categorized_stories = {
    "technology": [],
    "worldnews": [],
    "sports": [],
    "science": [],
    "entertainment": []
}

# Step 1: Fetch top story IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]  # first 500
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []

# Step 2: Fetch each story and categorize
for category, keywords in categories.items():
    print(f"Processing category: {category}")

    for story_id in story_ids:
        try:
            res = requests.get(ITEM_URL.format(story_id), headers=headers)
            story = res.json()

            if story is None or "title" not in story:
                continue

            title = story["title"].lower()

            # Check if any keyword matches
            if any(keyword in title for keyword in keywords):
                categorized_stories[category].append({
                    "id": story_id,
                    "title": story["title"],
                    "url": story.get("url", "")
                })

        except Exception as e:
            print(f"Failed to fetch story {story_id}: {e}")
            continue

    # Sleep AFTER finishing each category
    time.sleep(2)

# Print summary
print("\nSummary:")
for category, stories in categorized_stories.items():
    print(f"{category}: {len(stories)} stories")