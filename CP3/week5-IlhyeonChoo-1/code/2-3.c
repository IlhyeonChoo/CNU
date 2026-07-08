#include <stdio.h>

int main() {
  int a = 10, b = 70, c = 30, d = 40;
  int* arr[] = {&a, &b, &c, &d};
  int** pp = arr;

  int** base = arr;

  printf("%ld\n", (char*)pp - (char*)base);

  pp = pp + 1;
  printf("%ld\n", (char*)pp - (char*)base);

  pp = pp + 1;
  printf("%ld\n", (char*)pp - (char*)base);

  pp = pp + 1;
  printf("%ld\n", (char*)pp - (char*)base);

  return 0;
}
