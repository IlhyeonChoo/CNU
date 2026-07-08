#include <stdio.h>

int main() {
  unsigned int x = 0x12345678;

  unsigned char* addr = (unsigned char*)&x;

  printf("%x\n", *addr);
  printf("%x\n", *(addr + 1));
  printf("%x\n", *(addr + 2));
  printf("%x\n", *(addr + 3));

  return 0;
}
