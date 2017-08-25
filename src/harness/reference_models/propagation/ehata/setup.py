# Copyright 2017 SAS Project Authors. All Rights Reserved.
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

# To install the module, run 'python setup.py build_ext -i' to install
# into the local directory. Run 'python setup.py build' to build the
# module. See distutils documentation for more info.

from distutils.core import Extension, setup

ehata_module = Extension('ehata_its',
                         sources = ['its/ExtendedHata.cpp',
                                    'its/FindHorizons.cpp',
                                    'its/FindQuantile.cpp',
                                    'its/FineRollingHillyTerrainCorectionFactor.cpp',
                                    'its/GeneralSlopeCorrectionFactor.cpp',
                                    'its/IsolatedRidgeCorrectionFactor.cpp',
                                    'its/LeastSquares.cpp',
                                    'its/MedianBasicPropLoss.cpp',
                                    'its/MedianRollingHillyTerrainCorrectionFactor.cpp',
                                    'its/MixedPathCorrectionFactor.cpp',
                                    'its/PreprocessTerrainPath.cpp',
                                    'ehata_its_py.cpp'])

setup(name = 'ehata_its',
      version = '1.0',
      description = 'ITS eHata propagation model',
      ext_modules = [ehata_module])
