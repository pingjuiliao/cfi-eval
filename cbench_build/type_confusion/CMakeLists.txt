add_executable(cfi_function
  cfi_function.c)

add_executable(cfi_object
  cfi_object.cpp)

add_executable(cfi_object_function
  cfi_object_function.cpp)


configure_file(test.py test.py)
