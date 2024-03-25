import argparse
import json

def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_fields(data, fields):
    extracted_data = []
    for entry in data:
        extracted_entry = {field: entry.get(field) for field in fields}
        extracted_data.append(extracted_entry)
    return extracted_data

def print_formatted_output(extracted_data, field_names):
    for entry in extracted_data:
        for field_name in field_names:
            print(f"{field_name}: {entry[field_name]}")
        print("----------------------------------")

def main():
    parser = argparse.ArgumentParser(description="Parse JSON file and extract specified fields")
    parser.add_argument("-f", "--file", type=str, help="Path to the JSON file", required=True)
    parser.add_argument("-e", "--extract", nargs='+', type=str, help="Fields to extract", required=True)
    args = parser.parse_args()

    file_path = args.file
    field_names = args.extract

    data = parse_json(file_path)
    extracted_data = extract_fields(data, field_names)

    print_formatted_output(extracted_data, field_names)

if __name__ == "__main__":
    main()
