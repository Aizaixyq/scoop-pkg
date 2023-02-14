# 导入os模块，用于操作文件和目录
import os

# 定义一个函数，用于获取文件名的首字母
def get_first_letter(filename, len):
    # 如果文件名为空，返回空字符串
    if not filename:
        return ""
    # 如果文件名不是json文件，返回空字符串
    if not filename.endswith(".json"):
        return ""
    # 如果文件名的第一个字符是数字，返回"Number"
    if filename[0].isdigit():
        return "num"
    # 否则，返回文件名的第一个字符，转换为大写
    return filename[0:len].lower()

# 定义一个函数，用于将文件夹下的json文件按照首字母分类
def classify_json_files(folder, len):
    # 遍历文件夹下的所有文件和子目录
    for item in os.listdir(folder):
        # 获取文件或子目录的完整路径
        path = os.path.join(folder, item)
        # 如果是文件
        if os.path.isfile(path):
            # 获取文件名的首字母
            letter = get_first_letter(item, len)
            # 如果首字母不为空
            if letter:
                # 创建一个以首字母命名的子文件夹，如果已存在则忽略
                subfolder = os.path.join(folder, letter)
                os.makedirs(subfolder, exist_ok=True)
                # 将文件移动到子文件夹中
                new_path = os.path.join(subfolder, item)
                os.rename(path, new_path)
                # 打印移动的信息
                print(f"Moved {path} to {new_path}")
        # 如果是子目录，递归调用函数
        elif os.path.isdir(path):
            classify_json_files(path)

# 定义一个函数，用于移动一个文件夹下所有json文件到另一个文件夹下
def move_json_files(source_folder, target_folder):
    # 遍历源文件夹下的所有文件和子目录
    for item in os.listdir(source_folder):
        # 获取文件或子目录的完整路径
        path = os.path.join(source_folder, item)
        # 如果是文件
        if os.path.isfile(path):
            # 如果是json文件
            if item.endswith(".json"):
                # 将文件移动到目标文件夹中
                new_path = os.path.join(target_folder, item)
                os.copy(path, new_path)
                # 打印移动的信息
                print(f"copy {path} to {new_path}")
        # 如果是子目录，递归调用函数
        elif os.path.isdir(path):
            move_json_files(path, target_folder)

#copy from extras and main
move_json_files('.\\Extras\\bucket', ".\\bucket")
move_json_files('.\\Main\\bucket', ".\\bucket")
# 调用函数，传入要分类的文件夹路径
classify_json_files(".\\bucket", 1)


# 导入string模块，用于获取字母表
import string

# 遍历字母表中的小写字母
for letter in string.ascii_lowercase:
    classify_json_files(".\\bucket\\"+letter, 2)