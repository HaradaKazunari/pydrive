from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def main():
#OAuth認証を行う
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    file_list = drive.ListFile().GetList()
    for f in file_list:
        print(f['title'], f['id'])
    #ファイル作成
    # f = drive.CreateFile({'title':'drive_api.txt'})
    # f.SetContentString('https://news.mynavi.jp/article/zeropython-17/')
    # f.Upload()

    # print(f['title'],'up comp')

#いままでアップしたファイルの取得
# file_list = drive.ListFile().GetList()
# for f in file_list:
#     print(f['title'], f['id'])

if __name__ == "__main__":
    main()
