#!/usr/bin/env python

# Copyright 2017-2018 Biomedical Imaging Group Rotterdam, Departments of
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

import configparser


def load_config(config_file_path):
    """ Parse a segmentix configuration file.

    Arguments:
        config_file_path: path to the configuration file to be parsed.

    Returns:
        settings_dict: dictionary containing all parsed settings.
    """

    settings = configparser.ConfigParser()
    settings.read(config_file_path)

    settings_dict = {'Segmentix': dict()}

    # Segmentation settings
    settings_dict['Sementix'] = dict()
    settings_dict['Segmentix']['type'] =\
        str(settings['Segmentix']['segtype'])

    settings_dict['Segmentix']['mask'] =\
        str(settings['Segmentix']['mask'])

    settings_dict['Segmentix']['radius'] =\
        int(settings['Segmentix']['segradius'])

    settings_dict['Segmentix']['N_blobs'] =\
        int(settings['Segmentix']['N_blobs'])

    settings_dict['Segmentix']['fillholes'] =\
        settings['Segmentix'].getboolean('fillholes')

    return settings_dict
