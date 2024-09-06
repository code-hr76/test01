from fastapi import FastAPI
from nicegui import ui

app = FastAPI()

t1=ui.input(label='enter value')
b1=ui.button('BUTTON', on_click=lambda: lab.set_text( t1.value ) )
lab=ui.label('Hello NiceGUI!')

ui.run_with(app, storage_secret='secret')