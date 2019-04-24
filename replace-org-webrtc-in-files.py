import os, fnmatch

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

findReplace("android/webrtc/src/modules/audio_device", "org.webrtc", "dialogicbuzz.webrtc", "*.gn")

findReplace("android/webrtc/src/modules/audio_device", "org/webrtc", "dialogicbuzz/webrtc", "*.gn")

findReplace("android/webrtc/src/modules/audio_device/android/java/src/dialogicbuzz/webrtc/voiceengine", "org.webrtc", "dialogicbuzz.webrtc", "*.java")

findReplace("android/webrtc/src/modules/audio_device/android/java/src/dialogicbuzz/webrtc/voiceengine", "org/webrtc", "dialogicbuzz/webrtc", "*.java")

# rtc_base

findReplace("android/webrtc/src/rtc_base", "org.webrtc", "dialogicbuzz.webrtc", "*.gn")

findReplace("android/webrtc/src/rtc_base", "org/webrtc", "dialogicbuzz/webrtc", "*.gn")

findReplace("android/webrtc/src/rtc_base/java/src/dialogicbuzz/webrtc", "org.webrtc", "dialogicbuzz.webrtc", "*.java")

findReplace("android/webrtc/src/rtc_base/java/src/dialogicbuzz/webrtc", "org/webrtc", "dialogicbuzz/webrtc", "*.java")

# sdk/android

findReplace("android/webrtc/src/sdk/android", "org.webrtc", "dialogicbuzz.webrtc", "AndroidManifest.xml")

findReplace("android/webrtc/src/sdk/android", "org/webrtc", "dialogicbuzz/webrtc", "AndroidManifest.xml")

findReplace("android/webrtc/src/sdk/android", "org.webrtc", "dialogicbuzz.webrtc", "*.gn")

findReplace("android/webrtc/src/sdk/android", "org/webrtc", "dialogicbuzz/webrtc", "*.gn")

findReplace("android/webrtc/src/sdk/android/api/dialogicbuzz/webrtc", "org.webrtc", "dialogicbuzz.webrtc", "*.java")

findReplace("android/webrtc/src/sdk/android/api/dialogicbuzz/webrtc", "org/webrtc", "dialogicbuzz/webrtc", "*.java")

findReplace("android/webrtc/src/sdk/android/src/java/dialogicbuzz/webrtc", "org.webrtc", "dialogicbuzz.webrtc", "*.java")

findReplace("android/webrtc/src/sdk/android/src/java/dialogicbuzz/webrtc", "org/webrtc", "dialogicbuzz/webrtc", "*.java")

findReplace("android/webrtc/src/sdk/android/src/jni", "org_webrtc_", "dialogicbuzz_webrtc_", "*.h")

findReplace("android/webrtc/src/sdk/android/src/jni", "org_webrtc_", "dialogicbuzz_webrtc_", "*.cc")

# examples/androidapp

findReplace("android/webrtc/src/examples/androidapp/src/org/appspot/apprtc", "org.webrtc", "dialogicbuzz.webrtc", "*.java")




