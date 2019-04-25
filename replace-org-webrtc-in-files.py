import os, fnmatch

find_org_dot = "org.webrtc"
find_org_slash = "org/webrtc"
find_org_under = "org_webrtc_"
replace_buzz_dot = "dialogicbuzz.webrtc"
replace_buzz_slash = "dialogicbuzz/webrtc"
replace_buzz_under = "dialogicbuzz_webrtc_"

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)
                print("Saving " + filepath)

# modules/audio_device

mypath = "android/webrtc/src/modules/audio_device"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.gn")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.gn")

mypath = "android/webrtc/src/modules/audio_device/android"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.h")
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.cc")
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.java")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.h")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.cc")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.java")

# modules/audio_coding

mypath = "android/webrtc/src/modules/audio_coding/audio_network_adapter"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.proto")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.proto")

# modules/utility

mypath = "android/webrtc/src/modules/utility"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.h")
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.cc")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.h")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.cc")

# rtc_base

mypath = "android/webrtc/src/rtc_base"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.gn")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.gn")

mypath = "android/webrtc/src/rtc_base/java"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.java")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.java")

# sdk/android

mypath = "android/webrtc/src/sdk/android"
findReplace(mypath, find_org_dot, replace_buzz_dot, "AndroidManifest.xml")
findReplace(mypath, find_org_slash, replace_buzz_slash, "AndroidManifest.xml")
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.gn")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.gn")

mypath = "android/webrtc/src/sdk/android/api"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.java")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.java")

mypath = "android/webrtc/src/sdk/android/src/java"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.java")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.java")

mypath = "android/webrtc/src/sdk/android/src/jni"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.h")
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.cc")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.h")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.cc")
findReplace(mypath, find_org_under, replace_buzz_under, "*.h")
findReplace(mypath, find_org_under, replace_buzz_under, "*.cc")

# examples/androidapp

mypath = "android/webrtc/src/examples/androidapp/src"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.java")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.java")

mypath = "android/webrtc/src/examples/androidapp/res/layout"
findReplace(mypath, find_org_dot, replace_buzz_dot, "*.xml")
findReplace(mypath, find_org_slash, replace_buzz_slash, "*.xml")





