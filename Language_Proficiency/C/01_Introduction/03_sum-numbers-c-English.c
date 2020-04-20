#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int x, y;
    float a, b;
    scanf("%i %i", &x, &y);
    scanf("%f %f", &a, &b);
    printf("%i %i\n%.1f %.1f\n", (x + y), (x - y), (a + b), (a - b));    
    return 0;
}