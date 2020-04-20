#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    int sum = 0;
    for (; n > 0; n /= 10)
    {
        sum += n % 10;
    }
    printf("%i", sum);
    return 0;
}
