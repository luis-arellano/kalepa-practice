import json
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent / 'data/submissions.json'
output_path = Path(__file__).parent / 'output/summary.json'



def data_cleaning(data: list[dict])-> dict:
    cleaned_data = []
    for submission in data:

        new = submission.copy()

        new['business_name']= submission['business_name'].strip()
        new['coverage_type'] = submission['coverage_type'].title()
        new['state'] = submission['state'].upper()
        new['broker_email'] = submission['broker_email'].lower()
        new['annual_revenue'] = str(submission['annual_revenue']).replace("$", "").replace(",","")
        if new['employee_count']:
            new['employee_count'] = int(str(submission['employee_count']))
        else:
            new['employee_count'] = None

        cleaned_data.append(new)
    return cleaned_data


# Open the Data
with open (file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1 Data Cleaning
cleaned_data = data_cleaning(data)

# Saved data
with open( output_path, 'w', encoding='utf-8') as file:
     json.dump(cleaned_data, file, indent=4)