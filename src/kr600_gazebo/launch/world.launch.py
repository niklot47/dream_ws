from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Путь к файлу мира
    world_file_name = 'simple_world.sdf'
    world_path = os.path.join(get_package_share_directory('kr600_gazebo'), 'worlds', world_file_name)

    return LaunchDescription([
        # Запуск Gazebo (Ignition) с миром
        ExecuteProcess(
            cmd=['ign', 'gazebo', world_path, '--verbose'],
            output='screen'
        ),
    ])