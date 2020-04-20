#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int x, y;
    scanf("%d\n%d", &x, &y);
    
    // create char array to hold values

    char numbers[11][6] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "even", "odd"};
    int index;
    for (int i = x; i <= y; i++) 
    {
        index = i <= 9 ? i - 1 : 9 + i % 2;
        printf("%s\n", numbers[index]);
    }

    return 0;
}
