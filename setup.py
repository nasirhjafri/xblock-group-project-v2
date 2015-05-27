# -*- coding: utf-8 -*-

# Imports ###########################################################

import os
from setuptools import setup


# Functions #########################################################

def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


# Main ##############################################################

setup(
    name='xblock-group-project-v2',
    version='0.1',
    description='XBlock - Group Project V2',
    packages=['group_project_v2'],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': 'group-project-v2 = group_project_v2:GroupActivityXBlock',
    },
    package_data=package_data("group_project_v2", ["static", "templates", "public", "res"]),
)
