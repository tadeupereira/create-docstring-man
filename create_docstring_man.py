# MIT License
#
# Copyright (c) 2022 Tadeu Pereira
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
Module to generate the "docstring_man.md" file based on
the project's "docstrings".
'''

import ast
import os
from datetime import datetime, timezone

def genName(name):
    '''
    Author: Tadeu Pereira
    Creation: 07/10/2022

    Auxiliary subroutine responsible for replacing the names of packages, 
    modules, subroutines, classes and methods by the double underscore ( __ ), 
    as this is a character pattern of the "markdown language".
    '''

    return name.replace('__', '\_\_')


def genPython(text):
    '''
    Author: Tadeu Pereira
    Creation: 07/10/2022

    Auxiliary subroutine responsible for generating blocks of code in the "Python" pattern.
    '''

    return '```python\n' + text + '\n```\n'


def create():
    '''
    Author: Tadeu Pereira
    Creation: 07/10/2022

    Subroutine responsible for generating the "docstring_man.md" file.

        See too
        ----------
            genName(name)
            genPython(text)            
    '''

    file_write = open("docstring_man.md", "w")

    file_write.write('# __Developer manual__\n')
    file_write.write(genPython('This document was automatically generated based on the "docstrings" of project.\n' +
                                'It is your duty as a developer to keep the the "docstrings" of project up to date.'))

    # Processing all directories and files
    ttl_package = 0
    ttl_module = 0
    ttl_def = 0
    ttl_class = 0
    ttl_method = 0
    ttl_except = 0
    count_package = 0
    count_module = 0
    for current_directory, directories, files in sorted(os.walk('.'), key=lambda a: (a[0].lower(), a[1])):
        
        # Processing files in current directory
        for file in sorted(files, key=str.lower):

            if file == __file__:
                continue

            # Processing the current file
            if file[-3:].lower() == '.py':
                file_full_name = f'{current_directory}/{file}'
                file_read = open(file_full_name, 'r')
                module_def = ast.parse(file_read.read())
                file_read.close()

                file_full_name = genName(file_full_name)

                # Processing the package/module
                package = file == '__init__.py'
                if package:
                    ttl_package += 1
                    count_module = 0
                    count_package += 1
                    package_title = f'__{count_package}. PACKAGE: {current_directory}/__'
                    file_write.write(f'***\n## {package_title}\n')
                else:
                    ttl_module += 1
                    count_def_class = 0
                    count_module += 1
                    module_title = f'*{count_package}.{count_module}. MODULE: {file_full_name}*'
                    file_write.write(f'## {module_title}\n')
                
                try:
                    # Getting docstring from package/module
                    file_write.write(genPython(''.join(ast.get_docstring(module_def).splitlines(True))))

                    # Getting all subroutines from the package/module
                    function_definitions = [node for node in module_def.body if isinstance(node, ast.FunctionDef)]
                    for function_def in function_definitions:
                        # Processing the subroutine
                        ttl_def += 1
                        count_def_class += 1
                        function_title = f'{count_package}.{count_module}.{count_def_class}. SUBROUTINE: {genName(function_def.name)}'
                        file_write.write(f'### {function_title}' + '\n')
                        # Getting docstring from subroutine
                        file_write.write(genPython(''.join(ast.get_docstring(function_def).splitlines(True))))


                    # Getting all classes from package/module
                    class_definitions = [node for node in module_def.body if isinstance(node, ast.ClassDef)]
                    method_definitions = []
                    for class_def in class_definitions:
                        # Processing the class
                        ttl_class += 1
                        count_method = 0
                        count_def_class += 1
                        class_title = f'{count_package}.{count_module}.{count_def_class}. CLASS: {genName(class_def.name)}'
                        file_write.write(f'### {class_title}' + '\n')
                        # Getting the class documentation
                        file_write.write(genPython(''.join(ast.get_docstring(class_def).splitlines(True))))

                        
                        # Getting all class methods
                        method_definitions = [node for node in class_def.body if isinstance(node, ast.FunctionDef)]
                        for method_def in method_definitions:
                            # Processing method
                            ttl_method += 1
                            count_method += 1
                            method_title = f'{count_package}.{count_module}.{count_def_class}.{count_method}. METHOD ({genName(class_def.name)}): {genName(method_def.name)}'
                            file_write.write(f'#### {method_title}' + '\n')
                            # Getting docstring from method
                            file_write.write(genPython(''.join(ast.get_docstring(method_def).splitlines(True))))
                except:
                    ttl_except += 1
                    file_write.write(genPython('\nREAD FAILURE\n' * 3))

    file_write.write(f'***\n## __Data about the document__\n')
    file_write.write('```bash\n')
    file_write.write(f'- Total of packages          : {ttl_package:4}\n')
    file_write.write(f'- Total of modules           : {ttl_module:4}\n')
    file_write.write(f'- Total of subroutines       : {ttl_def:4}\n')
    file_write.write(f'- Total of classes           : {ttl_class:4}\n')
    file_write.write(f'- Total of methods           : {ttl_method:4}\n')
    file_write.write(f'- Total of read failures     : {ttl_except:4}\n')
    file_write.write( '- Generation date and time   : ' + datetime.now(timezone.utc).astimezone().isoformat(timespec='minutes'))
    file_write.write('\n```')
    file_write.close()


if __name__ == '__main__':
    create()
