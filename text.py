import syncedlyrics
import re
import json

# Input song name
query = input("Enter Song Name: ")

# Fetch lyrics using syncedlyrics
lrc = syncedlyrics.search(query)

# Check if lyrics were found
if not lrc:
    print("Lyrics not found.")
    exit()

# Split the data into lines
lines = lrc.split('\n')

# Initialize a list to store the JSON entries
json_data = []

# Define a regular expression pattern to extract timestamps and text
pattern = r'\[(\d+:\d+\.\d+)\] (.+)'

# Process each line
for line in lines:
    match = re.match(pattern, line)
    if match:
        timestamp, text = match.groups()
        json_entry = {
            "time": timestamp,
            "lyrics": text
        }
        json_data.append(json_entry)

# Check if we found any valid lyrics
if not json_data:
    print("No valid lyrics found.")
    exit()

# Convert the list of JSON entries to a JSON-formatted string
json_string = json.dumps(json_data, indent=4)

# Print the JSON string
print(json_string)


