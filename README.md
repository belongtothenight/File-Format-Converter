# File Format Converter for Data Manipulation and AI Training (FFC)

## NOTICE: THIS REPO IS UNDER DEVELOPMENT

## Functionality Development Process
- [ ] FFC Program
  1. [ ] Single Conversion
     1. [x] GUI Layout
     2. [x] GUI Event Handling
     3. [x] Conversion Algorithm
     4. [ ] Operation Rule
  2. [ ] Bulk to Bulk Conversion
     1. [x] GUI Layout
     2. [x] GUI Event Handling
     3. [x] Conversion Algorithm
     4. [ ] Operation Ruleerge
  3. [ ] File Merge
     1. [ ] GUI Layout
     2. [ ] GUI Event Handling
     3. [ ] Conversion Algorithm
     4. [ ] Operation Ruleerge
- [ ] Conversion Algorithm
  - [x] Single Conversion
    1. [x] MD to CSV
    2. [x] CSV to MD
    3. [x] XML to CSV
    4. [x] CSV to Parquet
    5. [x] Parquet to CSV
    6. [x] Rename
  - [x] Bulk to Bulk Conversion
    1. [x] MD to CSV
    2. [x] CSV to MD
    3. [x] XML to CSV
    4. [x] CSV to Parquet
    5. [x] Parquet to CSV
    6. [x] Rename
  - [ ] File Merge
    1. [ ] CSV
    2. [ ] Parquet
    3. [ ] MD
    4. [x] XML to CSV

*MD: Markdown files that contains only one table.
*XML: XML files generated from labelImg.

## Developing Environment
- Windows 11
- Python 3.10.4
    - numpy == 1.23.0
    - pandas == 1.4.3
    - PySimpleGUI == 4.60.1

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
1. Convert and Export: Please select converter.
   Problem: Button 'Convert and Export' in tab 'Single Conversion' doesn't work even if all names and directory are correct
   Fix: Try install python package 'pyarrow'.

## Bug
1. ListBox -> Program Freeze.
   Problem: Click on the listbox in tab 'Single Conversion' before selecting any directory will cause it to freeze.
   Status: Unsolved.
2. Window -> Always on top.
   Problem: The entire FFC window always display on top of every other windows.
   Status: Fixed.
3. Select -> Program Freeze.
   Problem: Click 'Select' in tab 'Single Conversion' before 'Export Filename' was input causing it to freeze.
   Status: Unsolved.
4. Bulk to Bulk CSV to Parquet -> Parquet file can't be previewed.
   Problem: When doing the above mentioned process, those csv files' table contains not only the numbers would result like this.
   Status: Unsolved.

## Possible Improvement
1. Rewrite the validating mechanism of the tab 'Single Conversion'.
2. Add validating mechanism to the tab 'Bulk to Bulk Conversion'.
3. Add progress bar in the tab 'Bulk to Bulk Conversion'.
4. Add multiprocessing feature to the tab 'Bulk to Bulk Conversion'.
5. Refresh window when 'Convert and Export' is processing.