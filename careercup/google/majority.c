#include <stdlib.h>
#include <stdio.h>

int compare (const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}

int FindMajority(int A[], int array_size) {
  qsort(A, array_size, sizeof(int), compare);
  int majority_start = 0;
  int majority_end = 0;
  int i = 0;
  int j = 0;

  while (j < array_size) {
    ++j;
    if (A[i] != A[j]) {
      if (j - i > majority_end - majority_start) {
        majority_start = i;
        majority_end = j;
      }
     i = j;
    }
  }
  if (majority_end - majority_start > array_size / 2) {
    return A[majority_start];
  } else {
    return -1;
  }
}

int main(int argc, const char *argv[])
{
  int A[] = {1, 1, 2, 3, 4, 1 , 5, 1, 7, 1, 1};
  printf("Majority of A is %d \n", FindMajority(A, sizeof(A) / sizeof(int)));
  return 0;
}

