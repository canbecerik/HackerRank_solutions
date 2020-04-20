#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Prototype
void draw(const int i, const int n, int shape[][n]);

int main() 
{
    int n;
    scanf("%d", &n);
    // Create free 2D int [2n-1][2n-1] array
    int shape[(2 * n) - 1][(2 * n) - 1];
    int i = n;
    // Call a recursive function with i, n, shape as inputs
    draw(i, n, shape);    
    // print the array
    for (i = 0; i < (2 * n) - 1; i++)
    {
        if (i > 0 && (i != (2 * n) - 1))
        {
            printf("\n");
        }
        for (int j = 0; j < (2 * n) - 1; j++)
        {
            printf("%i", shape[i][j]);
            if (j != (2 * n) - 2)
            {
                printf(" ");
            }
        }
    }
    return 0;
}

// Function to draw one square inside array
void draw(int i, const int n, int shape[][(2 * n) - 1])
{
    // Final condition for i = 1
    if (i == 1)
    {
        shape[n - 1][n - 1] = 1;
    }

    else
    {
        for (int j = (n - i); j < (2 * n) - 1 - (n - i); j++)
        {
            // Left edge
            shape[j][n - i] = i;
            // Top edge
            shape[n - i][j] = i;
            // Bottom Edge
            shape[(2 * n) - 2 - (n - i)][j] = i;
            // Right Edge
            shape[j][(2 * n) - 2 - (n - i)] = i;
        }
        i--;
        draw(i, n, shape);
    }
}