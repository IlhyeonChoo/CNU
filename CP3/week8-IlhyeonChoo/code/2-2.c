#include <stdio.h>

void foo() {
  char *str1 = "hello";
  printf("%p\n", (void *)str1);
}

void bar() {
  char *str2 = "hello";
  printf("%p\n", (void *)str2);
}

int main() {
  foo();
  bar();

  return 0;
}
