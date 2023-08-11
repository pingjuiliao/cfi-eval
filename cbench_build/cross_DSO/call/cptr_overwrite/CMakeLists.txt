# Cptr Overwrite
add_library(CptrOverwrite
  lib.c
  lib.h
)

add_executable(cptr_overwrite
  cptr_overwrite.c
)

target_link_libraries(cptr_overwrite
  CptrOverwrite
)

configure_file(test.py test.py)
