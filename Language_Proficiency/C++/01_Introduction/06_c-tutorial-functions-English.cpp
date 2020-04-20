#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    // collect inputs into an array
    int inputs[4] = {a, b, c, d};
    // init max value variable
    int max=0;
    // iterate and compare each array value with max
    for (int i=0; i<4; i++)
    {
        max= max < inputs[i] ? inputs[i] : max;
    }
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
