// CTCI 5.1

#include "stdio.h"
#include "stdint.h"

void SetBit(uint8_t bit, uint32_t* N) {
  *N = *N | (1<<bit);
}

void ClearBit(uint8_t bit, uint32_t* N) {
  *N = *N & ~(1<<bit);
}

// Overwrites bits i through j with the bits of M.
// j - i must be equal to the number of bits in M and
// should not overflow the bounds of N.
void OverwriteBits(uint32_t* N, uint32_t M, uint8_t i, uint8_t j) {
  for (uint8_t k = 0; k < (j + 1 - i); ++k) {
    if (M & 1<<k) {
      SetBit(i + k, N);
    } else {
      ClearBit(i + k, N);
    }
  }
}

int main() {
  uint32_t N = 1 << 10 ; // 10000000000
  uint32_t M = 19; // 10011 1 * 2^4 + 1 * 2^1 + 1 * 2^0

  printf("N:%d M:%d \n", N, M);
  OverwriteBits(&N, M, 2, 6);
  printf("N:%d M:%d \n", N, M);
  return 0;
}
