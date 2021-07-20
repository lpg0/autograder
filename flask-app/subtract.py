import sys

n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))

print(n1-n2)

try:
    sys.stdout.close()
except:
    pass
try:
    sys.stderr.close()
except:
    pass
