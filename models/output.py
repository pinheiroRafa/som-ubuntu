import os

class Output:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    # Converte as saidas em string
    @staticmethod
    def allToString(outputs):
        names = []
        for index in range(len(outputs)):
            names.append(outputs[index].name)
        return '\n'.join(names)

    # Busca todas as saidas
    @staticmethod
    def search(): 
        test = os.popen("pactl list sinks").read()
        arr = test.split("#")
        outputs = []
        
        for index in range(len(arr)):
            output = arr[index]
            lines = output.split("\t")
            if(len(lines) > 3 and lines[3] != ''):
                name = str(len(outputs) + 1) + " - " + (lines[3].split(":")[1].replace("\n","").strip())
                id = lines[2].split(":")[1].replace("\n","").strip()
                outputs.append(Output(name, id))
        
        return outputs
    # Seta a saida no sistema operacional
    def setSelected(self):
        os.system("pactl set-default-sink "+self.id)