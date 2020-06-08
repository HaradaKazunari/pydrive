from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#OAuth認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

def main():
# make folder
    folder = drive.CreateFile({
        'title':'new_folder',
        'mimeType':'application/vnd.google-apps.folder'
        })
    folder.Upload()
    print(folder['title'],'up comp')


if __name__ == "__main__":
    main()

