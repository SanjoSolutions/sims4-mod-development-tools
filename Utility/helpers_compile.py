#    Copyright 2020 June Hanabi, 2023-2024 Jonas Aschenbrenner
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

import fnmatch
import os
import py_compile
from zipfile import PyZipFile, ZIP_STORED

from Utility.helpers_path import remove_file, ensure_path_created, get_rel_path, replace_extension


def compile(mod_name: str, src_dir: str, build_dir: str) -> None:
    """
    Compiles the mod python scripts into a ts4script file.

    :param mod_name: Name of the mod
    :param src_dir: Source directory of the mod files
    :param build_dir: Place to put the mod files
    :return: Nothing
    """

    ts4script_build_path = os.path.join(build_dir, mod_name + '.ts4script')

    ensure_path_created(build_dir)
    remove_file(ts4script_build_path)

    print("Building ts4script file for mod...")

    zf = PyZipFile(ts4script_build_path, mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)

    for folder, subs, files in os.walk(src_dir):
        for filename in fnmatch.filter(files, '*.py'):
            file_path_py = folder + os.sep + filename
            print(file_path_py)
            file_path_pyc = replace_extension(file_path_py, "pyc")
            rel_path_pyc = get_rel_path(file_path_pyc, src_dir)
            out_file_path = os.path.join(build_dir, rel_path_pyc)
            print('out: ' + out_file_path)
            py_compile.compile(file_path_py, out_file_path)
            zf.write(out_file_path, rel_path_pyc)
            remove_file(out_file_path)

    zf.close()

    print("Done.")
