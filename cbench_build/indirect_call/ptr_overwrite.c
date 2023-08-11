#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef int (*Fptr)(int, int);

int my_read(void *buf, size_t size) {
  int r = read(0, buf, size);
  if (r == 0) {
    printf("error on read");
    exit(-1);
  }
  return r;
}

int SameTypeFunc(int a, int b) {
  printf("In %s \n", __FUNCTION__);
  return 0;
}

void DiffRetFunc(int a, int b) { printf("In %s \n", __FUNCTION__); }

int DiffArgFunc(int a, float b) {
  printf("In %s \n", __FUNCTION__);
  return 0;
}

int MoreArgFunc(int a, int b, int c) {
  printf("In %s \n", __FUNCTION__);
  return 0;
}

int LessArgFunc(int a) {
  printf("In %s \n", __FUNCTION__);
  return 0;
}

int VoidArgFunc(void) {
  printf("In %s \n", __FUNCTION__);
  return 0;
}

int VulEntryFunc(int a, int b) {
  __asm__ volatile("nop\n"
      "nop\n"
      "nop\n"
      "nop\n"
      "nop\n"
      "nop\n"
      "nop\n"
      "nop\n"
      "nop\n"
      "nop\n");
  printf("In %s\n", __FUNCTION__);
  exit(0);
}

int Foo(int a, int b) {
  printf("In %s\n", __FUNCTION__);
  return 0;
}

struct FuncMainStackFrame {
  char name[8];
  Fptr ptr;
};

int main(int argc, const char *argv[]) {
  printf("In %s\n", __FUNCTION__);

  printf("\tSameTypeFunc: %p\n", (void *)SameTypeFunc);
  printf("\tDiffRetFunc: %p\n", (void *)DiffRetFunc);
  printf("\tDiffArgFunc: %p\n", (void *)DiffArgFunc);
  printf("\tMoreArgFunc: %p\n", (void *)MoreArgFunc);
  printf("\tLessArgFunc: %p\n", (void *)LessArgFunc);
  printf("\tVoidArgFunc: %p\n", (void *)VoidArgFunc);
  printf("\tnot_entry: %p\n", (void *)(VulEntryFunc + 0x10));

  printf("In %s\n", __FUNCTION__);

  // Fptr ptr = Foo;
  // char name[8];
  struct FuncMainStackFrame main_stack;
  main_stack.ptr = Foo;

  printf("ptr is %p\n",&main_stack.ptr);
  printf("name is %p\n",main_stack.name);
  // buffer overflow
  printf("plz input your name:\n");
  my_read((void *)&main_stack.name, 0x20);
  main_stack.ptr(0, 0);

  return 0;
}
