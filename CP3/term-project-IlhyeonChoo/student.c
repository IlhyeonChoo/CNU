#include "student.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int save(const char *path, const Student *head) {
  if (path == NULL) {
    return -1;
  }

  FILE *file = fopen(path, "w");
  if (file == NULL) {
    return -1;
  }

  int student_count = 0;
  fprintf(file, "id,name,score\n");

  const Student *current = head;
  while (current != NULL) {
    fprintf(file, "%d,%s,%d\n", current->id, current->name, current->score);
    student_count++;
    current = current->next;
  }

  fclose(file);
  return student_count;
}

int add(Student **head, Student **tail, int id, const char *name, int score) {
  if (head == NULL || tail == NULL || name == NULL) {
    return -1;
  }
  if (id <= 0 || score < 0 || score > 100) {
    return -1;
  }

  Student *current = *head;
  while (current != NULL) {
    if (current->id == id) {
      return -1;
    }
    current = current->next;
  }

  Student *student = malloc(sizeof(*student));
  if (student == NULL) {
    return -1;
  }

  student->id = id;
  strncpy(student->name, name, STUDENT_NAME_SIZE - 1);
  student->name[STUDENT_NAME_SIZE - 1] = '\0';
  student->score = score;
  student->next = NULL;

  if (*head == NULL) {
    *head = student;
  } else {
    (*tail)->next = student;
  }

  *tail = student;
  return 0;
}

int del(Student **head, Student **tail, int id) {
  if (head == NULL || tail == NULL) {
    return -1;
  }

  Student *previous = NULL;
  Student *current = *head;

  while (current != NULL) {
    if (current->id == id) {
      if (previous == NULL) {
        *head = current->next;
      } else {
        previous->next = current->next;
      }

      if (*tail == current) {
        *tail = previous;
      }

      free(current);
      return 0;
    }

    previous = current;
    current = current->next;
  }

  return -1;
}

int update(Student *head, int id, int score) {
  Student *current = head;

  while (current != NULL) {
    if (current->id == id) {
      current->score = score;
      return 0;
    }

    current = current->next;
  }

  return -1;
}

void list(const Student *head) {
  if (head == NULL) {
    printf("No students found\n");
    return;
  }

  printf("ID Name Score\n");

  const Student *current = head;
  while (current != NULL) {
    printf("%d %s %d\n", current->id, current->name, current->score);
    current = current->next;
  }
}

void clear(void) { printf("\033[2J\033[H"); }

void exit_csv(Student *head) {
  while (head != NULL) {
    Student *next = head->next;
    free(head);
    head = next;
  }
}
