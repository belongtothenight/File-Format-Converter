import PySimpleGUI as sg

class Layout:
    def __init__(self, cl, Converter_check):
        self.cl = cl
        self.Converter_check = Converter_check
    
    # Menu Layout
    def menu_layout(self):
        menu_def = [
            ['Function List', [self.cl[0], self.cl[1], self.cl[2], self.cl[3], self.cl[4], self.cl[5]]],
            ['Help', ['Github README.md']]
        ]
        right_click_menu_def = [[], ['Help', ['Github README.md'], 'Exit']]
        return menu_def, right_click_menu_def

    # Single Conversion Layout
    def single_convertion_layout(self):
        col_1 = [
            [sg.Text('Files in'), sg.Radio('Source Folder', "RadioDemo", default=True, size=(10,1), k='-R1-', enable_events=True), sg.Radio('Export Folder', "RadioDemo", default=True, size=(10,1), k='-R2-', enable_events=True)],
            [sg.Listbox(values=[], enable_events=True, size=(40, 40), key='-LISTBOX-')]
        ]

        col_2 = [
            [sg.Text('Click documents on the left to preview. Support format: .txt .csv .md', size=(60,1))],
            [sg.MLine(key='-ML-'+sg.WRITE_ONLY_KEY,  size=(85,42))]
        ]

        single_conversion_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-')], 
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Export Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-')], 
            [sg.Text('Select Converter'), sg.OptionMenu(values=(self.cl[0], self.cl[1], self.cl[2], self.cl[3], self.cl[4], self.cl[5]),  key='-OPTION MENU-'), sg.Button('Select', enable_events=True, key='-CONVERTER-'), sg.Text(self.Converter_check , size=(36,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.Txt(size=(25,1), key='-OUTPUT0-')],
            [sg.HSeparator()],
            [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
        ]
        return single_conversion_layout

    # Bulk to Bulk Conversion Layout

    # File Merge Layout

    '''
    # Rename Layout
    @staticmethod
    def rename_layout():
        rename_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(key='-INPUT-')], 
            [sg.Text('Export File'), sg.OptionMenu(values=('None', 'CSV', 'EXCEL'),  key='-OPTION MENU-'), sg.Text('Initial Filename Number'), sg.Input(key='-INPUT-')],
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Button('Confirm and Rename'), sg.Text('View'), sg.OptionMenu(values=('Source Folder', 'Export Folder'),  k='-OPTION MENU-')],
            [sg.HSeparator()],
            [sg.Listbox(values=[], enable_events=True, size=(135, 42), key='-LISTBOX-1')]
        ]
        return rename_layout
    '''

    # Execution Log Layout
    @staticmethod
    def execution_log_layout():
        execution_log_layout = [
            [sg.Text("Log")],
            [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
        ]
        return execution_log_layout

    # Instructions Layout
    @staticmethod
    def instruction_layout():
        instruction_layout = [
            [sg.Text('Instructions for using this program are in this tab!')]
        ]
        return instruction_layout

    # About Layout
    @staticmethod
    def about_layout():
        about_layout = [
            [sg.Text('About this program is in this tab!')]
        ]
        return about_layout

    # Layout of the whole window
    @staticmethod
    def layout(menu_def, single_conversion_layout, execution_log_layout, instruction_layout, about_layout):
        layout = [
            [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)]
        ]

        layout +=[[sg.TabGroup([[
            sg.Tab('Single Conversion', single_conversion_layout),
            sg.Tab('Execution Log', execution_log_layout),
            sg.Tab('Instructions', instruction_layout),
            sg.Tab('About', about_layout)
            ]], key='-TAB GROUP-', expand_x=True, expand_y=True)
        ]]
        return layout


if __name__ == '__main__':
    print("This is GUI layout file, not main.")