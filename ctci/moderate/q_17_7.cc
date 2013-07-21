#include <vector>

#include <math.h>
#include <stdint.h>
#include <stdio.h>

using std::vector;
// Add vector of digits in 32-bit unsigned num:
//
// Input: 1,236
// Output: {0, 0, 0, 0, 0 , 0, 1, 2, 3, 6} ( 10 - element digit array)
// 4,000,000,000
//
void GetDigits(const unsigned int& num, vector<int>* digits) {
  unsigned int num_cpy = num;

  for (uint8_t pow_10 = 1;  pow_10 <= 10 ; ++pow_10 ) {
    digits->insert(digits->begin(),
        (num_cpy % static_cast<int>(pow(10, pow_10))) /
                   static_cast<int>(pow(10, pow_10 - 1)));
    num_cpy = num_cpy - (num_cpy % static_cast<int>(pow(10, pow_10)));
  }
}

int main(int argc, const char *argv[]) {
  unsigned int num = 12364;
  vector<int> digits;
  GetDigits(num, &digits);

  for (int i = 0; i < digits.size(); ++i) {
    printf("%d, ", digits[i]);
  }

  printf("\n");

  return 0;
}


