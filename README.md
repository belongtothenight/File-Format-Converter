# File Format Converter for Data Manipulation and AI Training

## Functionality
- GUI
    - [ ] 1. Functionality selecting GUI.
- Main Function
    - [x] 1. md to csv
    - [x] 2. csv to md
    - [x] 3. xml to csv
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

## File Structure and Description
- test_file: Containing used files and those exported by these functions.
    - jpb: File for renaming.
    - xml: File for renaming.
    - file_list_basic.csv: File generated from md to csv function.
    - file_list_basic.md: File generated from csv to md function.
    - file_list.csv: File generated from bulk file rename function.
    - file_list.xlsx: File generated from bulk file rename function.
- .gitignore: File types not included in this repo.
- LICENSE: MIT license detail.
- README.md: Introduction to this repo.
- converter_functions.yp: Store all the functions beside GUI.
- main.py: GUI.
