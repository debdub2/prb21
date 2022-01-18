cmake_minimum_required(VERSION 3.0.2)
project(square_moving)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  geometry_msgs
  tutrtlesim
)


generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
  tutrtlesim
)


catkin_package(
  CATKIN_DEPENDS message_runtime
)


catkin_install_python(PROGRAMS
  scripts/moving_square.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
