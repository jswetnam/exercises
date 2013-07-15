#include "stdio.h"
#include "math.h"

int fac(int a) {
    int result = a;
    for(int i = a - 1; i > 0; --i) {
        result = result * i;
    }
    return result;
}

int NumTrailingZeroes(int n) {
    int i = 0;
    while (n % (int) pow(10, i + 1) == 0) {
        i++;
    }
    return i;
}

int main() {
    printf("5! : %d \n", fac(5));
    printf("Num trailing zeroes in %d : %d\n", 10, NumTrailingZeroes(10));
    printf("Num trailing zeroes in 5! : %d\n", NumTrailingZeroes(fac(5)));
    printf("2000! : %d\n", fac(2000));
    printf("Num trailing zeroes in 2000! : %d\n", NumTrailingZeroes(fac(2000)));
    printf("Num trailing zeroes in 2000! : %d\n", NumTrailingZeroes(fac(2000)));
    return 0;
}
