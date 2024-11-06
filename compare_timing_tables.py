import re
from datetime import datetime

FIRST_FILE = "./single.txt"
SECOND_FILE = "./multi.txt"
HORIZONTAL_LINE = "|--------------------------------|------------------------------------------||------------|------------|------------||------------|------------|------------||------------|------------|------------||"

with open(FIRST_FILE, 'r', encoding='utf-16') as file:
    first_file_content = file.readlines()
with open(SECOND_FILE, 'r', encoding='utf-16') as file:
    second_file_content = file.readlines() 

print("|--------------------------------|------------------------------------------||--------------------------------------||--------------------------------------||--------------------------------------||")
print("|                                |                                          ||             First file               ||             Second file              ||        First to second ratio         ||")
print("|--------------------------------|------------------------------------------||--------------------------------------||--------------------------------------||--------------------------------------||")
print("| Page Name                      | Module Name                              || Total      |  Number    |  Items per || Total      |  Number    |  Items per || Load time  | items cnt  |   items/s  ||")
print("|                                |                                          || load time  |  of items  |  second    || load time  |  of items  |  second    || improvement| (always 1) | improvement||")

for i in range(len(first_file_content)):
    page_name = ""
    module_name = ""
    load_time = 0.0
    items_count = 0.0
    items_per_sec = 0.0
    if "---" not in first_file_content[i]:
        # Split the line to get unique values
        split_first_file_line = first_file_content[i].split("|")
        split_second_file_line = second_file_content[i].split("|")
        # Extract values
        try:
            # Get values from the first log file
            page_name = split_first_file_line[1].strip()
            module_name = split_first_file_line[2].strip()
            load_time = float(split_first_file_line[3].strip())
            items_count = float(split_first_file_line[4].strip())
            items_per_sec = float(split_first_file_line[5].strip())
            # Get values from the second log file
            second_page_name = split_second_file_line[1].strip()
            second_module_name = split_second_file_line[2].strip()
            second_load_time = float(split_second_file_line[3].strip())
            second_items_count = float(split_second_file_line[4].strip())
            second_items_per_sec = float(split_second_file_line[5].strip())
            # Get the ratio between the times
            if second_load_time == 0:
                load_time_ratio = 0
            else:
                load_time_ratio = load_time / second_load_time
            if second_items_count == 0:
                items_count_ratio = 0
            else:
                items_count_ratio = items_count / second_items_count
            if second_items_per_sec == 0:
                items_per_sec_ratio = 0
            else:
                items_per_sec_ratio = items_per_sec / second_items_per_sec
            # Print a separator per each page
            if page_name != "":
                print(HORIZONTAL_LINE)
            # Print the values
            print(f"| {page_name.ljust(30)} | {module_name.ljust(40)} || {load_time:10.2f} | {items_count:10} | {items_per_sec:10.2f} || {second_load_time:10.2f} | {second_items_count:10} | {second_items_per_sec:10.2f} || {load_time_ratio:10.2f} | {items_count_ratio:10.2f} | {items_per_sec_ratio:10.2f} ||")
        except ValueError as e:
            pass
print(HORIZONTAL_LINE)