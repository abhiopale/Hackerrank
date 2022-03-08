#The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n, printi**2 .and 1<=n<=20
if __name__ == '__main__':
    n = int(input())
    if (n>=1 and n<=20): 
        for i in range(n): print(i**2)