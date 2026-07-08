#include <stdio.h>

int main() {
  int a[5] = {1, 2, 3, 4, 5};

  for (int i = 0; i < 5; i++) {
    printf("%d ", a[i]);
  }
  printf("\n");

  int b[5] = {1, 2};

  for (int i = 0; i < 5; i++) {
    printf("%d ", b[i]);
  }
  printf("\n");

  int c[5] = {0};

  for (int i = 0; i < 5; i++) {
    printf("%d ", c[i]);
  }
  printf("\n");

  int d[] = {10, 20, 30};

  for (int i = 0; i < (sizeof(d) / sizeof(int)); i++) {
    printf("%d ", d[i]);
  }
  printf("\n");

  return 0;
}
