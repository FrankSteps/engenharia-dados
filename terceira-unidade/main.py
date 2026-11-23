from tkinter import *
from PIL import ImageTk, Image

class mainInterface:
    ''' Classe que possuirá a instancia de todos os objetos presentes na tela inicial '''
    
    def __init__(self, interSQL, interNOSQL):
        self.root = Tk()
        self.root.title("UNIVERSIDADATA - Dados acadêmicos")
        self.root.geometry("1280x720")

        self.telaSQL = interSQL
        self.telaNOSQL = interNOSQL

        # Imagem da logo
        self.logo = Image.open("Image.png")
        self.logo = ImageTk.PhotoImage(self.logo.resize((300, 65)))

        # Configuração de redimensionamento
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        # -- Frames de margem --
        self.leftFrame = Frame(self.root,
                               width=300,
                               height=720)
        
        self.leftFrame.grid(column=0, row=1, sticky='sn')

        self.centralFrame = Frame(self.root,
                                  borderwidth=3,
                                  relief='sunken',
                                  width=500,
                                  height=480)
        
        self.centralFrame.grid(column=1, row=1)
        self.centralFrame.pack_propagate(False)
        
        self.rightFrame = Frame(self.root,
                                width=300,
                                height=720)

        self.rightFrame.grid(column=2, row=1, sticky='sn')

        self.invisibleFrame = Frame(self.centralFrame, height=150)
        self.invisibleFrame.pack(side='top')

        # Label para a imagem
        self.imgLabel = Label(self.centralFrame, image=self.logo)
        self.imgLabel.pack(side='top', fill="x")

        self.invisibleFrame = Frame(self.centralFrame, height=40)
        self.invisibleFrame.pack(side='top')

        # Botões
        self.buttonSQL = Button(self.centralFrame, text='SQL', height=2, command=lambda: self.sql_transition(self.telaSQL))
        self.buttonNOSQL = Button(self.centralFrame, text='NOSQL', height=2)
        
        self.buttonSQL.pack(side='top', fill='x')
        self.buttonNOSQL.pack(side='top', fill='x')



        self.root.mainloop()

    # Função de transição de janela
    def sql_transition(self, telaSql):
        self.telaSQL()
        

class PostgreInterface:
    ''' Classe para a interface de interação via postgre '''

    def __init__(self):
        pass


class NoSQLinterface:
    ''' Classe para a interface de interação com o banco não-relacional '''

    def __init__(self):
        pass


telaMain = mainInterface(PostgreInterface, NoSQLinterface)



