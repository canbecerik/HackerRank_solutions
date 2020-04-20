#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k);
void max_calc(int *max, const int *temp, const int *k);

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}

void calculate_the_maximum(int n, int k)
{
    /* Initialize variables */
    int a = 0;
    int b = 0;
    int and_max = 0;
    int or_max = 0;
    int xor_max = 0;

    /* Main loop to scan */
    for (int a = 1; a < n; a++)
    {
        for (int b = a + 1; b <= n; b++)
        {
            /* Find results for each operation and check if satisfies conditions */
            int and_temp = a & b;
            max_calc(&and_max, &and_temp, &k);            
            int or_temp = a | b;
            max_calc(&or_max, &or_temp, &k);            
            int xor_temp = a ^ b;
            max_calc(&xor_max, &xor_temp, &k);            
        }
    }
    /* Print results */
    printf("%i\n%i\n%i\n", and_max, or_max, xor_max);
}
/* Function to check if the conditions are satisfied*/
void max_calc(int *max, const int *temp, const int *k)
{
    if (*temp > *max)
    {
        if (*temp < *k)
        {
            *max = *temp;
        }
    }
}
