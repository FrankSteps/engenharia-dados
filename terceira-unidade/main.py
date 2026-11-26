from tkinter import *
from PIL import ImageTk, Image

class mainInterface:
    ''' Classe que possuirá a instancia de todos os objetos presentes na tela inicial '''
    
    def __init__(self, interSQL, interNOSQL):
        self.root = Tk()
        self.root.title("UNIVERSIDADATA - Dados acadêmicos")
        self.root.geometry("1280x720")
        self.root.configure(bg='#1A1A1A')

        # Imagem da logo
        self.logo = Image.open("Image.png")
        self.logo = ImageTk.PhotoImage(self.logo.resize((300, 65)))

        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        # -- Frames de margem --
        self.topFrame = Frame(self.root,
                              width=300,
                              height=120)
        self.topFrame.configure(bg='#1A1A1A')
        
        self.topFrame.grid(column=1, row=0)

        self.mainFrame = Frame(self.root,
                               width=500,
                               height=480)
        
        self.mainFrame.grid(column=1, row=1)
        self.mainFrame.pack_propagate(False)

        self.bottomFrame = Frame(self.root,
                                 width=300,
                                 height=120)
                
        self.bottomFrame.grid(column=1, row=2)
        self.bottomFrame.configure(bg='#1A1A1A')

        ####
        self.invisibleFrame = Frame(self.mainFrame, height=150)
        self.invisibleFrame.pack(side='top')

        # Label para a imagem
        self.imgLabel = Label(self.mainFrame, image=self.logo)
        self.imgLabel.pack(side='top', fill="x")

        ####
        self.invisibleFrame = Frame(self.mainFrame, height=40)
        self.invisibleFrame.pack(side='top')

        # Botões
        self.buttonSQL = Button(self.mainFrame, text='SQL', height=2, command=lambda: self.postgre_win(interSQL))
        self.buttonNOSQL = Button(self.mainFrame, text='NOSQL', height=2)
        
        self.buttonSQL.pack(side='top', fill='x')
        self.buttonNOSQL.pack(side='top', fill='x')

        self.root.mainloop()

    def postgre_win(self, intSQL):
        intSQL()
        
class PostgreInterface:
    ''' Classe para a interface de interação via postgre '''

    def __init__(self):
        self.window = Toplevel()
        self.window.geometry('1128x896')

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(4, weight=1)
        self.window.rowconfigure(3, weight=1)

        #### TODOS OS FRAMES ####
        
        self.invisibleFrame1 = Frame(self.window)
        self.invisibleFrame2 = Frame(self.window)

        self.optionsBar = Frame(self.window,
                                width=200,
                                height=680,
                                relief='ridge',
                                borderwidth=3
                                )
        
        self.infoDisplay = Frame(self.window,
                                 width=700,
                                 height=790,
                                 relief='solid',
                                 borderwidth=3)

        self.infoDataBar = Frame(self.window,
                                 width=200,
                                 height=680,
                                 relief='ridge',
                                 borderwidth=3)

        self.invisibleFrame1.grid(column=0, row=3)
        self.invisibleFrame2.grid(column=4, row=3)
        self.optionsBar.grid(column=1, row=3)
        self.infoDisplay.grid(column=2, row=3)
        self.infoDataBar.grid(column=3, row=3)
        self.optionsBar.pack_propagate(False)
        self.infoDisplay.pack_propagate(False)
        self.infoDataBar.pack_propagate(False)

        ### OptionsBar - Buttons ###
        self.btADD = Button(self.optionsBar,
                            text="ADICIONAR",
                            height=2)
        self.btREMOVE = Button(self.optionsBar,
                               text="REMOVER",
                               height=2)
        self.btEDITAR = Button(self.optionsBar,
                               text="EDITAR",
                               height=2)

        self.btADD.pack(side='top', fill='x', pady = (250,0))
        self.btREMOVE.pack(side='top', fill='x')
        self.btEDITAR.pack(side='top', fill='x')

        # infoDataBar - Buttons
        self.btProfessor = Button(self.infoDataBar,
                                  text="PROFESSORES",
                                  height=2)
        self.btTurma = Button(self.infoDataBar,
                                  text="TURMAS",
                                  height=2)

        self.btProfessor.pack(side='top', fill='x', pady = (270,0))
        self.btTurma.pack(side='top', fill='x')

        ### infoDisplay - Details ###
        self.searchBar = Entry(self.infoDisplay)
        self.searchBar.pack(side='top', fill='x')

        self.window.mainloop()


class NoSQLinterface:
    ''' Classe para a interface de interação com o banco não-relacional '''

    def __init__(self):
        pass


telaMain = mainInterface(PostgreInterface, NoSQLinterface)



