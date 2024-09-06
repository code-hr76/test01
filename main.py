from nicegui import ui

t1=ui.input(label='enter value')
b1=ui.button('BUTTON', on_click=lambda: lab.set_text( t1.value ) )
lab=ui.label('Hello NiceGUI!')

ui.run()