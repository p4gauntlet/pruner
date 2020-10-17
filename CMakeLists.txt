
set (P4PRUNER_SRCS
    src/main.cpp
    src/pruner_options.cpp
    src/pruner_util.cpp
    src/statement_pruner.cpp
    src/compiler_pruner.cpp
    )
set (P4PRUNER_HDRS
    src/pruner_options.h
    src/pruner_util.h
    src/statement_pruner.h
    src/compiler_pruner.h
    )


# extensions are unpleasant with unified builds
build_unified(P4PRUNER_SRCS)

add_executable(p4pruner ${P4PRUNER_SRCS})
target_link_libraries (p4pruner ${P4C_LIBRARIES} ${P4C_LIB_DEPS})
add_dependencies(p4pruner frontend)


install(TARGETS p4pruner  RUNTIME DESTINATION ${P4C_RUNTIME_OUTPUT_DIRECTORY})

add_custom_target(linkp4pruner
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_CURRENT_BINARY_DIR}/p4pruner ${P4C_BINARY_DIR}/p4pruner
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${P4C_BINARY_DIR}/p4include ${CMAKE_CURRENT_BINARY_DIR}/p4include
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${P4C_BINARY_DIR}/p4_14include ${CMAKE_CURRENT_BINARY_DIR}/p4_14include
)

add_dependencies(p4c_driver linkp4pruner)


