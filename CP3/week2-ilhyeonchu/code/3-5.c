#include <stdio.h>

int main() {
  int a = 32;
  int b = 156;
  // 00100000
  // 10011100
  a = a ^ b;
  b = a ^ b;
  a = a ^ b;

  printf("%d %d\n", a, b);
  return 0;
}
