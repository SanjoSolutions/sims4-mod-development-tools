#    Copyright 2020 June Hanabi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import os
import sys

# Helpers
from Utility.helpers_compile import compile
sys.path.append(os.getcwd())
from settings import src_path, author_name, project_name, build_path

script_path = os.path.dirname(os.path.realpath(__file__))

try:
    compile(author_name + '_' + project_name, src_path, build_path)
except Exception as error:
    print("An error occurred!")
    print(error)
