#include <stdio.h>

int my_strcmp(const char *a, const char *b) {
  // int a_len = 0;
  // int b_len = 0;
  // char tmp = a[0];
  //
  // while (tmp != '\0') {
  //   a_len++;
  //   tmp = a[a_len];
  // }
  // tmp = b[0];
  // while (tmp != '\0') {
  //   b_len++;
  //   tmp = b[b_len];
  // }
  int i = 0;
  int cmp = *(a + i) - *(b + i);
  while (!cmp) {
    i++;
    cmp = *(a + i) - *(b + i);
    if (*(a + i) == '\0' || *(b + i) == '\0')
      break;
  }
  return *(a + i) - *(b + i);
}

int main(int argc, char *argv[]) {
  printf("%d\n", my_strcmp("abc", "abcd"));
  printf("%d\n", my_strcmp("abc", "abc"));
  printf("%d\n", my_strcmp("b", "a"));
  return 0;
}
