#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
//using namespace std;


int main() {
    // read n
    int n;
    std::cin >> n;
    // get array input
    int array_input[n];
    for (int i=0;i<n;i++)
    {
        std::cin>>array_input[i];        
    }
    // print array in reverse
    for (int i=n-1; i>=0; i--)
    {
        std::cout << array_input[i];
        // add space if not at last element (array_input[0])
        if (i!=0)
        {
            std::cout << " ";
        }
    }

    return 0;
}
