#include <iostream>
using namespace std;
int main()
{
    string fullname = "Iqra Mulla";
    char grade = 'A';
    int value = grade;
    float PI = 3.14f;
    bool isRegistered = true;
    double price = 120.98;
    int newPrice = (int)price;
    int a = 12, b = 8;
    int sum = a + b;
    cout << (3 > 5) << endl;
    cout << "differernce" << " = " << (a - b) << endl;
    cout << "division" << " = " << (a / b) << endl;
    cout << "product" << " = " << (a * b) << endl;
    cout << "modulo" << " = " << (a % b) << endl;
    cout << sum << endl;
    cout << newPrice << endl;
    cout << value << endl;
    cout << PI << endl;
    cout << isRegistered << endl;
    cout << grade << endl;
    cout << fullname << endl;
    cout << price << endl;
    int age;
    cout << "Enter your age: ";
    cin >> age;
    cout << "Your age is: " << age << endl;

    return 0;
}