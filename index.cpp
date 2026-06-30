#include <iostream>
using namespace std;

int main(){
    cout << "HEllo world" << endl;
    // string num = "shicam";
    string name = "shivam";
    string *add = &name;
    cout << add << endl;
    return 0;
}