#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import os


def get_pytext_home():
    internal_home = os.path.realpath(os.path.join(__file__, "../../"))
    oss_home = os.path.realpath(os.path.join(__file__, "../../../"))
    default_home = ""
    # use tests as anchor which will always in PYTEXT_HOME/tests
    if os.path.exists(os.path.join(internal_home, "tests")):
        default_home = internal_home
    elif os.path.exists(os.path.join(oss_home, "tests")):
        default_home = oss_home
    else:
        # when PyText is used as a module and packed as part of a single file X
        # __file__ will be path of X instead of path.py
        # in these case, PYTEXT_HOME will be the parent folder of X
        default_home = os.path.dirname(__file__)
    pytext_home = os.environ.get("PYTEXT_HOME", default_home)
    return pytext_home


# all relateive path in PyText is based on PYTEXT_HOME
PYTEXT_HOME = get_pytext_home()


def get_absolute_path(file_path):
    return (
        file_path
        if os.path.isabs(file_path)
        else os.path.realpath(os.path.join(PYTEXT_HOME, file_path))
    )
