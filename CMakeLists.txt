cmake_minimum_required(VERSION 2.8.3)

project(spotdog)


find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	sdf
	urdf
	controller_manager
	joint_state_controller
	robot_state_publisher
)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf sdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
