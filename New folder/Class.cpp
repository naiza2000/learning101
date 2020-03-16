#include <iostream>
#include <sstream>
#include<string>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student {
    private:
        int a;
        string b;
        string c;
        int d;
        string e;
    public:
        void set_age(int age) {
            a = age;
        }
        void set_standard(int standard) {
            d = standard;
        }
        void set_first_name(string first_name) {
            b = first_name;
        }
        void set_last_name(string last_name) {
            c=last_name;
        }        

        int get_age() {
            return a;
        }
        string get_first_name() {
            return b;
        }
        string get_last_name() {
            return c;
        }
        int get_standard() {
            return d;
        }
        string to_string(){
            string e;
            e=std::to_string(a)+','+b+','+c+','+std::to_string(d);
            return e;
        }
};
int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}