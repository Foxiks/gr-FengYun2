find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_FENGYUN2 gnuradio-fengyun2)

FIND_PATH(
    GR_FENGYUN2_INCLUDE_DIRS
    NAMES gnuradio/fengyun2/api.h
    HINTS $ENV{FENGYUN2_DIR}/include
        ${PC_FENGYUN2_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_FENGYUN2_LIBRARIES
    NAMES gnuradio-fengyun2
    HINTS $ENV{FENGYUN2_DIR}/lib
        ${PC_FENGYUN2_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-fengyun2Target.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_FENGYUN2 DEFAULT_MSG GR_FENGYUN2_LIBRARIES GR_FENGYUN2_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_FENGYUN2_LIBRARIES GR_FENGYUN2_INCLUDE_DIRS)
