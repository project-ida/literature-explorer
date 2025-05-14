"""
This script parses a locally saved HTML bibliography file to identify and download all untrimmed PDF links 
(i.e., links that do not include a '#page=X' fragment). It is intended to capture full-length documents that 
are not targeted for trimming to a specific article.

Key features:
- Reads a local HTML file (e.g., 'bibliography.html') from the same folder as the script.
- Identifies all .pdf links that do not contain '#page=' fragments.
- Deduplicates and limits the number of files downloaded (via MAX_FILES).
- Downloads and saves the PDFs unmodified to a local directory ('untrimmed_pdfs').

Requirements:
- BeautifulSoup4
- requests

Usage:
- Save the bibliography HTML file as 'bibliography.html' in the script directory.
- Run the script to download all full-length PDFs not marked with page numbers.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Configuration
base_page = "bibliography.html"  # Local file
download_dir = "untrimmed_pdfs"
MAX_FILES = 10000

os.makedirs(download_dir, exist_ok=True)

# Step 1: Load and parse the local HTML page
with open(base_page, "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")

# Step 2: Extract all PDF links (with or without #page=)
all_links = soup.find_all("a", href=True)
pdf_links = [a['href'] for a in all_links if a['href'].lower().endswith(".pdf") or ".pdf#" in a['href'].lower()]

# Step 3: Filter to keep only those without '#page='
untrimmed_links = [link for link in pdf_links if "#page=" not in link]
untrimmed_links = list(dict.fromkeys(untrimmed_links))  # deduplicate while preserving order
untrimmed_links = untrimmed_links[:MAX_FILES]

print(f"Found {len(untrimmed_links)} untrimmed PDF links.")

# Step 4: Download each PDF unmodified
for url in untrimmed_links:
    print("========================")
    print(f"Downloading untrimmed: {url}")

    filename = url.split("/")[-1]
    local_path = os.path.join(download_dir, filename)

    try:
        pdf_data = requests.get(url).content
        with open(local_path, "wb") as f:
            f.write(pdf_data)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
