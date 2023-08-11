#include "lib.h"
#include <stdio.h>

typedef int (*Fptr)(int, int);

__attribute__((visibility("default"))) void Callback(Fptr ptr) {

  printf("ptr is: %p\n", ptr);
  printf("ptr address is: %p\n", &ptr);
  // Assuming that the attacker has the ability to write to any address
  void **anyptr;
  printf("plz input the value of anyptr: \n");
  scanf("%p", &anyptr);
  printf("plz change the value of *anyptr: \n");
  scanf("%p", anyptr);

  ptr(0, 0);
}
