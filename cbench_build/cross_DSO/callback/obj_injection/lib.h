#pragma once
#include <unistd.h>

#include <string>
class Member {
	protected:
		int id;
		std::string permissions;
		char name[0x10];

	public:
		virtual void AdminStuff(void);
		virtual void SetName(void);
};

class User : public Member {
	public:
		User(void);
		virtual void AdminStuff(void);
};

class Admin : public Member {
	public:
		Admin(void);
		virtual void AdminStuff(void);
    virtual void SetName(void);
};

void Execute(Admin *admin, User *user_a, User *user_b);
