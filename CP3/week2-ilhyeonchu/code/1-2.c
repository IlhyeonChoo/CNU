#include <stdio.h>

typedef struct {
  char* name;
  int id;
  float value;
} Person;

int main() {
  Person p1 = {"kim", 12, 4.12};
  Person p2 = {"lee", 1922, 3.21};
  Person p3 = {"park", 432, 1};

  printf("%10s %10s %10s\n", "name", "id", "value");
  printf("%10s %010d %10.2f\n", p1.name, p1.id, p1.value);
  printf("%10s %010d %10.2f\n", p2.name, p2.id, p2.value);
  printf("%10s %010d %10.2f\n", p3.name, p3.id, p3.value);
  return 0;
}
