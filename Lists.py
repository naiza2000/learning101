if __name__ == '__main__':
    N = int(input())
    a = []
    for _ in range(N):
        name, *line = input().split()
        num = list(map(int, line))
        if(name=="insert"):
            a.insert(num[0],num[1])
        if(name=="print"):
            print(a)
        if(name=="remove"):
            a.remove(num[0])
        if(name=="append"):
            a.append(num[0])
        if(name=="sort"):
            a.sort()
        if(name=="pop"):
            a.pop()
        if(name=="reverse"):
            a.reverse()          