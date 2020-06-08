from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#OAuth認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

def main():

    folder_id = drive.ListFile({'q': "title = 'new_folder'"}).GetList()[0]['id']
    # folder_id = '1frM-1rRC8NiAb_zehuWCLREkfqmYGDK3'

    file_list = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(folder_id)}).GetList()

    for f in file_list:
        print(f['title'],' \t',f['id'])


if __name__ == "__main__":
    main()

    # def get_list(parent_id, l=None):
    #     if l is None:
    #         l = []

    #     file_list = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(folder_id)}).GetList()
    #     l += file_list

    #     for f in file_list:
    #         if f['mimeType'] == 'applicatoin/vnd.google-apps.folder':
    #             get_list_recursively(f['id'],l)

    #     return l


    # folder_id = drive.ListFile({'q': "title = 'new_folder'"}).GetList()[0]['id']

    # for f in get_list(folder_id):
    #     print(f['title'],' \t', f['id'])
