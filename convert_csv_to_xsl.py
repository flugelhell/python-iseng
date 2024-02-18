import json
import os
from os.path import isfile, join
import xlsxwriter

input_folder = os.path.join(os.getcwd(),'input')
output_folder = os.path.join(os.getcwd(),'output')

if not os.path.exists(input_folder):
    os.mkdir(input_folder) 

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


count_file = 0
input_files = [f for f in os.listdir(input_folder) if isfile(join(input_folder, f))]
for file_path in filter(lambda x: '.json' in x, input_files):
    fp = os.path.join(input_folder, file_path)
    f = open (fp, 'r')
    datas = json.loads(f.read())
    
    fn = file_path.removesuffix('.json')
    file_name = os.path.join(output_folder,  fn + '.xlsx')
    header = list(datas[1].keys())
    
    if len(datas) > 0:
        count_file += 1
        print(f'writing {fn}', end=" ")
        # write xlsx
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', f'data {fn}', bold)
        worksheet.set_column(0,0,5) # set column A to 10 width
        worksheet.write_row('A3', header)
        row_count = 4
        for x in datas:
            worksheet.write_row(f'A{row_count}', x.values())
            row_count += 1

        worksheet.autofit()
        workbook.close()
        print('done')

if count_file > 0:
    print(f'writing {count_file} file, done !')

# print(input_files)