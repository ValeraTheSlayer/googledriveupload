from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


def upload_file(name='filename.txt', content='content'):
    file1 = drive.CreateFile({'title': f'{name}'})
    file1.SetContentString(content)
    file1.Upload()


upload_file()
