import os, sys, csv, re
from modules import occurance_module
from datastructures import ordered_key_value_list

debug = False

def main(file):
    frequency_object = occurance_module.occurance(file)
    # frequency_object = occurance(file)
    sorted_object = sort_dictionary(frequency_object)

    sorted_object.display_list()

    # sorted_object.to_csv_file()
    if file == "merged.csv":
        os.remove("./merged.csv")


# This is only in this run.py file because of errors with pythonista which are not allowing me
# to have a list inside of a dictionary while this tool is modualized, so I have to keep it
# within a single file now
def occurance(file_name):
    with open(str(file_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        ip_addresses = {}
        count = 0
        pattern = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]", flags=0)
        for row in csv_reader:
            if count == 0:
                ip_addresses[row[2]] = [row[0]]
                if debug:
                    # ip_addresses['Data Errors'] = []
                    ip_addresses["Data Errors"] = 0
            elif pattern.match(row[2]):
                if row[2] not in ip_addresses:
                    # ip_addresses[row[2]] = [row[0]]
                    ip_addresses[row[2]] = 1
                    continue
                else:
                    ip_addresses[row[2]] += 1
                    # if row[0] not in ip_addresses[row[2]]:
                    # ip_addresses[row[2]].append(row[0])
                    # continue
            else:
                if debug:
                    ip_addresses["Data Errors"] += 1
                    # ip_addresses['Data Errors'].append('1')
            count += 1

    return ip_addresses


def sort_dictionary(dictionary):
    ordered_data = ordered_key_value_list.OrderedDictionary()
    count = 0
    for key in dictionary:
        if count != 0:
            ordered_data.ordered_insert(key, int(dictionary[key]))
        count += 1
    return ordered_data


if __name__ == "__main__":
    main("test_file.csv")
    # main(sys.argv[1])
