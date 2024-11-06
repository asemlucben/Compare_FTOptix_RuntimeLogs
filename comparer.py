import re
from datetime import datetime

LOG_FILE = "./RuntimeLogs/featuresdemo2.single.txt"
HORIZONTAL_LINE = "|--------------------------------|------------------------------------------|------------|------------|------------|"

with open(LOG_FILE, 'r') as file:
    log_entries = []
    page_name = ""
    old_page_name = ""
    # Print table header
    print(HORIZONTAL_LINE)
    print(f"| Page Name                      | Module Name                              | Total      |  Number    |  Items per |")
    print(f"|                                |                                          | load time  |  of items  |  second    |")
    # Loop in the file content
    for line in file:
        try:
            # Check the name of the page we are observing
            if "Add UI node completed" in line:
                page_name_match = re.search(r'Add UI node completed (.*)', line)
                if page_name_match:
                    page_name = page_name_match.group(1)
            # Get the values from the debug log
            match = re.search(r'(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}\.\d{3}) DEBUG \(urn:FTOptix:NativeUI\): Start (.*?);(\d+);(\d+);(\d+\.\d+)', line)
            if page_name != old_page_name:
                print(HORIZONTAL_LINE)
                table_content = f"| {page_name.ljust(30)} |"
                old_page_name = page_name
            # Print the new line if we match benchmark output
            if match:
                timestamp = datetime.strptime(match.group(1), '%d-%m-%Y %H:%M:%S.%f')
                module_name = match.group(2)
                benchmark1 = float(match.group(3))
                benchmark2 = float(match.group(4))
                benchmark3 = float(match.group(5))
                log_entries.append((timestamp, module_name, benchmark1, benchmark2, benchmark3))
                # Print the values
                print(f"{table_content} {module_name.ljust(40)} | {benchmark1:10.2f} | {benchmark2:10.2f} | {benchmark3:10.2f} |")
                table_content = f"|                                |"
        except ValueError as e:
            pass
    print(HORIZONTAL_LINE)