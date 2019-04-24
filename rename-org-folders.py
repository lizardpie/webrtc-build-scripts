import os

oldname = 'org'
newname = 'dialogicbuzz'

def renameFolder(basedir):
    oldpath = os.path.join(basedir, oldname)    
    newpath = os.path.join(basedir, newname)
    if os.path.isdir(oldpath):
        os.rename(oldpath, newpath)
        print('Path ' + oldpath + ' renamed to ' + newpath)
    else:
        print('Path not found: ' + oldpath)

renameFolder('android/webrtc/src/modules/audio_device/android/java/src')
renameFolder('android/webrtc/src/rtc_base/java/src')
renameFolder('android/webrtc/src/sdk/android/api')
renameFolder('android/webrtc/src/sdk/android/src/java')

