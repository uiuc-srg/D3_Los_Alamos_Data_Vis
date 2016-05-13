output_file = open('auth_data.txt', 'w')
data_file = open('data_files_aa', 'r')
for line in data_file:
    line_data = line.split(',')
    output_file.write(line_data[1] + ',' + line_data[2] + ',' + line_data[3] + ',' + line_data[4] + '\n')
data_file.close()