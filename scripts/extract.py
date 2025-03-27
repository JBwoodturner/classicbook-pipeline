import requests
from bs4 import BeautifulSoup
import os

# Step 1: URL and file setup
URL = "https://www.preces-latinae.org/thesaurus/Varia/CreatorIneff.html"
OUTPUT_DIR = "data"
OUTPUT_FILE = "creator_ineffabilis.txt"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Step 2: Download the page
response = requests.get(URL)
response.raise_for_status()

# Step 3: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find the main content in <td> tags
# We'll filter out any short text or navigation
paragraphs = []
for td in soup.find_all("td"):
    text = td.get_text(separator="\n", strip=True)
    if "copyright" not in text.lower() and len(text.split()) > 10:
        paragraphs.append(text)

# Step 5: Combine and write to file
latin_text = "\n\n".join(paragraphs)
output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(latin_text)

print(f"✅ Extracted {len(paragraphs)} blocks and saved to {output_path}")
