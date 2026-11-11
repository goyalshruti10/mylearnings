import sys

def count_lines(file):
    with open(file) as f:
        return len(f.readlines())

def count_word(file,wordsearch):
    with open(file) as f:
         text = f.read()
         count = text.count(wordsearch)
         return count



fileinput = sys.argv[1]
num_line = count_lines(fileinput)
print(f"there are {num_line} lines in file {fileinput}")

######     py countlines.py tasks.txt

fileinput = sys.argv[1]
num_line = count_lines(fileinput)
wordinput = sys.argv[2]
count = count_word(fileinput,wordinput)
print(f"there are {num_line} lines in file {fileinput} and i appears {count} times")