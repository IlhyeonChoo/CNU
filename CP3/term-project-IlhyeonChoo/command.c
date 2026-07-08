#include "command.h"
#include "file_io.h"
#include "student.h"

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 전역 변수 사용
extern Student *g_tail;
extern const char *g_csv_path;

#ifdef ADMIN_MODE
Command commands[] = {
    {"save", handle_save, "save", "Save students to CSV"},
    {"reload", handle_reload, "reload", "Reload students from CSV"},
    {"add", handle_add, "add <id> <name> <score>", "Add a student"},
    {"delete", handle_delete, "delete <id>", "Delete a student"},
    {"update", handle_update, "update <id> <score>", "Update student score"},
    {"find", handle_find, "find <id>", "Find student"},
    {"list", handle_list, "list", "List students"},
    {"sort", handle_sort, "sort <name|score>",
     "Sort students bt name or score"},
    {"stats", handle_stats, "stats", "Show statistics"},
    {"help", handle_help, "help", "Show help"},
    {"clear", handle_clear, "clear", "Clear screen"},
    {"exit", handle_exit, "exit", "Exit shell"},
};
#endif // !ADMIN_MODE

#ifdef CLIENT_MODE
Command commands[] = {
    {"reload", handle_reload, "reload", "Reload students from CSV"},
    {"find", handle_find, "find <id>", "Find student"},
    {"list", handle_list, "list", "List students"},
    {"sort", handle_sort, "sort <name|score>",
     "Sort students bt name or score"},
    {"stats", handle_stats, "stats", "Show statistics"},
    {"help", handle_help, "help", "Show help"},
    {"clear", handle_clear, "clear", "Clear screen"},
    {"exit", handle_exit, "exit", "Exit shell"},
};
#endif // !CLIENT_MODE

size_t command_count = sizeof(commands) / sizeof(commands[0]);

// 왼쪽 공백 제거
static char *trim_left(char *text) {
  while (*text != '\0' && isspace((unsigned char)*text)) {
    text++;
  }
  return text;
}

// 오른쪽 공백 제거
static void trim_right(char *text) {
  size_t length = strlen(text);
  while (length > 0 && isspace((unsigned char)text[length - 1])) {
    text[length - 1] = '\0';
    length--;
  }
}

// 입력 id, 점수 값 검사
static int parse_int(const char *text, int *value) {
  char *end = NULL;
  long parsed = strtol(text, &end, 10);

  if (text == end || *end != '\0') {
    return -1;
  }

  *value = (int)parsed;
  return 0;
}

static int has_student_id(const Student *head, int id) {
  const Student *current = head;
  while (current != NULL) {
    if (current->id == id) {
      return 1;
    }
    current = current->next;
  }
  return 0;
}

// 입력 받은 명령어 실행
ShellResult execute_command(char *line, Student **head) {
  char *command_name = trim_left(line);
  trim_right(command_name);

  // 공백(ex 바로 엔터)
  if (command_name[0] == '\0') {
    return SHELL_OK;
  }

  // 명령어 범위 확인
  char *args = command_name;
  while (*args != '\0' && !isspace((unsigned char)*args)) {
    args++;
  }

  if (*args != '\0') {
    *args = '\0';
    args = trim_left(args + 1);
  }

  // 어떤 command인지 확인해서 실행
  for (size_t i = 0; i < command_count; i++) {
    if (strcmp(command_name, commands[i].name) == 0) {
      return commands[i].handler(args, head);
    }
  }

#ifdef ADMIN_MODE
  printf("admin> ");
#elif defined(CLIENT_MODE)
  printf("client> ");
#endif

  printf("Unknown command or permission denied.\n");
  return SHELL_OK;
}

ShellResult handle_save(char *args, Student **head) {
  (void)args;

  int student_count = save(g_csv_path, *head);
  if (student_count < 0) {
    printf("Error: failed to save CSV file\n");
    return SHELL_ERR_FILE_WRITE;
  }

  printf("Saved %d students to %s\n", student_count, g_csv_path);
  return SHELL_OK;
}

ShellResult handle_reload(char *args, Student **head) {
  if (args[0] != '\0') {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  Student *new_head = NULL;
  Student *new_tail = NULL;
  int student_count = open_csv(g_csv_path, &new_head, &new_tail);
  if (student_count < 0) {
    printf("Error: failed to reload CSV file\n");
    return SHELL_ERR_FILE_OPEN;
  }

  exit_csv(*head);
  *head = new_head;
  g_tail = new_tail;

  printf("Reloaded %d students from %s\n", student_count, g_csv_path);
  return SHELL_OK;
}

ShellResult handle_add(char *args, Student **head) {
  char *id_text = strtok(args, " \t");
  char *name = strtok(NULL, " \t");
  char *score_text = strtok(NULL, " \t");
  char *extra = strtok(NULL, " \t");
  int id = 0;
  int score = 0;

  if (id_text == NULL || name == NULL || score_text == NULL || extra != NULL) {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }
  if (parse_int(id_text, &id) != 0 || id <= 0) {
    printf("Error: invalid ID\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }
  if (has_student_id(*head, id)) {
    printf("Error: duplicate ID\n");
    return SHELL_ERRDUPLICATE_STUDENT;
  }
  if (parse_int(score_text, &score) != 0 || score < 0 || score > 100) {
    printf("Error: invalid Score\n");
    return SHELL_ERR_INVALID_SCORE;
  }

  if (add(head, &g_tail, id, name, score) != 0) {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  printf("Student added\n");
  return SHELL_OK;
}

ShellResult handle_delete(char *args, Student **head) {
  char *id_text = strtok(args, " \t");
  char *extra = strtok(NULL, " \t");
  int id = 0;

  if (id_text == NULL || extra != NULL || parse_int(id_text, &id) != 0) {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  if (del(head, &g_tail, id) != 0) {
    printf("student not found\n");
    return SHELL_ERR_STUDENT_NOT_FOUND;
  }

  printf("Student deleted\n");
  return SHELL_OK;
}

ShellResult handle_update(char *args, Student **head) {
  char *id_text = strtok(args, " \t");
  char *score_text = strtok(NULL, " \t");
  char *extra = strtok(NULL, " \t");
  int id = 0;
  int score = 0;

  if (id_text == NULL || score_text == NULL || extra != NULL ||
      parse_int(id_text, &id) != 0 || parse_int(score_text, &score) != 0) {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  if (update(*head, id, score) != 0) {
    printf("student not found\n");
    return SHELL_ERR_STUDENT_NOT_FOUND;
  }

  printf("Student updated\n");
  return SHELL_OK;
}

ShellResult handle_find(char *args, Student **head) {
  char *id_text = strtok(args, " \t");
  char *extra = strtok(NULL, " \t");

  int id = 0;
  Student *st = *head;

  if (id_text == NULL || extra != NULL || parse_int(id_text, &id) != 0) {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  while (st->id != id && st != g_tail) {
    st = st->next;
  }
  if (st->id == id) {
    printf("ID: %d\nName: %s\nScore: %d\n", st->id, st->name, st->score);
    return SHELL_OK;
  } else {
    printf("Error: student not found.\n");
    return SHELL_ERR_STUDENT_NOT_FOUND;
  }
}

ShellResult handle_list(char *args, Student **head) {
  if (args[0] != '\0') {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  list(*head);
  return SHELL_OK;
}

ShellResult handle_sort(char *args, Student **head) {
  (void)args;
  (void)head;

  printf("Error: not implemented\n");
  return SHELL_ERR_UNKNOW_COMMAND;
}

ShellResult handle_stats(char *args, Student **head) {
  (void)args;
  (void)head;

  printf("Error: not implemented\n");
  return SHELL_ERR_UNKNOW_COMMAND;
}

ShellResult handle_help(char *args, Student **head) {
  (void)args;
  (void)head;

  printf("Error: not implemented\n");
  return SHELL_ERR_UNKNOW_COMMAND;
}

ShellResult handle_clear(char *args, Student **head) {
  (void)head;

  if (args[0] != '\0') {
    printf("Error: invalid argument\n");
    return SHELL_ERR_INVALID_ARGUMENT;
  }

  clear();
  return SHELL_OK;
}

ShellResult handle_exit(char *args, Student **head) {
  (void)args;
  (void)head;

  printf("Goodbye\n");
  return SHELL_EXIT;
}
