add_library(CallbackObjectReuse SHARED
  lib.cpp
  lib.h
)

add_executable(callback_obj_reuse
  callback_obj_reuse.cpp
)

target_link_libraries(callback_obj_reuse
  CallbackObjectReuse
)

configure_file(test.py test.py)
