#################################
####请注意，本软件版权为GPL3.0#####
####请注意，本软件版权暂归苏妲#####
####请注意，本软件禁止非授权商用####
####请注意，本软件仍处于beta版本####
####请注意，本软件仍有重大bug######
#################################


import re
import os
import shutil
import subprocess
import requests

header = "\t\""
Tail = "\"\n\t{\n\t\t\t\"default\"\t\t\"\"\n\t\t\t\"timer\"\t\t\"0\"\n\t\t\t\"timercover\"\t\t\"0\"\n\t\t\t\"timertip\"\t\t\"倒计时 {time} 秒\"\n\t\t\t\"timerend\"\t\t\"\"\n\t}\n"
top_header = "\"ConsoleMessage\"\n{\n"
top_tail = "\n}"

###########
###函数区###
###########

##检查是否拥有反编译工具，没有就下载
def check_and_download_file(url, filename):
    if os.path.exists(filename):
        print("反编译工具存在，正在开始工作")
    else:
        print("反编译工具不存在，正在开始下载")
        try:
            response = requests.get(url)
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"下载 '{filename}' 完成.继续进行地图检测文本")
        except requests.RequestException as e:
            print(f" 尝试从 '{url}'下载 '{filename}'失败，错误为: {e}")
            input("请按下任意键退出程序...")
            exit()

##检查是否有且只有一个bsp文件
def count_bsp_files():
    bsp_files = [file for file in os.listdir() if file.endswith(".bsp")]
    return len(bsp_files)

##检查是否没有vmf文件
def count_vmf_files():
    vmf_files = [file for file in os.listdir() if file.endswith(".vmf")]
    return len(vmf_files)


##寻找bsp并记录进目录中
def find_bsp_files(directory):
    bsp_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".bsp"):
                bsp_files.append(os.path.abspath(os.path.join(root, file)))
    return bsp_files
def save_to_file(file_list, output_file):
    with open(output_file, "w") as f:
        for file_path in file_list:
            f.write(file_path + "\n")

##将vmf复制一份并重命名，不对原文件进行操作
def copy_and_rename_files(source_folder, destination_folder, target_extension, new_name):
    for root, _, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith(target_extension):
                source_path = os.path.join(root, filename)
                destination_path = os.path.join(destination_folder, new_name)

                # To avoid overwriting an existing file, add a number to the new_name if it already exists.
                counter = 1
                while os.path.exists(destination_path):
                    new_name_with_counter = f"{new_name}_{counter}"
                    destination_path = os.path.join(destination_folder, new_name_with_counter)
                    counter += 1

                # Copy the file and rename it.
                shutil.copy2(source_path, destination_path)

##用于提取关键字，原句保留
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_f:
        lines = input_f.readlines()

    matching_lines = [line.strip() for line in lines if 'say' in line]

    if matching_lines:
        with open(output_file, 'w', encoding='utf-8') as output_f:
            output_f.write('\n'.join(matching_lines))
    else:
        # If no matching lines, delete the output file (if it exists)
        try:
            import os
            os.remove(output_file)
        except FileNotFoundError:
            pass

##用于提取原文内容
def engthing(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_f:
        content = input_f.read()

    # Use regular expression to find content between '0000' and '1111'
    pattern = re.compile(r'say (.*?)', re.DOTALL)
    extracted_text = pattern.findall(content)

    # Write the extracted text to the output file
    with open(output_file, 'w', encoding='utf-8') as output_f:
        output_f.write('\n'.join(extracted_text))

#去重复
def remove_duplicates(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Remove duplicates while preserving the order
    unique_lines = list(dict.fromkeys(lines))

    with open(output_file, 'w') as f:
        f.writelines(unique_lines)

##格式化
def text_formatted(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            processed_line = header + line.strip() + Tail
            f.write(processed_line)

##修改为top社区格式
def modify_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(top_header + content)  # Add "top_header" at the beginning
            file.write(top_tail)  # Add "top_tail" at the end
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
##批量删除过程垃圾模块
def delete_files():
    files_to_delete = ["1command.txt", "2text.txt", "3text_deduplicated.txt", "4text_formatted.cfg", "input.txt", "path.txt"]
    current_directory = os.getcwd()

    for filename in files_to_delete:
        file_path = os.path.join(current_directory, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {filename}")
        else:
            print(f"{filename} not found, skipping.")
###########
###操作区###
###########

##主函数前检查
if __name__ == "__main__":
    jar_file_url = "https://gitee.com/moefox_kimo/disk/releases/download/test/bspsrc.jar"
    jar_file_name = "bspsrc.jar"
    print("正在检查bsp文件数量是否唯一")
    bsp_count = count_bsp_files()
    if bsp_count == 1:
        print("只有一个bsp文件，检查vmf数量中")
    elif bsp_count > 1:
        print("多个bsp文件")
        input("请按下任意键退出程序...")
        exit()
    else:
        print("没有找到bsp文件")
        input("请按下任意键退出程序...")
        exit()
    vmf_count = count_vmf_files()
    if vmf_count == 0:
        print("vmf文件不存在，正在检查是否包含反编译工具")
    else:
        print("存在vmf文件")
        input("请按下任意键退出程序...")
    check_and_download_file(jar_file_url, jar_file_name)
    # 继续执行后面的代码
    print("正在执行其他命令")


if __name__ == "__main__":
    target_directory = "."  # 可以修改为你想要查找的目录
    output_file = "path.txt"

    bsp_files = find_bsp_files(target_directory)
    save_to_file(bsp_files, output_file)
    print(f"Found {len(bsp_files)} .bsp files. Paths saved in {output_file}.")
    print(os.path.dirname(os.path.abspath(__file__)))

# 要执行的命令
path1 = os.path.dirname(os.path.abspath(__file__))
command = "java -jar .\\bspsrc.jar -l " + path1 + "\path.txt"  # 这里使用了Linux的ls命令，可以替换成其他命令或程序

# 使用subprocess.run()函数执行命令
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# 输出命令的执行结果
print("返回值:", result.returncode)
print("标准输出:", result.stdout)
print("错误输出:", result.stderr)

##重命名
if __name__ == "__main__":
    # Get the current working directory (where the script is located).
    current_directory = os.getcwd()
    # The source folder is the current directory.
    source_folder = current_directory
    # The destination folder can be the same as the source folder or a different one.
    destination_folder = current_directory
    # The target extension you want to copy (e.g., ".vmf").
    target_extension = ".vmf"
    # The new name for the copied files.
    new_name = "input.txt"
    copy_and_rename_files(source_folder, destination_folder, target_extension, new_name)

##开始提取关键字
if __name__ == '__main__':
    input_file = 'input.txt'   # Replace with your input file name
    output_file = '1command.txt' # Replace with your output file name
    process_file(input_file, output_file)

##开始提取原文内容
if __name__ == '__main__':
    input_file = '1command.txt'  # Replace with your extracted file name
    output_file = '2text.txt'  # Replace with your final output file name

    engthing(input_file, output_file)

##开始去重
if __name__ == "__main__":
    input_file = '2text.txt'  # Replace with your final output file name
    output_file = '3text_deduplicated.txt'  # Replace with your new output file name
    remove_duplicates(input_file, output_file)

##格式化
if __name__ == "__main__":
    input_filename = "3text_deduplicated.txt"
    output_filename = "4text_formatted.cfg"
    text_formatted(input_filename, output_filename)
    modify_file(output_filename)
    print("文件处理完成！")

##最终重命名
# 输出结果
# 获取当前脚本所在的目录
current_directory = os.path.dirname(os.path.abspath(__file__))
# 获取文件夹内的所有文件名
files = os.listdir(current_directory)
# 初始化变量name0101
new_name = None
# 遍历文件名，找到后缀名为'.vmf'的文件名并保存不带后缀名的部分
for file in files:
    if file.endswith('.vmf'):
        new_name = os.path.splitext(file)[0]
        break
print(new_name)
file_name = "4text_formatted.cfg"
new_file_name = f"{new_name}.cfg"
# 检查是否存在同名文件，若存在则进行重命名
counter = 0
while os.path.exists(new_file_name):
    counter += 1
    new_file_name = f"{new_name}_{counter}.cfg"
# 复制文件
shutil.copy(file_name, new_file_name)
##删除过程垃圾（注释此段可以debug）
if __name__ == "__main__":
    delete_files()