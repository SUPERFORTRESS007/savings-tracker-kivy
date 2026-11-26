8[app]

# (str) Title of your application
title = Savings Tracker

# (str) Package name
package.name = savingstracker

# (str) Package domain (needed for android packaging)
package.domain = org.savingstracker

# (str) Source files to include (let it find python files, json data, and the icon)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source files to include (let it include your data folder/files explicitly)
source.include_patterns = assets/*.png, images/*.png, quotes.json, icon.png

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Add android, pyjnius, kivy, and python3 dependencies here
requirements = python3,kivy,plyer

# (list) Custom source folders for python modules
source.include_dir =

# (str) Supported orientations
orientation = portrait

# (list) List of services to declare
#services =

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash of the application
#presplash.filename = %(source.dir)s/presplash.png

# (string) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (list) Supported orientations
#full_orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.target = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use Android X
android.androidx = True

# (list) Gradle dependencies
#android.gradle_dependencies =

# (str) python-for-android branch to use
#p4a.branch = master

# (str) Ouput format [apk, aar, aar-bundle]
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
