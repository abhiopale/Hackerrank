#Given an array of integers, find the sum of its elements.
def simpleArraySum(ar):
    sum=0
    for a in ar:
        sum+=a
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
