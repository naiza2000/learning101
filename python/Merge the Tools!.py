import textwrap
def merge_the_tools(string, k):
    word = textwrap.wrap(string,width=k)
    l=[]
    n=len(word)
    for i in range(n):
        s=word[i]
        a=''
        a=s[0]
        for j in range(1,k):
            flag=1
            for t in range(j):
                if(s[j]==s[t]):
                    flag=0
                    break
            if(flag==1):
                a+=s[j]
        l.append(a)
    for z in range(n):
        print(l[z])    
 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)       
