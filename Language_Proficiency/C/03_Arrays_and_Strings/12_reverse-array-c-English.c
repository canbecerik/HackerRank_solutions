#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
   
    /* Write the logic to reverse the array. */
    // Create another array of same size to hold reverse array
    int *arrCopy;
    arrCopy = (int*) malloc(num * sizeof(int));
    
    // Write reverse array from arr
    for(i = 0; i < num; i++)
    {
        arrCopy[num - i - 1] = arr[i];
    }
    
    // Use another pointer to hold arr address    
    int *arrTemp = arr;
    // Point arr to reverse array
    arr = arrCopy;
    // Free arrTemp -> free original array
    free(arrTemp);

    for(i = 0; i < num; i++)
    {
        printf("%d ", *(arr + i));
    }

    // Free arr -> free arrCopy
    free(arr);
    return 0;
}
