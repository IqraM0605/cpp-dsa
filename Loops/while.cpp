#include <iostream>
using namespace std;
int main()
{
    int n = 20;
    int i = 1;
    int sum = 0;

    while (i <= n)
    {
        if (i % 3 == 0)
        {
            sum += i;
        }

        i++;
    }
    cout << "sum:" << sum << endl;
    return 0;
}