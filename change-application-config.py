# /usr/bin/env python3

import os

script_dir = os.path.dirname(os.path.realpath(__file__))
flutter_project_dir = os.path.join(script_dir, "photo_manager_test_version")

android_path = os.path.join(flutter_project_dir, "android")


# change wrapper version
print("change wrapper version to 7.5.1")
gradle_path = os.path.join(
    android_path, "gradle", "wrapper", "gradle-wrapper.properties"
)

with open(gradle_path, "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith("distributionUrl"):
            lines[
                i
            ] = "distributionUrl=https\\://services.gradle.org/distributions/gradle-7.5-all.zip\n"

with open(gradle_path, "w") as f:
    f.writelines(lines)

# change build.gradle AGP version and kotlin version
print("change build.gradle AGP version to 7.3.0, and change kotlin version to 1.7.10")

build_gradle_path = os.path.join(android_path, "build.gradle")
with open(build_gradle_path, "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith("classpath") and "com.android.tools.build" in line:
            lines[i] = "        classpath 'com.android.tools.build:gradle:7.3.0'\n"
        elif line.strip().startswith("ext.kotlin_version"):
            lines[i] = "    ext.kotlin_version = '1.7.10'\n"

with open(build_gradle_path, "w") as f:
    f.writelines(lines)

# change compileSdkVersion
print("change compileSdkVersion to 34")

app_build_gradle_path = os.path.join(android_path, "app", "build.gradle")
with open(app_build_gradle_path, "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith("compileSdkVersion"):
            lines[i] = "    compileSdkVersion 34\n"

with open(app_build_gradle_path, "w") as f:
    f.writelines(lines)

print("Change success!")
