import os
import json
from datetime import datetime

# -----------------------------
# Create 'data/' folder if not exists
# -----------------------------
folder_name = "data"
os.makedirs(folder_name, exist_ok=True)

# -----------------------------
# Create filename with date
# -----------------------------
date_str = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(folder_name, f"trends_{date_str}.json")

# -----------------------------
# Save data to JSON file
# -----------------------------
collected_data = []  # Define collected_data or populate it with your actual data
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4)

# -----------------------------
# Print total count
# -----------------------------
print(f"✅ Saved to: {file_path}")
print(f"📊 Total stories collected: {len(collected_data)}")