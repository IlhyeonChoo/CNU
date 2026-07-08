#include <stdio.h>

int main() {
  char* alphas[] = {"abc", "def", "hij"};

  int size = sizeof(alphas) / sizeof(alphas[0]);

  for (int i = 0; i < size; i++) {
    printf("%s\n", alphas[i]);
  }

  return 0;
}
