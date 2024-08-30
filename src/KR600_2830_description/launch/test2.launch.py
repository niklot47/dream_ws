import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'KR600_2830_description'
    urdf_filename = 'model.urdf'
    
    pkg_share_description = FindPackageShare(pkg_name)
    default_urdf_model_path = PathJoinSubstitution([pkg_share_description, 'urdf', urdf_filename])

  # Configure the node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': default_urdf_model_path}] # add other parameters here if required
    )


    # Run the node
    return LaunchDescription([
        node_robot_state_publisher
    ])
