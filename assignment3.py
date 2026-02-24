"""Note: The URL was not working so I had to test a local file version of the script. I chose to 
break up the RegEx in imageSearch and browserSearch because I was having trouble comprehending 
everything in one line, as the full regular expression was a bit overwhelming to do all at once.
Since the instructions mentioned that we have freedom to choose how we want to do this, I chose not
to use main() or if __name__ == "__main__" because during my research, I discovered that these are mainly
used for lengthy scripts that will be imported elsewhere, which is not the case for this script.

Additional Note: This script is ran by terminal (so type python assignment3.py to execute)"""

import urllib.request
import csv 
import re
# other imports go here

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

def processData(csv_string):
    rows = csv_string.splitlines()
    organizer = csv.reader(rows)
    kept_rows = [row for row in organizer if row]
    return kept_rows

def imageSearch(rows):
    file_types = ['jpg', 'png', 'gif']
    joined_types = "|".join(file_types)
    period = r"\."
    group = "(" + joined_types + ")"
    end_character = r"$"
    regex_string = period + group + end_character
    file_type_regex = re.compile(regex_string, re.IGNORECASE)
    all_files = len(rows)
    stored_matching_files = [row for row in rows if file_type_regex.search(row[0])]
    percent = (len(stored_matching_files) / all_files) * 100
    print(f"Files ending in .jpg, .png, and .gif make up {percent:.1f}% of total files.")
    return stored_matching_files

def browserSearch(rows):
    browsers = ['Chrome', 'Firefox', 'Safari', 'MSIE']
    pattern = re.compile("|".join(browsers), re.IGNORECASE)    
    total_browsers = len(rows)
    matched_browsers = rows.copy()
    count_of_each_browser = {browser_name: 0 for browser_name in browsers}
    for row in rows:
        browser = pattern.search(row[2]).group(0)
        count_of_each_browser[browser] += 1
    most_popular = max(count_of_each_browser, key=count_of_each_browser.get)
    percent = (count_of_each_browser[most_popular] / total_browsers) * 100
    print(f"The most popular browser is {most_popular}, making up {percent:.1f}% of all logged browsers.")    
    return matched_browsers


url = "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"
csv_text = downloadData(url)
processed_data = processData(csv_text)
stored_file_types = imageSearch(processed_data)
most_popular_browser = browserSearch(processed_data)

    
