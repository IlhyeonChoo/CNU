/*
 * main.c  –  Mini Student Shell
 *
 * TODO: Implement admin_shell and client_shell.
 *
 * Build:
 *   make admin   →  admin_shell  (compiled with -DADMIN_MODE)
 *   make client  →  client_shell (compiled with -DCLIENT_MODE)
 *
 * Usage:
 *   ./admin_shell [students.csv]
 *   ./admin_shell -f commands.txt [students.csv]
 *   ./client_shell [students.csv]
 *   ./client_shell -f commands.txt [students.csv]
 */

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "command.h"
#include "file_io.h"
#include "student.h"

#define INPUT_LINE_SIZE 256

Student *g_head = NULL;
Student *g_tail = NULL;
const char *g_csv_path;
int student_count;

// 프로그램 실행 방법 출력
static void print_usage(const char *program_name) {
  printf("Usage: %s [students.csv] [-f commands.txt]\n", program_name);
}

static char *skip_spaces(char *text) {
  while (*text != '\0' && isspace((unsigned char)*text)) {
    text++;
  }
  return text;
}

static void strip_line_end(char *text) { text[strcspn(text, "\r\n")] = '\0'; }

/* ---------------------------------------------------------------
 * TODO: Implement the interactive shell loop.
 *   - Print a prompt and read a line from stdin.
 *   - Parse the line into a command and arguments.
 *   - Dispatch to the appropriate handler function.
 *   - Loop until the user types "exit" or EOF.
 * --------------------------------------------------------------- */
void run_shell(const char *csv_path) {
  /* TODO */
  (void)csv_path;

  char line[INPUT_LINE_SIZE];

  // 명령어 입력 받아서 execute_command로 전달 반
  while (fgets(line, sizeof(line), stdin) != NULL) {
    ShellResult result = execute_command(line, &g_head);
    if (result == SHELL_EXIT) {
      break;
    }
  }
}

/* ---------------------------------------------------------------
 * TODO: Implement batch mode – read commands from a file.
 *   - Open cmd_file for reading.
 *   - Execute each line as a command (same logic as run_shell).
 *   - Close the file when done.
 * --------------------------------------------------------------- */
ShellResult run_command_file(const char *cmd_file, const char *csv_path) {
  (void)csv_path;

  FILE *file = fopen(cmd_file, "r");
  if (file == NULL) {
    printf("Error: failed to open command file\n");
    return SHELL_ERR_FILE_OPEN;
  }

  char line[INPUT_LINE_SIZE];
  int command_line = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    strip_line_end(line);
    char *command = skip_spaces(line);

    if (command[0] == '\0' || command[0] == '#') {
      continue;
    }

    command_line++;
    printf("[command file:%d] %s\n", command_line, command);

    ShellResult result = execute_command(command, &g_head);
    if (result == SHELL_EXIT) {
      fclose(file);
      return SHELL_EXIT;
    }
    if (result != SHELL_OK) {
      printf("Skipped line %d\n", command_line);
    }
  }

  fclose(file);
  return SHELL_OK;
}

int main(int argc, char *argv[]) {
  const char *cmd_file = NULL; /* -f <file> argument */

  /* TODO: Parse command-line arguments.
   *   Supported flags:
   *     -f <file>   run commands from <file> instead of stdin
   *   Remaining positional argument (if any): path to students CSV.
   *
   *   Example parsing skeleton:
   *
   *   for (int i = 1; i < argc; i++) {
   *       if (strcmp(argv[i], "-f") == 0 && i + 1 < argc) {
   *           cmd_file = argv[++i];
   *       } else {
   *           csv_path = argv[i];
   *       }
   *   }
   */

  for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "-f") == 0) {
      if (i + 1 >= argc) {
        printf("Error: -f requires a command file\n");
        print_usage(argv[0]);
        return 1;
      }
      cmd_file = argv[++i];
    } else {
      g_csv_path = argv[i];
    }
  }

  // csv 파일 열기 실패
  if ((student_count = open_csv(g_csv_path, &g_head, &g_tail)) < 0) {
    printf("Error: failed to open CSV file\n");
    print_usage(argv[0]);
    return 1;
  }

#ifdef ADMIN_MODE
  /* Admin shell: supports add, delete, update, save, load, sort, list, find,
   * help, exit */
  printf("[Admin Program]\n");
  printf("Loaded %d students from %s\n", student_count, g_csv_path);
  if (cmd_file) {
    if (run_command_file(cmd_file, g_csv_path) == SHELL_EXIT) {
      // 실행 후 종료
      exit_csv(g_head);
      return 0;
    }
  }
  run_shell(g_csv_path);

#elif defined(CLIENT_MODE)
  /* Client shell: supports find, list, help, exit  (read-only) */
  printf("[Client Program]\n");
  printf("Loaded %d students from %s\n", student_count, g_csv_path);
  if (cmd_file) {
    if (run_command_file(cmd_file, g_csv_path) == SHELL_EXIT) {
      exit_csv(g_head);
      return 0;
    }
  }
  run_shell(g_csv_path);

#else
#error "Define either -DADMIN_MODE or -DCLIENT_MODE when compiling."
#endif

  exit_csv(g_head);
  return 0;
}
