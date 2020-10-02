
set (SIMPLE_OUT_SRCS
    test.cpp
    toz3Options.cpp
    )
set (SIMPLE_OUT_HDRS
     toz3Options.h

	)


# extensions are unpleasant with unified builds
build_unified(SIMPLE_OUT_SRCS)

add_executable(simple_out ${SIMPLE_OUT_SRCS})
target_link_libraries (simple_out ${P4C_LIBRARIES} ${P4C_LIB_DEPS})
add_dependencies(simple_out frontend)


install(TARGETS simple_out  RUNTIME DESTINATION ${P4C_RUNTIME_OUTPUT_DIRECTORY})

add_custom_target(linksimple_out
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_CURRENT_BINARY_DIR}/simple_out ${P4C_BINARY_DIR}/simple_out
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${P4C_BINARY_DIR}/p4include ${CMAKE_CURRENT_BINARY_DIR}/p4include
  COMMAND ${CMAKE_COMMAND} -E create_symlink ${P4C_BINARY_DIR}/p4_14include ${CMAKE_CURRENT_BINARY_DIR}/p4_14include
)

add_dependencies(p4c_driver linksimple_out)


