add_library(CallbackCptrReuse SHARED
  lib.c
  lib.h)

add_executable(callback_cptr_reuse
  callback_cptr_reuse.c
)

target_link_libraries(callback_cptr_reuse CallbackCptrReuse)

configure_file(test.py test.py)
