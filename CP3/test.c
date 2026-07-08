#include <stdio.h>

void increment(int *a) {
  ++(*a);
  printf("dksl%d\n", *a);
}

void print_value6(int (*arr)[4]) {
  printf("%d\n", arr[0][0]);
  printf("%d\n", *arr[0]);
  printf("%d\n", *(*(arr) + 2));
  printf("%d\n", *(*(arr + 2)));
}

void print_value7(int *p, int rows, int cols) {}

int main() {
  int arr[5] = {0, 1, 2, 3};
  int *p = arr;
  printf("%d\n", arr[0]);
  printf("%d\n", *p);
  printf("%d\n", p[0]);
  printf("%d\n", *arr);
  p++;
  printf("%d\n", *p);
  // arr++;

  int arr2[3][4] = {{1, 2, 3}, {2, 3, 4, 5}, {}};

  print_value6(arr2);

  int a = 1000;
  increment(&a);
  printf("%d\n", a);

  int arr5[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

  int (*k)[4] = arr5;
  printf("%d\n", *(k + 2)[1]);
  printf("%d\n", (*k++)[1]);
  foo();
}
