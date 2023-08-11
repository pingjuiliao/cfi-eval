add_library(ObjectInjection SHARED
  lib.cpp
  lib.h
)

add_executable(obj_inject
  obj_inject.cpp
)

target_link_libraries(obj_inject
  ObjectInjection
)

configure_file(test.py test.py)
