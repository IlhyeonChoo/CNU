#include <stdio.h>

int main() {
  int a, b, c;

  a = b = c = 5;
  printf("%d %d %d\n", a, b, c);

  a = 2 + 3 * 4;
  printf("%d %d %d\n", a, b, c);

  c = a++ + ++b;
  printf("%d %d %d\n", a, b, c);

  return 0;
}
