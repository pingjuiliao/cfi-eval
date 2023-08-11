#include "lib.h"

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <unistd.h>

void Execute(Admin *admin, User *user_a, User *user_b) {
	std::cout << "Admin registration:" << std::endl;
	admin->SetName();
	admin->AdminStuff();

	std::cout << "UserA registration:" << std::endl;
	user_a->SetName();
	user_a->AdminStuff();

	std::cout << "UserB registration:" << std::endl;
	user_b->SetName();
	user_b->AdminStuff();

	std::cout << "UserA Rename:" << std::endl;
	user_a->SetName();

	std::cout << "Check UserB again:" << std::endl;
	user_b->AdminStuff();
}

int main(int argc, const char *argv[]) {
  Admin *admin = new Admin();
  User *user_a = new User();
  User *user_b = new User();
  Member *vul = new Member;

  setbuf(stdin, NULL);
  setbuf(stdout, NULL);

  void **same_vtable = *(void ***)user_a;
  void **base_vtable = *(void ***)vul;
  void **Diff_vtable = *(void ***)admin;
  printf("It is the cross-DSO callback reuse test");
  printf("It is the coop test\n");
  printf("UserA address is %p\n", user_a);
  printf("UserB address is %p\n", user_b);
  printf("admin address is %p\n", admin);
  printf("the same class vtable address is %p\n", same_vtable);
  printf("the base class vtable address is %p\n", base_vtable);
  printf("the diff class vtable address is %p\n", Diff_vtable);
  printf("if hacked successfully,it will give the admin Permissions  to "
      "userB \n");

  Execute(admin, user_a, user_b);

  return 0;
}
