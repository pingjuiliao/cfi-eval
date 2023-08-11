cmake_minimum_required(VERSION 3.11)
project(CBench VERSION 1.0)

add_subdirectory(indirect_call)
add_subdirectory(indirect_jump)
add_subdirectory(type_confusion)
add_subdirectory(cross_DSO)
configure_file(benchmark.sh benchmark.sh)
