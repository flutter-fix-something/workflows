# /usr/bin/env python3

import os
import sys
import yaml


script_dir = os.path.dirname(os.path.realpath(__file__))

flutter_project_dir = os.path.join(script_dir, "photo_manager_test_version")

version = sys.argv[1]

# read pubspec.yaml
pubspec_path = os.path.join(flutter_project_dir, "pubspec.yaml")
with open(pubspec_path, "r") as f:
    pubspec = yaml.load(f, Loader=yaml.FullLoader)

    # add dependency
    pubspec["dependencies"]["photo_manager"] = version

with open(pubspec_path, "w") as f:
    yaml.dump(pubspec, f)
