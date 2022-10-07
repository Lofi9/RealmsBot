cmake_minimum_required(VERSION 3.23)
project(RealmsBot)

set(CMAKE_CXX_STANDARD 14)

add_executable(RealmsBot main.cpp)

add_subdirectory(sleepy-discord)
target_link_libraries(RealmsBot sleepy-discord)