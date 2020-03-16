if __name__ == '__main__':
    arr1=[]
    n =int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        arr1.append([score,name])
    arr1.sort()
    for x in range(n):
        if (arr1[0][0]!=arr1[x][0]):
            break
    for t in range(x,n):
        if(arr1[x][0]==arr1[t][0]):
            print(arr1[t][1])