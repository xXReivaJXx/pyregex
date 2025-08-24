import argparse
import re
import os
import glob

##predefined regex patterns
predefined_patterns = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "ip": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "url": r"https?://[^\s]+",
    "date": r"\b\d{4}-\d{2}-\d{2}\b",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
}


# Argument Parser
parser = argparse.ArgumentParser(description="Run Script with multiple arguments")
parser.add_argument("-r","--regex", type=str, help="Custom Regex Pattern")
##parser.add_argument("-p", "--predefined", type=str, choices=predefined_patterns.keys(), help="Predefined Regex Pattern")
parser.add_argument("-f","--file", type=str, help="File to be searched")
parser.add_argument("-o","--output", type=str, help="save results", default="output.txt")
args = parser.parse_args()


#compile pattern
if args.regex:
    try:
        pattern_compiled = re.compile(args.regex)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        exit(1)
#else f args.predefined:
######  pattern = predefined_patterns[args.predefined]
##else:
##    print("No regex pattern provided. Use -r for custom pattern or -p for predefined patterns.")
##    exit(1) 

#Check for file
matched_files = glob.glob(args.file)
if not matched_files:
    print(f"File not found: {args.file}")
    exit(1)
    
#search and save results
with open(args.output, 'w') as output_file:
    for file_path in matched_files:
        print(f"Searching in : {file_path}")
        with open(file_path, "r") as file:
            for line in file:
                match = pattern_compiled.search(line)
                if match:
                    print(f"Mathc found: {match.group()}")
                    output_file.write(match.group() + "\n")
          


