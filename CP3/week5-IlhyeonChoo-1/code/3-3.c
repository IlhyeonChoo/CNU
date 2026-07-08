#include <stdio.h>

int main() {
  int val = 7;
  int other = 77;

  const int* const p = &val;
  //*p = 10;
  // p = &other;

  printf("%d\n", *p);
  return 0;
}
