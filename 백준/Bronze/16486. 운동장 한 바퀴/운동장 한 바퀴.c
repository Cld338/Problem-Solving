#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>

int main(void) {
    int length, radius;
    double pi = 3.14159265358979;

    scanf("%d\n%d", &length, &radius);
    double perimeter = (2.0 * length ) + 2.0 * pi * radius;

    printf("%f\n", perimeter);

    return 0;
}
