import os
import pandas as pd

# Set input and output file paths
input_path = "data/creator_ineffabilis.txt"
output_path = "data/creator_ineffabilis_clean.csv"

# Read the raw text file
with open(input_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Step 1: Split into paragraphs by double newlines
paragraphs = [p.strip() for p in raw_text.split("\n\n") if p.strip()]

# Step 2: Remove duplicates (preserve order)
seen = set()
unique_paragraphs = []
for para in paragraphs:
    if para not in seen:
        seen.add(para)
        unique_paragraphs.append(para)

# Step 3: Alternate Latin / English
data = []
for i in range(0, len(unique_paragraphs), 2):
    latin = unique_paragraphs[i]
    english = unique_paragraphs[i + 1] if i + 1 < len(unique_paragraphs) else ""

    data.append({
        "paragraph_number": len(data) + 1,
        "language": "Latin",
        "text": latin,
        "word_count": len(latin.split())
    })
    if english:
        data.append({
            "paragraph_number": len(data),
            "language": "English",
            "text": english,
            "word_count": len(english.split())
        })

# Step 4: Save to CSV
df = pd.DataFrame(data)
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ Transformed text saved to {output_path}")
