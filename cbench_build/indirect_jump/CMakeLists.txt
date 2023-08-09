
add_executable(tailcall_overwrite
  tailcall_overwrite.c
)

add_executable(tailcall_reuse_multithreading
  tailcall_reuse_multithreading.c
)

add_executable(tailcall_reuse_single_phread
  tailcall_reuse_single_phread.c
)

configure_file(test.py test.py)
