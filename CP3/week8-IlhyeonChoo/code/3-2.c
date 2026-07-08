#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  for (int i = 1; i < argc; i++) {
    for (int j = 1; j < argc - i; j++) {
      if (strcmp(argv[j], argv[j + 1]) > 0) {
        char *tmp = argv[j + 1];
        argv[j + 1] = argv[j];
        argv[j] = tmp;
      }
    }
  }

  for (int i = 1; i < argc; i++) {
    printf("%s\n", argv[i]);
  }
  return 0;
}
