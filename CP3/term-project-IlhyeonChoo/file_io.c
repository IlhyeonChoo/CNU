#include "file_io.h"
#include "student.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CSV_LINE_SIZE 256

static void strip_newline(char *text) { text[strcspn(text, "\r\n")] = '\0'; }

int open_csv(const char *path, Student **head, Student **tail) {
  if (path == NULL || head == NULL || tail == NULL) {
    return -1;
  }

  FILE *file = fopen(path, "r");
  if (file == NULL) {
    file = fopen(path, "w");
    if (file == NULL) {
      return -1;
    }

    fprintf(file, "id,name,score\n");
    fclose(file);
    *head = NULL;
    *tail = NULL;
    return 0;
  }

  char line[CSV_LINE_SIZE];
  if (fgets(line, sizeof(line), file) == NULL) {
    fclose(file);
    return 0;
  }

  Student *loaded = NULL;
  Student *loaded_tail = NULL;
  int student_count = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    strip_newline(line);
    if (line[0] == '\0') {
      continue;
    }

    char *id_text = strtok(line, ",");
    char *name = strtok(NULL, ",");
    char *score_text = strtok(NULL, ",");

    if (id_text != NULL && name != NULL && score_text != NULL) {
      int id = atoi(id_text);
      int score = atoi(score_text);
      if (add(&loaded, &loaded_tail, id, name, score) == 0) {
        student_count++;
      }
    }
  }

  fclose(file);

  *head = loaded;
  *tail = loaded_tail;
  return student_count;
}
