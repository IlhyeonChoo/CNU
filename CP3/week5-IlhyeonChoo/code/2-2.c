#include <stdio.h>
#include <string.h>

void sort_strings(char** arr, int size) {
  char* temp;
  for (int i = 0; i < size - 1; i++) {
    for (int j = 0; j < size - 1 - i; j++) {
      if (strcmp(*(arr + i), *(arr + i + j)) > 0) {
        temp = *(arr + j);
        *(arr + j) = *(arr + i);
        *(arr + i) = temp;
      }
    }
  }
}

int main() {
  char* words[] = {"apple", "ant", "banana", "cherry"};
  int size = 4;

  sort_strings(words, size);

  for (int i = 0; i < size; i++) {
    printf("%s\n", words[i]);
  }

  return 0;
}
