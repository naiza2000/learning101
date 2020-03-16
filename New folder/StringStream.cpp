#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
   vector<int> integers;
   int i=0;
     int count=0;
    char ch='a';
    do{ ch=str[i];
    i++;
        if(ch==',')
        count++;

    }while(ch!='\0');
    stringstream ss(str);
    for(int j=0;j<count;j++){
        int a;
        char ch;
        ss>>a>>ch;
         integers.push_back(a);
}
      int a;
      ss>>a;
      integers.push_back(a);
    
         return integers;
}

int main() {
    string str;
    cin >> str;
    
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
