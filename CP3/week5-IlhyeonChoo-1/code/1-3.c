#include <stdio.h>

void print_reverse(int* arr, int size) {
  for (int i = 1; i <= size; i++) {
    printf("%d ", *(arr + size - i));
  }
}

int main() {
  int nums[] = {1, 2, 3, 4, 5};

  print_reverse(nums, 5);
  printf("\n");

  return 0;
}
