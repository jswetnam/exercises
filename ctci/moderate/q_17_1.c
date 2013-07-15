#include "stdio.h"

void swap(int* a, int* b) {
    *a = *b - *a;
    *b = *b - *a;
    *a = *b + *a;
}

int main() {
    int a = 3;
    int b = 5;
    printf("Before swap: a: %d, b: %d\n", a, b);
    swap(&a, &b);
    printf("After swap: a: %d, b: %d\n", a, b);
    return 0;
}
