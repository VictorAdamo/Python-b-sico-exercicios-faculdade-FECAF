import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Escolha seu candidato')],
            [sg.Text('1- Zé das couves 2- Zé roela 3- Sem noção')],
            [sg.Text('4- Em branco 5- Nulo')],
            [sg.Text('Nome'),sg.Input(size=(24,0),key='nome')],
            [sg.Text('Idade'),sg.Input(size=(24,0),key='idade')],
            [sg.Text('Qual é o seu sexo?')],
            [sg.Checkbox('Masculino',key='M'),sg.Checkbox('Feminino',key='F')], 
            [sg.Text('Voto'),sg.Input(size=(24,0),key='voto')],
            [sg.Button('ENVIAR')],
            [sg.Output(size=(30,14))]
        ]
        #janela
        self.janela = sg.Window('ELEIÇÃO 2021').layout(layout)
        
    def Iniciar(self):
        while True:
            #extrair dados
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            sm = self.values['M']
            sf = self.values['F']
            voto = self.values['voto']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'Sexo masculino: {sm}')
            print(f'Sexo Feminino: {sf}')
            print(f'Voto: {voto}')
            print('=' * 15)   

tela = TelaPython()
tela.Iniciar()
        