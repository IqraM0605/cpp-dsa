#include <iostream>
using namespace std;

int main()
{
    int n = 20;

    cout << "Even Numbers: ";
    for (int i = 1; i <= n; i++)
    {
        if (i % 2 == 0)
        {
            cout << i << " ";
        }
    }

    cout << endl;

    cout << "Odd Numbers: ";
    for (int i = 1; i <= n; i++)
    {
        if (i % 2 != 0)
        {
            cout << i << " ";
        }
    }

    return 0;
}