#include <stdio.h>

int main() {
  int x = 10;
  int y = 20;

  printf("%d\n", x);

  int* ptr = &x;

  *ptr = y;

  printf("%d\n", x);

  return 0;
}
