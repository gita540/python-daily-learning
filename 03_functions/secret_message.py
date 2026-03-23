# ============================================================
# SECRET MESSAGE DECODER - Google Doc Grid Parser
# ============================================================
# This program fetches a Google Doc, reads a table of (x, y, character)
# coordinates, and reconstructs a hidden message on a 2D grid.
#
# PREREQUISITES:
#   pip install requests beautifulsoup4
#
# HOW TO RUN:
#   1. Replace the URL at the bottom with your Google Doc /pub URL
#   2. Run: python secret_message.py
# ============================================================

import requests
from bs4 import BeautifulSoup


def decode_secret_message(url: str):
    """
    Fetches a Google Doc and decodes a hidden message from a coordinate table.

    The Google Doc must contain a table with 3 columns:
        Column 1: x-coordinate (integer)
        Column 2: character (single character)
        Column 3: y-coordinate (integer)

    Args:
        url (str): The publicly published Google Doc URL (/pub format)
    """

    # ----------------------------------------------------------
    # STEP 1: Fetch the Google Doc HTML
    # ----------------------------------------------------------
    # requests.get() sends an HTTP GET request to the URL
    # response.text gives us the raw HTML of the page
    print(f"Fetching document from: {url}\n")
    response = requests.get(url)

    # Check if the request was successful (HTTP status 200 = OK)
    if response.status_code != 200:
        print(f"ERROR: Failed to fetch document. HTTP Status: {response.status_code}")
        return

    # Parse the HTML using BeautifulSoup
    # 'html.parser' is Python's built-in HTML parser (no extra install needed)
    soup = BeautifulSoup(response.text, 'html.parser')

    # ----------------------------------------------------------
    # STEP 2: Initialize the grid storage
    # ----------------------------------------------------------
    # We use a dictionary where key = (x, y) tuple, value = character
    # Example: grid[(0, 0)] = 'A', grid[(1, 0)] = 'B', etc.
    grid = {}

    # Track the maximum x and y values so we know the grid dimensions
    max_x = 0
    max_y = 0

    # ----------------------------------------------------------
    # STEP 3: Find all table rows and extract coordinates
    # ----------------------------------------------------------
    # soup.find_all('tr') finds every table row (<tr> tag) in the HTML
    rows = soup.find_all('tr')

    print(f"Total rows found in document: {len(rows)}")

    for row in rows:
        # Find all table data cells (<td> tags) within this row
        cells = row.find_all('td')

        # We only care about rows with exactly 3 columns: x | char | y
        if len(cells) == 3:
            try:
                # Extract and clean text from each cell
                # .get_text() gets the visible text inside the HTML tag
                # .strip() removes leading/trailing whitespace and newlines
                x    = int(cells[0].get_text().strip())   # Column 1: x-coordinate
                char = cells[1].get_text().strip()         # Column 2: character
                y    = int(cells[2].get_text().strip())    # Column 3: y-coordinate

                # Store the character at position (x, y) in our grid dictionary
                grid[(x, y)] = char

                # Update max boundaries so we know how big to draw the grid
                max_x = max(max_x, x)
                max_y = max(max_y, y)

            except ValueError:
                # int() throws ValueError if the cell contains non-numeric text
                # This handles the header row (e.g., "x-coordinate", "char", "y-coordinate")
                continue

    print(f"Characters parsed: {len(grid)}")
    print(f"Grid size: {max_x + 1} wide x {max_y + 1} tall\n")

    # Guard: if no data was found, exit early
    if not grid:
        print("ERROR: No coordinate data found. Check your URL or table format.")
        return

    # ----------------------------------------------------------
    # STEP 4: Reconstruct and print the 2D grid
    # ----------------------------------------------------------
    # We iterate y from 0 → max_y (top to bottom)
    # For each row, we iterate x from 0 → max_x (left to right)
    # If no character exists at (x, y), we use a space ' ' as a blank

    print("=" * 40)
    print("DECODED MESSAGE:")
    print("=" * 40)

    for y in range(max_y + 1):         # Loop over each row (top → bottom)
        row_string = ''
        for x in range(max_x + 1):     # Loop over each column (left → right)
            # dict.get(key, default) returns the character or ' ' if not found
            row_string += grid.get((x, y), ' ')
        print(row_string)              # Print the completed row

    print("=" * 40)


# ============================================================
# ENTRY POINT
# ============================================================
# This block only runs when you execute this file directly.
# It will NOT run if this file is imported as a module.

if __name__ == "__main__":

    # --------------------------------------------------------
    # REPLACE THIS URL with your actual Google Doc /pub link
    #
    # How to get the correct URL:
    #   1. Open your Google Doc
    #   2. File → Share → Publish to web
    #   3. Click "Publish" and copy the link
    #   It should look like:
    #   https://docs.google.com/document/d/<DOC_ID>/pub
    # --------------------------------------------------------

    url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

    decode_secret_message(url)