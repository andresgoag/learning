from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           

drive = GoogleDrive(gauth) 

gfile = drive.CreateFile({'parents': [{'id': '11n_eTNlmTE50XAqkzkAPoku0_ky5sDEk'}]})

gfile.SetContentFile('files/test.txt')
gfile.Upload()