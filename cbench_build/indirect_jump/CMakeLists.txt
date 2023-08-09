
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pthread")

add_executable(tailcall_overwrite
  tailcall_overwrite.c
)

add_executable(tailcall_reuse_single_phread
  tailcall_reuse_single_phread.c
)

add_executable(tailcall_reuse_multithreading
  tailcall_reuse_multithreading.c
)
#target_compile_options(tailcall_reuse_multithreading PRIVATE
#  -pthread)

configure_file(test.py test.py)
