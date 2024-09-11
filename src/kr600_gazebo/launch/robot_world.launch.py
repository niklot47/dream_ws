from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Путь к файлу мира
    world_file_name = 'simple_world.sdf'
    world_path = os.path.join(get_package_share_directory('kr600_gazebo'), 'worlds', world_file_name)

    # Путь к файлу робота URDF
    robot_urdf_file = os.path.join(get_package_share_directory('kr600'), 'urdf', 'gazebo.urdf.xacro')

    # Запуск Gazebo с миром
    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', world_path, '--verbose'],
        output='screen'
    )

    # Узел для публикации модели робота в Ignition Gazebo (робот спавнится на -1.5м по оси X)
    spawn_robot = Node(
        package='ros_gz_sim', 
        executable='create', 
        arguments=['-file', robot_urdf_file, '-name', 'kr600', '-x', '-1.5', '-z', '0.5'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])
