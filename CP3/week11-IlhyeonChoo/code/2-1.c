#include <stdio.h>

enum State { IDLE, RUNNING, PAUSED, DONE };

void print_state(enum State s) {
  switch (s) {
  case IDLE:
    printf("State: IDLE\n");
    break;
  case RUNNING:
    printf("State: RUNNING\n");
    break;
  default:
    printf("Unknown state\n");
  }
}

int main() {
  print_state(RUNNING);
  return 0;
}
