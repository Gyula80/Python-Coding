import PySimpleGUI as ps

label_feet = ps.Text('Enter feet:')
textbox_feet = ps.InputText('', key = 'feet')
label_inch = ps.Text('Enter inches')
textbox_inch = ps.InputText('', key = 'inch')
button = ps.Button('convert', key = 'convert')
result_label = ps.Text('',key = 'result')

window = ps.Window('Convertor', layout = [[label_feet, textbox_feet],
                                          [label_inch, textbox_inch],
                                          [button, result_label] ])

while True:
    event, values = window.read()

    match event:
        case ps.WIN_CLOSED:
            break
        case 'convert':
            in_meter = float(values['feet']) * 0.3048 + float(values['inch']) * 0.0254
            print('hello')
            window['result'].update(str(in_meter) + ' m')
            ###window['result'].update(value=f"{in_meter} m", text_color="pink")

window.close()

