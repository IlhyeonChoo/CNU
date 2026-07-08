#include <stdio.h>

int main() {
  char s1[] = "hi";
  char s2[] = "hi";
  char s3[] = {'h', 'i', '\0'};

  printf("%s\n", s1);
  printf("%s\n", s2);
  printf("%s\n", s3);

  return 0;
}
