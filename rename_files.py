import csv
import os
import logging

# Prompt the user for the folder path
folder_path = input("フォルダのpathを入れてね。: ")

# Set up logging
logging.basicConfig(filename='renaming_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s', filemode='w')

with open(folder_path + '/' + 'ReadMe.csv', 'r', encoding='cp932') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i < 3:
            continue  # skip the first 4 lines
        if len(row) < 2:
            continue  # skip rows that don't have enough columns
        try:
            old_name = row[2]  # assumes the file names are in the first column of the CSV file
            new_name = row[1]  # assumes the new names are in the second column of the CSV file
            _, ext = os.path.splitext(old_name)
            new_name_with_ext = new_name + ext
            old_path = os.path.join(folder_path + '/', old_name)
            new_path = os.path.join(folder_path + '/', new_name_with_ext)
            try:
                os.rename(old_path, new_path)
                logging.info(f'名前を {old_name} から {new_name_with_ext}へ変更したよ。')
            except FileNotFoundError:
                logging.warning(f'ファイルが見つからないよ。: {old_name}')
        except UnicodeDecodeError:
            continue  # skip rows that contain non-UTF-8 characters
print("できました！授業がんばってね＾＾")
