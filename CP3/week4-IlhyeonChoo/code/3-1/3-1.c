#include <stdio.h>

int main() {
  int n = 10;

  int* p = &n;

  printf("address of n: %p\n", p);

  printf("*p = %d\n", *p);

  *p = 99;
  printf("n = %d\n", n);
  return 0;
}
