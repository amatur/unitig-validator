import sys
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1 # use start += 1 to find overlapping matches
# print(list(find_all('ATATAT', 'ATAT')))
where=sys.argv[1]
pattern=sys.argv[2]

f=open(where,"r")
lines=f.readlines()
line=lines[0].rstrip()
print(list(find_all(line, pattern)))
