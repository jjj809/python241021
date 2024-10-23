import os
import shutil
import glob

# 다운로드 폴더 경로 설정
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로 설정
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더가 없으면 생성하는 함수
def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# 각 폴더 생성
create_folder_if_not_exists(image_folder)
create_folder_if_not_exists(data_folder)
create_folder_if_not_exists(docs_folder)
create_folder_if_not_exists(archive_folder)

# 파일을 이동하는 함수
def move_files(pattern, destination_folder):
    for file in glob.glob(pattern):
        try:
            shutil.move(file, destination_folder)
            print(f'Moved: {file} -> {destination_folder}')
        except Exception as e:
            print(f'Error moving {file}: {e}')

# 이미지 파일 이동 (*.jpg, *.jpeg)
move_files(os.path.join(download_folder, '*.jpg'), image_folder)
move_files(os.path.join(download_folder, '*.jpeg'), image_folder)

# 데이터 파일 이동 (*.csv, *.xlsx)
move_files(os.path.join(download_folder, '*.csv'), data_folder)
move_files(os.path.join(download_folder, '*.xlsx'), data_folder)

# 문서 파일 이동 (*.txt, *.doc, *.pdf)
move_files(os.path.join(download_folder, '*.txt'), docs_folder)
move_files(os.path.join(download_folder, '*.doc'), docs_folder)
move_files(os.path.join(download_folder, '*.pdf'), docs_folder)

# 압축 파일 이동 (*.zip)
move_files(os.path.join(download_folder, '*.zip'), archive_folder)

print("File sorting complete.")
