#include <stdio.h>

int main() {
  int a, b, result;
  char op;

  scanf("%d %d %c", &a, &b, &op);

  if (op == '+') {
    result = a + b;
  } else if (op == '-') {
    result = a - b;
  } else if (op == '*') {
    result = a * b;
  } else if (op == '/') {
    result = a / b;
  } else {
    printf("error");
  }

  printf("%d\n", result);

  return 0;
}
