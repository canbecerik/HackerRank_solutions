#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    int test;
    for (test=1; test<11; test++)
    {
        int result = n*test;
        cout << n << " x " << test << " = " << result << endl;
    }

    return 0;
}
