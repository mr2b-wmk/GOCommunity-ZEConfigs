import re
import os
import shutil

header = "\""
Tail = "\"\n{\n\t\t\"default\"\t\t\t\t\" \"\n\t\t\"print\"\t\t\t\t\"hud\"\n\t\t\"timer\"\t\t\t\t\"0\"\n\t\t\"timercover\"\t\t\t\t\"0\" \n\t\t\"timertip\"\t\t\t\t\"倒计时 {time} 秒\"\n\t\t\"timerend\"\t\t\" \"\n\t\t\"mulithud\"\t\t\t\t\"1\" \n\t\t\"taskhud\"\t\t\t\t\"0\"\n\t\t\"taskmessage\"\t\t\t\t\" \"\n}\n"

##rename
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
def remove_duplicates_and_save(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_f:
        lines = input_f.readlines()

    # Remove duplicates using a set
    unique_lines = set(lines)

    # Write the unique lines to the output file
    with open(output_file, 'w', encoding='utf-8') as output_f:
        output_f.writelines(unique_lines)

##格式化
def text_formatted(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            processed_line = header + line.strip() + Tail
            f.write(processed_line)
###############################################################################################################################

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
if __name__ == '__main__':
    input_file = '2text.txt'  # Replace with your final output file name
    output_file = '3text_deduplicated.txt'  # Replace with your new output file name

    remove_duplicates_and_save(input_file, output_file)

##格式化

if __name__ == "__main__":
    input_filename = "3text_deduplicated.txt"
    output_filename = "4text_formatted.cfg"

    text_formatted(input_filename, output_filename)
    print("文件处理完成！")