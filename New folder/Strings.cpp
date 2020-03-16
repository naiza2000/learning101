#include <iostream>
#include <string>
using namespace std;

int main() {
    string str1;
    string str2;
	getline(cin,str1);
    getline(cin,str2);
    int len1 =str1.size();
    int len2=str2.size();
    cout<<len1<<' '<<len2<<'\n';
    string a=str1+str2;
    cout<<a<<endl;
    char ch;
    ch= a[len1];
    a[len1]=a[0];
    a[0]=ch;
    for(int i=0;i<len1;i++){
        printf("%c",a[i]);
    
    }
    cout<<' ';
    for(int j=len1;j<(len1+len2);j++){
        cout<<a[j];
    }
    return 0;
}
