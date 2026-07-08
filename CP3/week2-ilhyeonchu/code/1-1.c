#include <stdio.h>

int main() {
  int var1 = 100;
  printf("int : %d\n", var1);
  printf("hex : %x\n", var1);
  printf("oct : %o\n", var1);

  char var2 = 'c';
  printf("char : %c\n", var2);

  char* var3 = "hello world!";
  printf("string : %s\n", var3);

  float var4 = 3.141592;
  printf("float : %f\n", var4);
  printf("exp : %e\n", var4);

  return 0;
}
