"""
This script extracts, downloads, and trims PDF files based on page-specific links in a locally saved HTML bibliography file.

Key features:
- Parses a local HTML file (e.g., 'bibliography.html') containing links to PDFs with page anchors (e.g., #page=154).
- Optionally filters links using a whitelist (if specified).
- Downloads each PDF only once, even if referenced multiple times.
- Trims each downloaded PDF to include only the relevant pages, from the start page (#page=X) to the page before the next article in the same file, or to the end if it's the last one.
- Saves the trimmed PDFs to a local folder ('trimmed_pdfs') using filenames like <original>_pageX.pdf.

Requirements:
- BeautifulSoup4
- requests
- PyPDF2

Usage:
- Place 'bibliography.html' in the same folder as this script.
- (Optional) Add full link strings (including #page=X) to the `whitelist` to limit processing.
- Run the script to populate the 'trimmed_pdfs' folder with the processed PDFs.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# Configuration
base_page = "bibliography.html"
download_dir = "trimmed_pdfs"
MAX_FILES = 10000  # Limit number of PDFs for testing/debugging

os.makedirs(download_dir, exist_ok=True)

# Step 1: Download and parse the HTML page
with open(base_page, "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")

# Step 2: Find all links with #page=NUM
pattern = re.compile(r"(http[^\s\"']+\.pdf)#page=(\d+)")
matches = pattern.findall(html)

whitelist = []

# Optionally filter matches based on whitelist
# If whitelist is empty, keep all matches
if whitelist:
    matches = [(url, page) for (url, page) in matches if f"{url}#page={page}" in whitelist]

# Deduplicate while preserving original order
seen = set()
deduped_matches = []
for match in matches:
    if match not in seen:
        deduped_matches.append(match)
        seen.add(match)
matches = deduped_matches[:MAX_FILES]

print(f"Found {len(matches)} unique PDF links with page numbers.")

matches = matches[:MAX_FILES]

print(matches)

# Step 3: Process each PDF link
for url, page_str in matches:

    print("========================")
    print(f"Processing URL: {url}#page={page_str}")

    filename = url.split("/")[-1]
    stem = Path(filename).stem
    page_start = int(page_str)
    start_index = max(0, page_start - 1)

    # New filename with page number
    new_filename = f"{stem}_page{page_start}.pdf"
    local_path = os.path.join(download_dir, new_filename)

    # Download the PDF
    print(f"Downloading {filename}...")
    try:
        pdf_data = requests.get(url).content
        temp_path = os.path.join(download_dir, "temp_" + filename)
        with open(temp_path, "wb") as f:
            f.write(pdf_data)

        # Read PDF to determine number of pages
        reader = PdfReader(temp_path)
        writer = PdfWriter()
        n_pages = len(reader.pages)

        if start_index >= n_pages:
            print(f"??  {filename} only has {n_pages} pages. Skipping.")
            os.remove(temp_path)
            continue

        # Determine trimming boundaries
        higher_pages = [
            int(other_page)
            for other_url, other_page in matches
            if other_url == url and int(other_page) > page_start
        ]

        if higher_pages:
            num_below = min(higher_pages)
            print(f"Found page number of other article below: {num_below}")
            upper_limit = min(num_below - 1, n_pages)
        else:
            upper_limit = n_pages  # ✅ Safe now because n_pages is defined above

        # Trim the PDF
        for i in range(start_index, upper_limit):
            writer.add_page(reader.pages[i])

        with open(local_path, "wb") as f:
            writer.write(f)

        os.remove(temp_path)
        print(f"Saved trimmed PDF as {new_filename} (pages {start_index + 1} to {upper_limit}).")

    except Exception as e:
        print(f"? Failed to process {filename}: {e}")
