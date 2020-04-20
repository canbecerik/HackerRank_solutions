#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int input[3];
    int sum=0;
    for (int i=0; i<3; i++)
    {
        std::cin >> input[i];
        sum+=input[i];
    }
    std::cout << sum << std::endl;
    return 0;
}
