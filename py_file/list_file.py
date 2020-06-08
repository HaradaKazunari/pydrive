from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#OAuth認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

def get_list(parent_id,l=None):

    if l is None:
        l = []

    folder_id = drive.ListFile({'q': "title = 'new_folder'"}).GetList()[0]['id']
    l += file_list

    for f in file_list:
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            get_list(f['id'],l)

    return l

# def main():

#いままでアップしたファイルの取得
# file_list = drive.ListFile().GetList()
# for f in file_list:
#     print(f['title'], f['id'])

if __name__ == "__main__":
    # main()
    for f in get_list(forlder_id):
        print(f['title'],' \t', f['id'])
