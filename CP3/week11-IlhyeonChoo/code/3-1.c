#include <stdio.h>
#include <stdlib.h>

typedef int (*BinOp)(int, int);

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int compute(int a, int b, BinOp op) {
  // if (op == NULL) {
  //   printf("Null pointer\n-1\n");
  //   exit(0);
  // }
  // return op(a, b);
  if (op) {
    return op(a, b);
  } else {
    printf("Null pointer\n-1\n");
    exit(0);
  }
}

int main() {
  int a = 10, b = 5;

  printf("%d\n", compute(a, b, add));
  printf("%d\n", compute(a, b, sub));
  printf("%d\n", compute(a, b, mul));
  printf("%d\n", compute(a, b, NULL));

  return 0;
}
