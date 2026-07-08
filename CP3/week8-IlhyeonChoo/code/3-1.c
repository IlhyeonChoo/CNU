#include <stdio.h>
#include <string.h>

int main(void) {
  char *names[] = {"apple", "mango", "ant", "banana", "cat", "anaconda"};
  int n = sizeof(names) / sizeof(names[0]);

  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (strcmp(names[j], names[j + 1]) > 0) {
        char *tmp = names[j + 1];
        names[j + 1] = names[j];
        names[j] = tmp;
        // for (int i = 0; i < n; i++) {
        //   printf("%s ", names[i]);
        // }
        // printf("\n");
      }
    }
  }

  for (int i = 0; i < n; i++) {
    printf("%s\n", names[i]);
  }

  return 0;
}
