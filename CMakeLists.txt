
set (PRUNER_SRCS
    main.cpp
    toz3Options.cpp
    )
set (PRUNER_HDRS
     toz3Options.h

	)


# extensions are unpleasant with unified builds
build_unified(PRUNER_SRCS)

add_executable(pruner ${PRUNER_SRCS})
target_link_libraries (pruner ${P4C_LIBRARIES} ${P4C_LIB_DEPS})
add_dependencies(pruner frontend)


install(TARGETS pruner  RUNTIME DESTINATION ${P4C_RUNTIME_OUTPUT_DIRECTORY})

add_custom_target(linkpruner
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_CURRENT_BINARY_DIR}/simple_out ${P4C_BINARY_DIR}/pruner
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${P4C_BINARY_DIR}/p4include ${CMAKE_CURRENT_BINARY_DIR}/p4include
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${P4C_BINARY_DIR}/p4_14include ${CMAKE_CURRENT_BINARY_DIR}/p4_14include
)

add_dependencies(p4c_driver linkpruner)


