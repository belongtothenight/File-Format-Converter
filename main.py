import converter_functions as cf
import PySimpleGUI as psg

'''finished functions
cf.select_folder()
cf.convert_file()
cf.user_input()
cf.csv_to_md()
cf.xml_to_md()
cf.bulk_file_rename()
cf.md_to_csv(fp, mdfn, csvfn)
'''

layout = [
    [psg.Text('Select a folder to convert')],
    [psg.Button("OK"), psg.Button("Cancel")]
]

window = psg.Window("File Format Converter", layout)

while True:
    event, values = window.read()
    # Exit if user closes window or clicks ok
    if event == "OK" or event == psg.WIN_CLOSED:
        break

window.close()