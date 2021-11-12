import csv 
import json 

JSON_ENTRIES_THRESHOLD = 5000 # modify to whatever you see suitable

def write_json(json_array, filename):
    with open(filename, 'w', encoding='utf-8') as jsonf: 
        json.dump(json_array, jsonf)  # note the usage of .dump directly to a file descriptor

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        filename_index = 0
    
        for row in csvReader:
            jsonArray.append(row)
            if len(jsonArray) >= JSON_ENTRIES_THRESHOLD:
                # if we reached the treshold, write out
                write_json(jsonArray, f"jsonFilePath-{filename_index}.json")
                filename_index += 1
                jsonArray = []
            
        # Finally, write out the remainder
        write_json(jsonArray, f"jsonFilePath-{filename_index}.json")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_to_json('company3_translated-2.csv','./company4')

