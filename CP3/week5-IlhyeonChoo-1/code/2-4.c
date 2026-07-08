#include <stdio.h>

long my_strtol(char* str, char** endptr) {
  long res = 0;

  while (*str >= 48 && *str <= 57) {
    res *= 10;
    res += *str - 48;

    str++;
  }

  if (endptr != NULL) {
    *endptr = (char*)str;
  }

  return res;
}

int main() {
  char str[] = "2026hello";
  char* end;

  long val = my_strtol(str, &end);

  printf("%ld %s\n", val, end);
  return 0;
}
