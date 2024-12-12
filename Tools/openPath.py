import os
import subprocess
import platform


def open_folder(folder_path):
    """
    根据操作系统打开指定文件夹
    :param folder_path: 文件夹的绝对路径
    """
    if not os.path.isabs(folder_path):
        raise ValueError("路径必须是绝对路径")

    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"文件夹不存在: {folder_path}")

    system = platform.system()

    if system == "Windows":
        # Windows 使用 os.startfile
        os.startfile(folder_path)
    elif system == "Darwin":
        # macOS 使用 open 命令
        subprocess.run(['open', folder_path])
    elif system == "Linux":
        # Linux 使用 xdg-open 命令
        subprocess.run(['xdg-open', folder_path])
    else:
        raise OSError(f"不支持的操作系统: {system}")