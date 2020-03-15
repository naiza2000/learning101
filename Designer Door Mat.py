a, b = map(int, input().split())
s =".|."
for i in range(1,(a+1)//2):
    print('-'*((b-3*(2*(i-1)+1))//2),end='')
    print(s*(2*(i-1)+1),end='')
    print('-'*((b-3*(2*(i-1)+1))//2))         
print('-'*((b-7)//2),end='')
print("WELCOME",end='')
print('-'*((b-7)//2))
for i in range(1,(a+1)//2):
    print('-'*((b-3*a+6*i)//2),end='')
    print(s*(a-2*i),end='')
    print('-'*((b-3*a+6*i)//2))   
