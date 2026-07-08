#include <stdio.h>

int main() {
  int arr[5] = {10, 20, 30, 40, 50};
  int size = 5;
  int index;

  scanf("%d", &index);

  if (index > sizeof(arr) / sizeof(arr[0])) {
    printf("Error!\n");
    return 0;
  } else if (index < 0) {
    printf("Invalid Index\n");
  } else {
    printf("%d\n", arr[index]);
  }
}
