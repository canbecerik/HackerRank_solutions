#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define LENGTH 1000
#define NODIGITS 10

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    // Get input
    char input[LENGTH + 1];
    // Replace \n with '\0'
    if (fgets(input, LENGTH, stdin))
    {
        input[strcspn(input, "\n")] = 0;
    }
    // String for digits
    char digits[NODIGITS] = "0123456789";
    // Compute input length
    int inputLength = strlen(input);
    // For each digit
    for (int j = 0; j < NODIGITS; j++)
    {
        int count = 0;
        for (int i = 0; i < inputLength; i++)
        {
            if (input[i] == digits[j])
            count++;
        }
        printf("%i ", count);
    }

    return 0;
}
