#include "stdio.h"

int Sum(int A[], int i, int j){
  int sum = A[i];
  for (int k = i + 1; k <= j; k++) {
    sum += A[k];
  }
  return sum;
}

int LargestContigSum(int A[], int len_a) {
  int max_sum = A[0];
  for (int i = 1; i <= len_a; i++) {
    for (int j = 0; j <= len_a - i; ++j) {
      int sum = Sum(A, j, j + i - 1);
      if (sum > max_sum) {
        max_sum = sum;
      }
    }
  }
  return max_sum;
}

int main(int argc, const char *argv[])
{
  int A[] = {2, -8, 3, -2, 4, -10};
  int a_len = sizeof(A) / sizeof(int);

  printf("Max Sum: %d \n", LargestContigSum(A, a_len));

  return 0;
}
