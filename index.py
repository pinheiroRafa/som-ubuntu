from tkinter import Tk
from tkinter.simpledialog import askstring
from models.output import Output




root = Tk()
root.withdraw() # hide main window

#Lista todas as saídas disponíveis
outputs = Output.search()

text = askstring(
    title = "Qual saída você deseja usar?", 
    prompt = "\n"+Output.allToString(outputs)+"\n",
    initialvalue = str(len(outputs))
    )

outputs[(int(text)-1)].setSelected()