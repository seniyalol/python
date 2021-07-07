import re
import sys

def itoBase(nb, base):
    sym = "0123456789abcdefghijklmnopqrstuvwxyz"
    res = ""
    while nb > 0:
        nb, m = divmod(nb, base)
        res += sym[m]
    return res[::-1]
def main():
    if len(sys.argv) != 3:
        print("Usage:\npython3 task1.py nb, base ")
        exit(1)
    nb, base  = sys.argv[1:3]
    print(itoBase(int(nb), int(base) ))
main()  



