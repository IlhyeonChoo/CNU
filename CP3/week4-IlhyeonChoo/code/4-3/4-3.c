#include <stdio.h>

int main() {
  int arr[] = {3, 7, 1, 9, 4, 6};
  int n = sizeof(arr) / sizeof(arr[0]);

  for (int i = 0; i < (n - 1); i++) {
    void* addr_0 = &(arr[i]);
    void* addr_1 = &(arr[i + 1]);

    printf("address of arr[%d]: %p\n", i, addr_0);
    printf("address of arr[%d+1]: %p\n", i, addr_1);

    printf("&(arr[%d]) - &(arr[%d+1]) = %d\n", i, i + 1,
           (unsigned long long)addr_1 - (unsigned long long)addr_0);
    printf("\n");
  }
  return 0;
}
