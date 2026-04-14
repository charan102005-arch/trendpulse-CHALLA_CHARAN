# task2_data_extraction_cleaning.py

from datetime import datetime

# -----------------------------
# Category keywords
# -----------------------------
CATEGORY_KEYWORDS = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# -----------------------------
# Helper: assign category
# -----------------------------
def get_category(title):
    title_lower = title.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    return None


# -----------------------------
# INPUT: your raw data from Task 1
# (must be a list of story dicts)
# Example: data = json.load(...)
# -----------------------------
# Replace this with your actual loaded JSON
data = []


# -----------------------------
# Step: Extract + Clean
# -----------------------------
cleaned_data = []

category_counts = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

for story in data:

    # Stop when all categories reach 25
    if all(count >= 25 for count in category_counts.values()):
        break

    # -------- Cleaning --------
    if not story:
        continue

    title = story.get("title")
    if not title or title.strip() == "":
        continue  # skip invalid titles

    # -------- Categorisation --------
    category = get_category(title)
    if not category:
        continue

    if category_counts[category] >= 25:
        continue

    # -------- Extract + Clean Fields --------
    post_id = story.get("id")

    score = story.get("score")
    if score is None:
        score = 0

    num_comments = story.get("descendants")
    if num_comments is None:
        num_comments = 0

    author = story.get("by")
    if not author:
        author = "unknown"

    collected_at = datetime.now().isoformat()

    # -------- Store cleaned record --------
    cleaned_story = {
        "post_id": post_id,
        "title": title.strip(),
        "category": category,
        "score": score,
        "num_comments": num_comments,
        "author": author,
        "collected_at": collected_at
    }

    cleaned_data.append(cleaned_story)
    category_counts[category] += 1


# -----------------------------
# Output check
# -----------------------------
print("Total cleaned stories:", len(cleaned_data))
print("Category counts:", category_counts)