#include <stdio.h>

void update(int *a,int *b) {
    int sum = *a + *b;
    int absDif = (*a - *b < 0 ? *b - *a : *a - *b);
    *a = sum;
    *b = absDif;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}