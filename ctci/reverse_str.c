// Implement a function reverse(char str) in C or C++ which reverses
// a null-terminated string.

#include "string.h"
#include "stdio.h"

void reverse(char* str) {
  char tmp;
  int str_len = strlen(str);
  for(int i = 0; i < str_len / 2; ++i) {
    tmp = str[i];
    str[i] = str[str_len - i - 1];
    str[str_len - i - 1] = tmp;
  }
}

int main() {
  char str[] = "abcde";
  printf("String: %s\n", str);
  reverse(str);
  printf("Reversed: %s\n", str);
}
