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
                               width=900,
                               height=680)
        
        self.mainFrame.grid(column=1, row=1)
        self.mainFrame.pack_propagate(False)

        self.bottomFrame = Frame(self.root,
                                 width=300,
                                 height=120)
                
        self.bottomFrame.grid(column=1, row=2)
        self.bottomFrame.configure(bg='#1A1A1A')

        # Label para a imagem
        self.imgLabel = Label(self.mainFrame, image=self.logo)
        self.imgLabel.pack(side='top', fill="x", pady=(200,0))

        # Botões
        self.buttonSQL = Button(self.mainFrame, text='SQL', height=4, width=30, command=lambda: self.postgre_win(interSQL))
        self.buttonNOSQL = Button(self.mainFrame, text='NOSQL', height=4, width=30, command=lambda: self.mongodb_win(interNOSQL))
        
        self.buttonSQL.pack(side='top', pady=(40,0))
        self.buttonNOSQL.pack(side='top')

        self.root.mainloop()

    def postgre_win(self, intSQL):
        intSQL()
    def mongodb_win(self, intNOSQL):
        intNOSQL()
        
class PostgreInterface:
    ''' Classe para a interface de interação via postgre '''

    def __init__(self):
        self.window = Toplevel()
        self.window.geometry('1128x896')
        self.window.title("SQL - MANIPULE DADOS DOS PROFESSORES")

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
                                 height=680,
                                 relief='solid',
                                 borderwidth=3)

        # Gambiarra do cancro, mas blz
        self.ctrlFrame = Frame(self.window, width=0, height=0)

        self.invisibleFrame1.grid(column=0, row=3)
        self.invisibleFrame2.grid(column=4, row=3)
        self.optionsBar.grid(column=1, row=3)
        self.infoDisplay.grid(column=2, row=3)
        self.ctrlFrame.grid(column=3, row=3)
        self.optionsBar.pack_propagate(False)
        self.infoDisplay.pack_propagate(False)
        self.ctrlFrame.pack_propagate(False)

        ### OptionsBar - Buttons ###
        self.btADD = Button(self.optionsBar,
                            text="ADICIONAR",
                            height=3)
        self.btREMOVE = Button(self.optionsBar,
                               text="REMOVER",
                               height=3)
        self.btEDITAR = Button(self.optionsBar,
                               text="EDITAR",
                               height=3)

        self.btADD.pack(side='top', fill='x', pady = (250,25))
        self.btREMOVE.pack(side='top', fill='x', pady = (0, 25))
        self.btEDITAR.pack(side='top', fill='x')

        ### infoDisplay - Details ###
        self.searchBar = Entry(self.infoDisplay, width=30)
        self.OptionsDisplay = Frame(self.infoDisplay,
                                    width=550,
                                    height=450,
                                    relief='sunken',
                                    borderwidth=4)
        
        self.searchBar.pack(side='top', anchor='w', pady=(100, 0), padx=(73,0))
        self.OptionsDisplay.pack(side='top')
        self.OptionsDisplay.pack_propagate(False)

        #### Scrollbar para o OptionsDisplay ####
        self.canvas = Canvas(self.OptionsDisplay)
        self.canvas.pack(side='left', fill='both', expand=1)

        self.scrollbar = Scrollbar(self.OptionsDisplay, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y', expand=1, padx = (150,0))

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.supportFrame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.supportFrame, anchor="nw")

        for thing in range(100):
            Button(self.supportFrame, text=f"Number {thing}").pack()

        self.window.mainloop()

class NoSQLinterface:
    ''' Classe para a interface de interação com o banco não-relacional '''

    def __init__(self):
        self.window = Toplevel()
        self.window.geometry('1128x896')
        self.window.title("SQL - MANIPULE DADOS DOS PROFESSORES")

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
                                    height=680,
                                    relief='solid',
                                    borderwidth=3)

        # Gambiarra do cancro, mas blz
        self.ctrlFrame = Frame(self.window, width=0, height=0)

        self.invisibleFrame1.grid(column=0, row=3)
        self.invisibleFrame2.grid(column=4, row=3)
        self.optionsBar.grid(column=1, row=3)
        self.infoDisplay.grid(column=2, row=3)
        self.ctrlFrame.grid(column=3, row=3)
        self.optionsBar.pack_propagate(False)
        self.infoDisplay.pack_propagate(False)
        self.ctrlFrame.pack_propagate(False)

        ### OptionsBar - Buttons ###
        self.btADD = Button(self.optionsBar,
                            text="ADICIONAR",
                            height=3)
        self.btREMOVE = Button(self.optionsBar,
                                text="REMOVER",
                                height=3)
        self.btEDITAR = Button(self.optionsBar,
                                text="EDITAR",
                                height=3)

        self.btADD.pack(side='top', fill='x', pady = (250,25))
        self.btREMOVE.pack(side='top', fill='x', pady = (0, 25))
        self.btEDITAR.pack(side='top', fill='x')

        ### infoDisplay - Details ###
        self.searchBar = Entry(self.infoDisplay, width=30)
        self.OptionsDisplay = Frame(self.infoDisplay,
                                    width=550,
                                    height=450,
                                    relief='sunken',
                                    borderwidth=4)
        
        self.searchBar.pack(side='top', anchor='w', pady=(100, 0), padx=(73,0))
        self.OptionsDisplay.pack(side='top')
        self.OptionsDisplay.pack_propagate(False)

        #### Scrollbar para o OptionsDisplay ####
        self.canvas = Canvas(self.OptionsDisplay)
        self.canvas.pack(side='left', fill='both', expand=1)

        self.scrollbar = Scrollbar(self.OptionsDisplay, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y', expand=1, padx = (150,0))

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.supportFrame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.supportFrame, anchor="nw")

        for thing in range(100):
            Button(self.supportFrame, text=f"Number {thing}").pack()

        self.window.mainloop()


telaMain = mainInterface(PostgreInterface, NoSQLinterface)