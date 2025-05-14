# This script parses a locally saved HTML file containing numbered bibliographic entries.
# It removes abstracts, identifies and extracts each entry based on numeric prefixes (e.g. "1."),
# and parses key metadata including the entry ID, citation text, publication year, URL, and a derived filename.
# The results are saved to a CSV file ("lenr_entries5.csv") for further analysis or processing.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from urllib.parse import urlparse, parse_qs

# Step 1: Fetch the webpage
# Step 1: Load the local HTML file
with open("DetailOnly.html", "r", encoding="windows-1252") as f:
    html_content = f.read()
soup = BeautifulSoup(html_content, 'html.parser')

# Remove all abstract sections to avoid false positives for "1." etc.
for abstract in soup.find_all("p", class_="ABSTRACT"):
    abstract.decompose()

MAX_FILES = 10000  # Change this to limit how many entries are processed

# Step 2: Extract the raw text (now without abstracts)
text = soup.get_text()

# Step 3: Find all entry start positions
entry_starts = [m.start() for m in re.finditer(r'(?m)^(\d+)\.\s', text)]


# Step 4: Slice the text into individual entries
entries = []
for i in range(len(entry_starts)):
    start = entry_starts[i]
    end = entry_starts[i + 1] if i + 1 < len(entry_starts) else len(text)
    entries.append(text[start:end])

# Step 5: Parse each entry
parsed_entries = []
for entry in entries:
    try:
        entry = entry.strip()

        # Flatten line breaks to help regex
        entry_flat = ' '.join(entry.split())

        # Match ID and citation
        id_match = re.match(r'^(\d+)\.\s+(.*)', entry_flat)
        if not id_match:
            print(f"⚠️ Skipping malformed entry (regex fail):\n{entry_flat[:100]}")
            continue

        entry_id = id_match.group(1)
        citation = id_match.group(2).strip()

        # Extract year from citation
        year_match = re.search(r'\b(19[2-9]\d|20[0-1]\d|202[0-5])\b', citation)
        year = year_match.group(1) if year_match else ''

        # Extract the first URL, if any
        url_match = re.search(r'(https?://[^\s]+)', entry)
        url = url_match.group(1).strip() if url_match else ''

        # Compute filename
        filename = ''
        if url:
            parsed_url = urlparse(url)
            base = parsed_url.path.split('/')[-1]
            if '#page=' in url:
                page_number = parse_qs(parsed_url.fragment).get('page', [''])[0]
                if base.endswith('.pdf'):
                    name_only = base.rsplit('.pdf', 1)[0]
                    filename = f"{name_only}_page{page_number}.pdf"
                else:
                    filename = f"{base}_page{page_number}"
            else:
                filename = base

        parsed_entries.append([entry_id, citation, year, url, filename])
    except Exception as e:
        print(f"⚠️ Skipping entry due to error: {e}\n{entry[:100]}")
        continue


# Limit number of entries if needed
parsed_entries = parsed_entries[:MAX_FILES]

# Step 6: Create DataFrame and save
df = pd.DataFrame(parsed_entries, columns=['ID', 'Citation', 'Year', 'URL', 'Filename'])
df.to_csv("lenr_entries5.csv", index=False)
print("✅ CSV file saved as 'lenr_entries.csv'")
