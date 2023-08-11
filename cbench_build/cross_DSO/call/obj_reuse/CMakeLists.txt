add_library(ObjectReuse SHARED
  lib.cpp
  lib.h
)

add_executable(obj_reuse
  obj_reuse.cpp
)

target_link_libraries(obj_reuse
  ObjectReuse
)

configure_file(test.py test.py)
