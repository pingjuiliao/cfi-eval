add_library(CallbackObjectInjection SHARED
  lib.cpp
  lib.h
)

add_executable(callback_obj_inject
  callback_obj_inject.cpp
)

target_link_libraries(callback_obj_inject
  CallbackObjectInjection
)

configure_file(test.py test.py)
