#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef int (*Fptr)(int, int);

int my_read(void* buf, size_t size) {
  int r = read(0, buf, size);
  if (r == 0) {
    printf("error on read\n");
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

struct ExcuteStackFrame {
  char name[0x10];
  Fptr ptr;
};

int excute(void) {
  printf("In %s\n", __FUNCTION__);

  struct ExcuteStackFrame stack_frame;
  printf("name is : %p \n", stack_frame.name);
  printf("ptr is : %p \n", &stack_frame.ptr);
  // buffer overflow
  printf("plz input your name:\n");
  my_read((void *)stack_frame.name, 0x30);
  return stack_frame.ptr(0, 0);
}

int main(int argc, const char *argv[]) {

  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  printf("\tSameTypeFunc: %p\n", (void *)SameTypeFunc);
  printf("\tDiffRetFunc: %p\n", (void *)DiffRetFunc);
  printf("\tDiffArgFunc: %p\n", (void *)DiffArgFunc);
  printf("\tMoreArgFunc: %p\n", (void *)MoreArgFunc);
  printf("\tLessArgFunc: %p\n", (void *)LessArgFunc);
  printf("\tVoidArgFunc: %p\n", (void *)VoidArgFunc);
  printf("\tnot_entry: %p\n", (void *)(VulEntryFunc + 0x10));

  printf("In %s\n", __FUNCTION__);
  excute();
  return 0;
}
