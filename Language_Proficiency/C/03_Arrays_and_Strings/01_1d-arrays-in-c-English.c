#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    // Get number
    int n = 0;
    scanf("%d", &n);       
    // Create array of size n
    int *arr = (int*)malloc(n * sizeof(int));
    // Fill array while summing
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    // Deallocate array
    free(arr);

    // Print sum
    printf("%i\n", sum);
    
    return 0;
}
