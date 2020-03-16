#include <iostream>
#include <cstdio>
using namespace std;
int max_of_two(int a,int b){
    if(a>=b)
    return a;
    else return b;
}
int max_of_four(int a,int b,int c,int d){
    int e=max_of_two(a,b);
    int f=max_of_two(c,d);
    return max_of_two(e,f);
    
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}