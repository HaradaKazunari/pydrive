from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#OAuth認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

def main():
    folder_id = drive.ListFile({'q':'title = "new_folder"'}).GetList()[0]['id']
    #キャリア会を指定。（指定のフォルダのURLの最後がID
    # folder_id = '1frM-1rRC8NiAb_zehuWCLREkfqmYGDK3'
        
    f = drive.CreateFile({
        'parents': [{'id':folder_id}]
        })
    f.SetContentFile('test.jpg')
    f.Upload()
    print(f['parents'][0]['id'] == folder_id)


if __name__ == "__main__":
    main()

