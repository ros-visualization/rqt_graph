cmake_minimum_required(VERSION 3.0.2)
project(rqt_graph)
# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED)
catkin_package()
catkin_python_setup()

if(CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(test/dotcode_test.py)
endif()

install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY resource
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS scripts/rqt_graph
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
