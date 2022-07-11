# Import custom modules
import gui_layout as gl
import event_handler_function as ehf
# Import Package
import PySimpleGUI as sg
# prevent exe error
import sys

'''
Links
    https://github.com/PySimpleGUI
    https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_All_Elements.py
    https://pysimplegui.readthedocs.io/en/latest/cookbook/#keys_1
    https://www.youtube.com/watch?v=-_z2RPAH0Qk
    https://www.youtube.com/watch?v=n6qzrBPkPqw
    https://stackoverflow.com/questions/66079632/python-should-gui-be-in-separate-file-confused
    https://github.com/PySimpleGUI/PySimpleGUI/issues/5139
    https://docs.python-guide.org/writing/structure/
    https://www.youtube.com/watch?v=35yYObtZ95o
'''

# Function


# PysimpleGUI Window Layout
def make_window(theme):
    sg.theme(theme)
    guic = gl.Layout(cl_single_conversion, cl_bulk_to_bulk_conversion, cl_file_merge, converter_check)
    menu_def, right_click_menu_def = guic.menu_layout()
    single_conversion_layout = guic.single_convertion_layout()
    bulk_to_bulk_conversion_layout = guic.bulk_to_bulk_conversion_layout()
    file_merge_layout = guic.file_merge_layout()
    execution_log_layout = guic.execution_log_layout()
    instruction_layout = guic.instruction_layout()
    about_layout = guic.about_layout()
    layout = guic.layout(
        menu_def,
        single_conversion_layout,
        bulk_to_bulk_conversion_layout,
        file_merge_layout,
        execution_log_layout,
        instruction_layout,
        about_layout
        )
    window = guic.window_layout(layout, right_click_menu_def)
    return window

# PysimpleGUI Window Event Handler
def main():
    window = make_window(sg.theme())
    
    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)
        ehfc = ehf.Event_Handler_Function(cl_single_conversion, cl_bulk_to_bulk_conversion, cl_file_merge, hl, window, event, values)
        
        # calculations

        # General Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            ehfc.execution_log_update()
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        elif event in (cl_single_conversion + cl_bulk_to_bulk_conversion + cl_file_merge + hl):
            ehfc.menu_event()

        # Common Event Handling
        elif event == '-FOLDER-':
            source_folder, source_folder_list = ehfc.conversion_source_folder()
        elif event == '-INPUT-':
            source_filename = ehfc.conversion_source_filename()
        elif event == '-FOLDER-0':
            export_folder, export_folder_list = ehfc.conversion_export_folder()
        elif event == '-INPUT-0':
            export_filename = ehfc.conversion_export_filename()

        # Single Conversion Event Handling
        elif event == '-CONVERTER-':
            converter, converter_check = ehfc.single_conversion_converter(source_filename, export_filename, source_folder_list)
        elif event == 'Convert and Export':
            ehfc.single_conversion_convert_and_export_check(converter, converter_check, source_folder, export_folder, source_filename, export_filename)
        elif event == '-R1-':
            ehfc.single_conversion_view_source_folder(source_folder)
        elif event == '-R2-':
            ehfc.single_conversion_view_export_folder(export_folder)
        elif event == '-LISTBOX-':
            ehfc.single_conversion_file_preview(source_folder, export_folder)

        # Bulk to Bulk Conversion Event Handling
        elif event == '-CONVERTER-0':
            # new_filename_initial_number_layout_update()
            print("[LOG] Select Bulk to Bulk Conversion => " + values['-OPTION MENU-0'])
            if values['-OPTION MENU-0'] == cl_bulk_to_bulk_conversion[5]:
                window['-TXT-'].update(text_color='black')
                window['-INPUT-2'].update(disabled=False)
            else:
                window['-TXT-'].update(text_color='grey')
                window['-INPUT-2'].update(disabled=True)
            # source_filetype_exist_check()
        elif event == '-CE-':
            print("[LOG] Select Bulk to Bulk Conversion and Export")
            # bulk_to_bulk_conversion_converter_check()
            # bulk_to_bulk_conversion_convert_and_export()
            print(values['-INPUT-1'])
        
            

        # File Merge Event Handling

    window.close()
    sys.exit(0)

if __name__ == '__main__':
    # Variables Initialization
    source_folder = ''
    source_filename = ''
    source_folder_list = []
    export_folder = ''
    export_filename = ''
    export_folder_list = []
    converter = ''
    converter_check = ''
    final_status = ''

    # Converter Function List
    cl_single_conversion = ['MD to CSV', 'CSV to MD', 'XML to CSV', 'CSV to Parquet', 'Parquet to CSV', 'File Rename']
    cl_bulk_to_bulk_conversion = ['MDs to CSVs', 'CSVs to MDs', 'XMLs to CSVs', 'CSVs to Parquets', 'Parquets to CSVs', 'Files Rename']
    cl_file_merge = ['CSV', 'Parquet', 'MD', 'XMLs to CSV']

    # Help List
    hl = ['Github README.md']

    # Start GUI
    sg.theme('lightgrey1')
    main()