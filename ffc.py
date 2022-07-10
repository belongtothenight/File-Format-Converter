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
    guic = gl.Layout(fl, converter_check)
    menu_def, right_click_menu_def = guic.menu_layout()
    single_conversion_layout = guic.single_convertion_layout()
    # Bulk to Bulk Conversion Layout
    # File Merge Layout
    execution_log_layout = guic.execution_log_layout()
    instruction_layout = guic.instruction_layout()
    about_layout = guic.about_layout()
    layout = guic.layout(menu_def, single_conversion_layout, execution_log_layout, instruction_layout, about_layout)
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('File Format Converter', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=False)
    window.set_min_size(window.size)
    return window

# PysimpleGUI Window Event Handler
def main():
    window = make_window(sg.theme())
    
    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)
        ehfc = ehf.Event_Handler_Function(fl, hl, window, event, values)
        
        # calculations

        # Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            ehfc.execution_log_update()
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        elif event in fl or event in hl:
            ehfc.menu_event()
        elif event == '-FOLDER-':
            source_folder, source_folder_list = ehfc.single_conversion_source_folder()
        elif event == '-INPUT-':
            source_filename = ehfc.single_conversion_source_filename()
        elif event == '-FOLDER-0':
            export_folder, export_folder_list = ehfc.single_conversion_export_folder()
        elif event == '-INPUT-2':
            export_filename = ehfc.single_conversion_export_filename()
        elif event == '-CONVERTER-':
            converter, converter_check = ehfc.single_conversion_converter(source_filename, export_filename, source_folder_list)
        elif event == 'Convert and Export':
            #ehfc.single_conversion_convert_and_export(converter, source_folder, export_folder, source_filename, export_filename)
            # Error detectinon is bugged.
            ehfc.single_conversion_convert_and_export_check(converter, converter_check, source_folder, export_folder, source_filename, export_filename)
        elif event == '-R1-':
            ehfc.single_conversion_view_source_folder(source_folder)
        elif event == '-R2-':
            ehfc.single_conversion_view_export_folder(export_folder)
        elif event == '-LISTBOX-':
            ehfc.single_conversion_file_preview(source_folder, export_folder)

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
    fl = ['MD to CSV', 'CSV to MD', 'XML to CSV', 'CSV to Parquet', 'Parquet to CSV', 'File Rename']

    # Help List
    hl = ['Github README.md']

    # Start GUI
    sg.theme('lightgrey1')
    main()