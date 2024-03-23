# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT fengyun2_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT fengyun2_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND fengyun2_python_files
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(fengyun2
   ../../..
   gr::fengyun2
   "${fengyun2_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET fengyun2_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:fengyun2_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/fengyun2/
)

install(TARGETS fengyun2_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/fengyun2 COMPONENT pythonapi)
