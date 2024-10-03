def few_files_in_one(file_names, result_file):
    files_info = []

    for file_name in file_names:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            files_info.append((file_name, line_count, lines))

    files_info.sort(key=lambda x: x[1])

    with open(result_file, 'w', encoding='utf-8') as result:
        for filename, line_count, lines in files_info:
            result.write(f"{filename}\n")
            result.write(f"{line_count}\n")
            result.writelines(lines)
            result.write('\n')

    print (f'Файлы успешно объединены в {result_file}.')

files_name = ['1.txt', '2.txt', '3.txt']
few_files_in_one(files_name, 'result.txt')