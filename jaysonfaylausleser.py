import json

import pandas as pd

filepath = r"C:\Users\Vural Zurnaci\Desktop\Dump of json\dump-dummy.JSON"
# Load the JSON data
with open(filepath, 'r') as f:
    data = json.load(f)

# Initialize a list to store filtered data for each entry
filtered_data_list = []

# Check if the loaded data is a list
if isinstance(data, list):
    # Iterate over each element in the list
    for entry in data:
        # Initialize variables to store filtered data for this entry
        filtered_data = {}

        # Filter the required fields for this entry
        filtered_data['href'] = None
        if 'link' in entry and isinstance(entry['link'], list):
            for link in entry['link']:
                if isinstance(link, dict) and link.get('@ref') == 'scopus':
                    filtered_data['href'] = link.get('@href', '')
                    break

        filtered_data['title'] = entry.get('dc:title', '')
        filtered_data['creator'] = entry.get('dc:creator', '')
        filtered_data['cover_date'] = entry.get('prism:coverDate', '')
        filtered_data['display_date'] = entry.get('prism:coverDisplayDate', '')
        filtered_data['doi'] = entry.get('prism:doi', '')

        if 'affiliation' in entry and isinstance(entry['affiliation'], list) and entry['affiliation']:
            filtered_data['affilname'] = entry['affiliation'][0].get('affilname', '')
        else:
            filtered_data['affilname'] = ''

        filtered_data['aggregation_type'] = entry.get('prism:aggregationType', '')
        filtered_data['subtype_description'] = entry.get('subtypeDescription', '')

        # Append filtered data for this entry to the list
        filtered_data_list.append(filtered_data)

# Save the filtered data as JSON
output_path = r"C:\Users\Vural Zurnaci\Desktop\Dump of json\dump-dummy2.JSON" # Specify the output file path
with open(output_path, 'w') as outfile:
    json.dump(filtered_data_list, outfile, indent=4)

# Load the JSON data
with open(output_path, 'r') as f:
    data = json.load(f)

# Convert JSON to DataFrame
df = pd.json_normalize(data)

# Specify the path for the output CSV file
output_file_path = r'C:\Users\Vural Zurnaci\Desktop\Dump of json\filtered_data.csv'

# Save DataFrame to CSV
df.to_csv(output_file_path, index=False)


# Print the filtered data list
for index, filtered_data in enumerate(filtered_data_list, start=1):
    print(f"Entry {index}: {filtered_data}")