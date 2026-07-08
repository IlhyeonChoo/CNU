#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp_str(const void *a, const void *b) {
  const char *const *str_a = a;
  const char *const *str_b = b;

  return strcmp(*str_a, *str_b);
}

int main(void) {
  const char *words[] = {"banana", "apple", "ant", "orange"};
  int size = 4;

  qsort(words, size, sizeof(const char *), cmp_str);

  for (int i = 0; i < size; ++i) {
    printf("%s\n", words[i]);
  }
  return 0;
}
