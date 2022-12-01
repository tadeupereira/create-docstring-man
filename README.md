# __Create Docstring Manual__
```python
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
```
## *create_docstring_man.py*
```python
Module to generate the "docstring_man.md" file based on
the project's "docstrings".
```
### SUBROUTINE: genName
```python
Author: Tadeu Pereira
Creation: 07/10/2022

Auxiliary subroutine responsible for replacing the names of packages, 
modules, subroutines, classes and methods by the double underscore ( __ ), 
as this is a character pattern of the "markdown language".
```
### SUBROUTINE: genPython
```python
Author: Tadeu Pereira
Creation: 07/10/2022

Auxiliary subroutine responsible for generating blocks of code in the "Python" pattern.
```
### SUBROUTINE: create
```python
Author: Tadeu Pereira
Creation: 07/10/2022

Subroutine responsible for generating the "docstring_man.md" file.

    See too
    ----------
        genName(name)
        genPython(text)            
```
