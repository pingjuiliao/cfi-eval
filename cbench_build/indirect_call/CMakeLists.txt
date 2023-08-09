set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")

add_executable(ptr_OOB
  ptr_OOB.c)

add_executable(ptr_overwrite
  ptr_overwrite.c)

configure_file(
  test.py test.py
)
