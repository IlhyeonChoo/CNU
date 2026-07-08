#include <stdio.h>

void my_print(char type, void* x) {
  if (type == 'C') {
    printf("%c\n", *(char*)x);
  } else if (type == 'D') {
    printf("%d\n", *(int*)x);
  } else if (type == 'S') {
    printf("%s\n", (char*)x);
  } else {
    return;
  }
}

int main() {
  int a = 0x61;
  char b = 'b';
  char* c = "hello world";

  my_print('C', &a);
  my_print('D', &b);
  my_print('S', c);
  my_print('C', c);

  return 0;
}
