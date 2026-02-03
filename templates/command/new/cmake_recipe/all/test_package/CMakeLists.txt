cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES C)

find_package({{as_name(name)}} REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.c)
target_link_libraries(${PROJECT_NAME} PRIVATE {{as_name(name)}}::{{as_name(name)}})

