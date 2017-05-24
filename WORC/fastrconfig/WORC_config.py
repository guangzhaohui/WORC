#!/usr/bin/env python

# Copyright 2011-2017 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import site
import os


# Add the WORC FASTR tools and type paths
packagedir = site.getsitepackages()[0]
tools_path = [os.path.join(packagedir, 'WORC', 'resources', 'fastr_tools')] + tools_path
types_path = [os.path.join(packagedir, 'WORC', 'resources', 'fastr_types')] + types_path

# Mounts accessible to fastr virtual file system
mounts['worc_example_data'] = os.path.join(packagedir, 'WORC', 'exampledata')
mounts['apps'] = os.path.expanduser(os.path.join('~', 'apps'))
mounts['output'] = os.path.expanduser(os.path.join('~', 'WORC', 'output'))
mounts['test'] = os.path.join(packagedir, 'WORC', 'resources', 'fastr_tests')