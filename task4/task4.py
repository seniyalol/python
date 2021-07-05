

import re
import sys


def compare(str1, str2):
    str2 = re.escape(str2).replace('\\*', '.*')
    if re.search('^{}$'.format(str2), str1):
        return 'OK'
    return 'KO'
    
    

    
def main():
    if len(sys.argv) != 3:
        print("Usage:\npython3 task4.py str1, str2")
        exit(1)
    str1, str2 = sys.argv[1:3]
    print(compare(str1, str2))
main()
