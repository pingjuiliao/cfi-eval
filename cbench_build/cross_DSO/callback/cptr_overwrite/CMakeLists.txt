add_library(CallbackCptrOverwrite SHARED
  lib.c
  lib.h
)

add_executable(callback_cptr_overwrite
  callback_cptr_overwrite.c
)

target_link_libraries(callback_cptr_overwrite CallbackCptrOverwrite)

configure_file(test.py test.py)
