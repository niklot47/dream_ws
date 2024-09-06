import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition

def generate_launch_description():
    # Path to the world file
    pkg_gazebo = FindPackageShare(package='kr600_gazebo').find('kr600_gazebo')
    world_file = os.path.join(pkg_gazebo, 'worlds', 'simple_world.sdf')

    # Path to RViz configuration
    pkg_kr600 = FindPackageShare(package='kr600').find('kr600')
    rviz_config_file = os.path.join(pkg_kr600, 'rviz', 'config.rviz')

    # Path to the new RViz-specific URDF file
    urdf_file_rviz = os.path.join(pkg_kr600, 'urdf', 'model_rviz.urdf.xacro')

    # Launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    use_gui = LaunchConfiguration('use_gui', default='true')  # To control GUI mode for Gazebo

    return LaunchDescription([

        # Launch argument to toggle GUI in Gazebo
        DeclareLaunchArgument(
            'use_gui',
            default_value='true',
            description='Flag to enable/disable Gazebo GUI'
        ),

        # Gazebo simulation launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(pkg_gazebo, 'launch', 'gazebo.launch.py')),
            launch_arguments={
                'world': world_file,
                'gui': use_gui
            }.items(),
        ),

        # Публикация joint_states для робота
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=[urdf_file_rviz]  
        ),

        # RViz2 launch
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file],
            parameters=[{'use_sim_time': True}]
        ),

        # Запуск controller_manager
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[{'use_sim_time': True}],
            output='screen'
        ),
        
        # Joint State Broadcaster (если требуется)
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_state_broadcaster'],
            output='screen'
        ),

    ])
