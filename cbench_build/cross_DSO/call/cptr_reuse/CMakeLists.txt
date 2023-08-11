add_library(CptrReuse SHARED
  lib.c
  lib.h)

add_executable(cptr_reuse
  cptr_reuse.c
)

target_link_libraries(cptr_reuse CptrReuse)

configure_file(test.py test.py)
