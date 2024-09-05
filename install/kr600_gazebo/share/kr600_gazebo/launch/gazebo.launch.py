from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Путь к директории пакета
    pkg_share_dir = get_package_share_directory('kr600')
    models_path = os.path.join(pkg_share_dir, 'meshes')
    
    # Установить переменную окружения для Gazebo
    os.environ['GZ_SIM_RESOURCE_PATH'] = models_path

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'),
            'launch', 'gz_sim.launch.py'
        )])
    )

    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-file', os.path.join(pkg_share_dir, 'urdf', 'model.urdf.xacro'), '-name', 'kr600'],
        output='screen'
    )

    return LaunchDescription([
        SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', models_path),
        gazebo,
        spawn_entity,
    ])
