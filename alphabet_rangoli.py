import string 

def print_rangoli(size):
    # your code goes here
    alphabetList = string.ascii_lowercase
    l = []
    for i in range(size):
        s = '-'.join(alphabetList[i:size])
        l.append((s[-1:0:-1]+s[:]).center(size*4-3,'-'))
    print('\n'.join(l[-1:0:-1]+l))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)