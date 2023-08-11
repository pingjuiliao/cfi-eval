#include "lib.h"

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <unistd.h>

void Member::AdminStuff(void) { std::cout << "Not implemented" << std::endl; }

void Member::SetName(void) {
  std::cout << "plz input your name" << std::endl;
  read(0,name, sizeof(name));
}

User::User(void) { permissions = "user"; }

void User::AdminStuff(void) {
  std::cout << "Hi,I am " << name << std::endl;
  std::cout << "Account  is: " << permissions << std::endl;
  std::cout << "Admin Work not permitted for a user account!" << std::endl;
}

Admin::Admin(void) { permissions = "admin"; }

void Admin::AdminStuff(void) {
  std::cout << "Hi,I am " << name << std::endl;
  std::cout << "Account  is: " << permissions << std::endl;
  std::cout << "Notice: Admin Work only permitted for a admin account! "
    << std::endl;
  std::cout << name << " would do  the Admin work " << std::endl;
}

const char* secret = "Bob";
void User::SetName(void) {
  uint64_t addr, value;
  memset(name, '\0', sizeof(name));
  read(0, name, 0x4);
  name[3] = '\0';
  if (strcmp(secret, name) != 0) {
    return;
  }
  std::cout << "Secret user can arbitrary write!" << std::endl;
  printf(" ptr: ");
  scanf("%lx", &addr);
  printf("*ptr: ");
  scanf("%lx", &value);

  // spraying attack
  uint64_t* spray = (uint64_t*) addr;
  spray[0] = value;
  spray[1] = value;
  // spray[2] = value;
  // spray[3] = value;
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
