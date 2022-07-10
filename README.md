# File Format Converter for Data Manipulation and AI Training

## NOTICE: THIS REPO IS UNDER DEVELOPMENT

## Functionality
- GUI
    - [ ] 1. Functionality selecting GUI.
- Main Function
    - [x] 1. md to csv
    - [x] 2. csv to md
    - [x] 3. xml to csv (labelimg)
    - [x] 4. bulk file rename
    - [ ] 5. csv to parquet (dtype, compress format)
    - [ ] 6. parquet to csv (partial read)
- Sub Function
    - [x] 1. select folder path
    - [x] 2. select file
    - [x] 3. user input
    - [ ] 4. list all files

## Developing Environment
- Windows 11
- Python 3.10.4
    - xml.etree.ElementTree
    - pandas
    - numpy
    - os
    - glob
    - tkinter
    - subprocess
    - pathlib
    - pyarrow

## File Structure and Description
- .github/ISSUE_TEMPLATE
  - bug_report.md
  - custom.md
  - feature_request.md
- test_file: Containing used files and those exported by these functions.
  - jpb: File for renaming.
  - xml: File for renaming.
  - file_list_basic.csv: File generated from md to csv function.
  - file_list_basic.md: File generated from csv to md function.
  - file_list.csv: File generated from bulk file rename function.
  - file_list.xlsx: File generated from bulk file rename function.
- .gitignore: File types not included in this repo.
- CONTRIBUTING.md: What to do if you want to contribute.
- LICENSE: MIT license detail.
- README.md: Introduction to this repo.
- converter_functions.yp: Store all the functions beside GUI.
- ffc.exe: Executable version of ffc.py.
- ffc.py: GUI and function execution.
- python_library_requirement.txt: List of python library can be used to install them. "$ pip install -r python_library_requirement.txt"

## Troubleshoot
1. Convert and Export
   Problem: Button 'Convert and Export' in tab 'Single Conversion' doesn't work even if all names and directory are correct
   Fix: Try install python package 'pyarrow'.