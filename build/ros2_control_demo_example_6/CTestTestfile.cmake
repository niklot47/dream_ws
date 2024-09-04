# CMake generated Testfile for 
# Source directory: /root/dream_ws/src/ros2_control_demos/example_6
# Build directory: /root/dream_ws/build/ros2_control_demo_example_6
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(example_6_urdf_xacro "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/root/dream_ws/build/ros2_control_demo_example_6/test_results/ros2_control_demo_example_6/example_6_urdf_xacro.xunit.xml" "--package-name" "ros2_control_demo_example_6" "--output-file" "/root/dream_ws/build/ros2_control_demo_example_6/ament_cmake_pytest/example_6_urdf_xacro.txt" "--command" "/usr/bin/python3" "-u" "-m" "pytest" "/root/dream_ws/src/ros2_control_demos/example_6/test/test_urdf_xacro.py" "-o" "cache_dir=/root/dream_ws/build/ros2_control_demo_example_6/ament_cmake_pytest/example_6_urdf_xacro/.cache" "--junit-xml=/root/dream_ws/build/ros2_control_demo_example_6/test_results/ros2_control_demo_example_6/example_6_urdf_xacro.xunit.xml" "--junit-prefix=ros2_control_demo_example_6")
set_tests_properties(example_6_urdf_xacro PROPERTIES  LABELS "pytest" TIMEOUT "60" WORKING_DIRECTORY "/root/dream_ws/build/ros2_control_demo_example_6" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/root/dream_ws/src/ros2_control_demos/example_6/CMakeLists.txt;68;ament_add_pytest_test;/root/dream_ws/src/ros2_control_demos/example_6/CMakeLists.txt;0;")
add_test(view_example_6_launch "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/root/dream_ws/build/ros2_control_demo_example_6/test_results/ros2_control_demo_example_6/view_example_6_launch.xunit.xml" "--package-name" "ros2_control_demo_example_6" "--output-file" "/root/dream_ws/build/ros2_control_demo_example_6/ament_cmake_pytest/view_example_6_launch.txt" "--command" "/usr/bin/python3" "-u" "-m" "pytest" "/root/dream_ws/src/ros2_control_demos/example_6/test/test_view_robot_launch.py" "-o" "cache_dir=/root/dream_ws/build/ros2_control_demo_example_6/ament_cmake_pytest/view_example_6_launch/.cache" "--junit-xml=/root/dream_ws/build/ros2_control_demo_example_6/test_results/ros2_control_demo_example_6/view_example_6_launch.xunit.xml" "--junit-prefix=ros2_control_demo_example_6")
set_tests_properties(view_example_6_launch PROPERTIES  LABELS "pytest" TIMEOUT "60" WORKING_DIRECTORY "/root/dream_ws/build/ros2_control_demo_example_6" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/root/dream_ws/src/ros2_control_demos/example_6/CMakeLists.txt;69;ament_add_pytest_test;/root/dream_ws/src/ros2_control_demos/example_6/CMakeLists.txt;0;")
add_test(run_example_6_launch "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/root/dream_ws/build/ros2_control_demo_example_6/test_results/ros2_control_demo_example_6/run_example_6_launch.xunit.xml" "--package-name" "ros2_control_demo_example_6" "--output-file" "/root/dream_ws/build/ros2_control_demo_example_6/ament_cmake_pytest/run_example_6_launch.txt" "--command" "/usr/bin/python3" "-u" "-m" "pytest" "/root/dream_ws/src/ros2_control_demos/example_6/test/test_rrbot_modular_actuators_launch.py" "-o" "cache_dir=/root/dream_ws/build/ros2_control_demo_example_6/ament_cmake_pytest/run_example_6_launch/.cache" "--junit-xml=/root/dream_ws/build/ros2_control_demo_example_6/test_results/ros2_control_demo_example_6/run_example_6_launch.xunit.xml" "--junit-prefix=ros2_control_demo_example_6")
set_tests_properties(run_example_6_launch PROPERTIES  LABELS "pytest" TIMEOUT "60" WORKING_DIRECTORY "/root/dream_ws/build/ros2_control_demo_example_6" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/root/dream_ws/src/ros2_control_demos/example_6/CMakeLists.txt;70;ament_add_pytest_test;/root/dream_ws/src/ros2_control_demos/example_6/CMakeLists.txt;0;")
