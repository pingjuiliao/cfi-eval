#pragma once
#include <unistd.h>
#include <string>

class Member {
	protected:
		char name[0x10];
		int id;
		std::string permissions;

	public:
		virtual void AdminStuff(void);
		virtual void SetName(void);
};

class User : public Member {
	public:
		User(void);
		virtual void AdminStuff(void);
    virtual void SetName(void);
};

class Admin : public Member {
	public:
		Admin(void);
		virtual void AdminStuff(void);
};
