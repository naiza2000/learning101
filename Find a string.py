def count_substring(a,b):
    N = len(a)
    n = len(b)
    count = 0
    flag = 1
    for x in range(0,N-n+1):
        if(a[x]==b[0]):
            for y in range(0,n):
                flag=1
                if(a[x+y]!=b[y]):
                    flag=0
                    break
            if(flag==1):
                count = count + 1

    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

