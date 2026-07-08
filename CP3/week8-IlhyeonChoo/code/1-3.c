#include <stdio.h>
#include <string.h>

char *my_strcat(char *dst, const char *src) {
  char tmp;
  int dst_len = 0;
  int src_len = 0;
  tmp = dst[0];
  while (tmp != '\0') {
    dst_len++;
    tmp = dst[dst_len];
  }
  tmp = src[0];
  while (tmp != '\0') {
    src_len++;
    tmp = src[src_len];
  }

  for (int i = 0; i < src_len; i++) {
    dst[dst_len + i] = src[i];
  }
  // for (int i = 0; i < strlen(src); i++) {
  //   dst[strlen(dst) + i] = src[i];
  // }
}

int main(void) {
  char str1[20] = "Hello";
  char str2[] = "World";

  printf("%s\n", str1);
  my_strcat(str1, str2);
  printf("%s\n", str1);

  return 0;
}
