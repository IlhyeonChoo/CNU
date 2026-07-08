#include <stdio.h>

int main() {
  printf("char: %ld\n", sizeof(char));
  printf("short: %ld\n", sizeof(short));
  printf("int: %ld\n", sizeof(int));
  printf("unsigned int: %ld\n", sizeof(unsigned int));
  printf("long: %ld\n", sizeof(long));
  printf("long long: %ld\n", sizeof(long long));
  printf("float: %ld\n", sizeof(float));

  return 0;
}
