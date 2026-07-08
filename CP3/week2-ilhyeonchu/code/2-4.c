#include <stdio.h>

int main() {
  float a = 0.1 + 0.2;
  float b = 0.3;

  printf("a = %.100f\n", a);
  printf("b = %.100f\n", b);
  printf("a == b is %d\n", a == b);

  double c = 0.1 + 0.2;
  double d = 0.3;

  printf("c = %.100f\n", c);
  printf("d = %.100f\n", d);
  printf("c == d is %d\n", c == d);

  return 0;
}
