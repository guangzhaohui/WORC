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
    """ Parse a WORC configuration file.

    Arguments:
        config_file_path: path to the configuration file to be parsed.

    Returns:
        settings_dict: dictionary containing all parsed settings.
    """

    settings = configparser.ConfigParser()
    settings.read(config_file_path)

    settings_dict = {'ImageFeatures': dict(), 'General': dict(),
                     'SVMFeatures': dict()}

    settings_dict['ImageFeatures']['image_type'] =\
        [str(item).strip() for item in
         settings['ImageFeatures']['image_type'].split(',')]

    settings_dict['General']['patientclass'] =\
        str(settings['General']['patientclass'])

    settings_dict['General']['FeatureCalculator'] =\
        str(settings['General']['FeatureCalculator'])

    settings_dict['General']['PCE'] =\
        settings['General'].getboolean('PCE')

    settings_dict['General']['Segmentix'] =\
        settings['General'].getboolean('Segmentix')

    # settings_dict['General']['gridsearch_SVM'] =\
    #     str(settings['General']['gridsearch_SVM'])

    # for key in settings['SVMFeatures'].keys():
    #     settings_dict['SVMFeatures'][key] =\
    #         [str(item).strip() for item in
    #          settings['SVMFeatures'][key].split(',')]

    return settings_dict
