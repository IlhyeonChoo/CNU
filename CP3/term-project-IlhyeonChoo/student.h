#ifndef STUDENT_H
#define STUDENT_H

#define STUDENT_NAME_SIZE 32

typedef struct Student {
  int id;
  char name[STUDENT_NAME_SIZE];
  int score;
  struct Student *next;
} Student;

int save(const char *path, const Student *head);

void reload();

int add(Student **head, Student **tail, int id, const char *name, int score);

int del(Student **head, Student **tail, int id);

int update(Student *head, int id, int score);

void find(int id);

void list(const Student *head);

void stats();

void clear(void);

void exit_csv(Student *head);

void sort();

#endif // STUDENT_H
