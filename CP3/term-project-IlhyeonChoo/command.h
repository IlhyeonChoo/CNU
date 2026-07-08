#ifndef COMMAND_H
#define COMMAND_H

#include "student.h"
#include <stddef.h>

typedef enum {
  SHELL_OK = 0,
  SHELL_EXIT,
  SHELL_ERR_UNKNOW_COMMAND,
  SHELL_ERR_INVALID_ARGUMENT,
  SHELL_ERR_MISSING_ARGUMENT,
  SHELL_ERR_FILE_OPEN,
  SHELL_ERR_FILE_WRITE,
  SHELL_ERR_STUDENT_NOT_FOUND,
  SHELL_ERRDUPLICATE_STUDENT,
  SHELL_ERR_INVALID_SCORE,
} ShellResult;

typedef ShellResult (*CommandHandler)(char *args, Student **head);

typedef struct {
  const char *name;
  CommandHandler handler;
  const char *usage;
  const char *description;
} Command;

extern Command commands[];
extern size_t command_count; // 명령어 탐색 범위, help 명령어

ShellResult execute_command(char *line, Student **head);

ShellResult handle_save(char *args, Student **head);
ShellResult handle_reload(char *args, Student **head);
ShellResult handle_add(char *args, Student **head);
ShellResult handle_delete(char *args, Student **head);
ShellResult handle_update(char *args, Student **head);
ShellResult handle_find(char *args, Student **head);
ShellResult handle_list(char *args, Student **head);
ShellResult handle_sort(char *args, Student **head);
ShellResult handle_stats(char *args, Student **head);
ShellResult handle_help(char *args, Student **head);
ShellResult handle_clear(char *args, Student **head);
ShellResult handle_exit(char *args, Student **head);

#endif // !COMMAND_H
