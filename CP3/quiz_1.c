#include <stdio.h>
#include <stdlib.h>

void quiz_3() {
  int a = 2;
  int b = 3;
  int result = a++ * b + 1;

  printf("%d\n", result);
}
void foo(void);

// void quiz_4() {
//   int a = 2;
//   int b = 3;
//   int result = ++(++a + b) * 2;
//   printf("%d\n", result);
// }

void quiz_5() {
  static int x = 0;
  printf("%d ", x++);
}

void quiz_8() {
  int a = 10;
  int *p = &a;
  *p = *p + 5;
  printf("%d\n", a);
}

// void foo(int *p, int cols) { printf("%d\n", *(p + 2 + cols)); }

int main(int argc, char *argv[]) {
  int a = 10;
  double b = 9.99;
  printf("%3d %.1f\n", a, b);

  unsigned char c = 255;
  printf("%d\n", c + 1);

  quiz_3();
  // quiz_4();
  quiz_5();
  quiz_5();
  quiz_5();
  quiz_5();
  quiz_8();

  printf("%d\n", sizeof(int) == sizeof(char));
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};

  // foo(&arr[0][0], 3);
  foo();

  return 0;
}
