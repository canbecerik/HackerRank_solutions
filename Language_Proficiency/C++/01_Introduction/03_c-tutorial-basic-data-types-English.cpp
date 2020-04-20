#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int input_int=0;
    long input_long=0;
    char input_char;
    float input_float=0;
    double input_double=0;

    scanf("%d %ld %c %f %lf", &input_int, &input_long, &input_char, &input_float, &input_double);
    printf("%d\n%ld\n%c\n%f\n%lf\n", input_int, input_long, input_char, input_float, input_double);


    return 0;
}
