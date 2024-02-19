from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

ALTURA = 600
LARGURA = 400

#definindo tamanho da janela
Window.size = (LARGURA, ALTURA)
#Carrgeando o arquivo de 'front'
Builder.load_file('/home/lucas/Documentos/Kivy Projeto/Design.kv')


#classe para calculadora, que herda da classe widget do kivy
class Calculadora(Widget):
    def clear(self):
        self.ids.input_text.text = '0'
    
    def inserir_valor (self, numero):
        current_number = self.ids.input_text.text
       
        if current_number == "0":
            self.ids.input_text.text = ''
            self.ids.input_text.text = f"{numero}"

        else:
            self.ids.input_text.text = f"{current_number}{numero}"
    
    def sinais(self, sinal):
        current_number = self.ids.input_text.text
        self.ids.input_text.text = f"{current_number}{sinal}"
    
    def Del (self):
        removido = self.ids.input_text.text
        removido = removido[:-1] #string slice para remover o úlitmo caracter
        self.ids.input_text.text = removido
        if self.ids.input_text.text == '':
            self.ids.input_text.text = '0'
    
    def ponto(self):
        ponto = '.'
        current_number = self.ids.input_text.text
        self.ids.input_text.text = f"{current_number}{ponto}"

    def inverso (self):
        resultado = eval(self.ids.input_text.text)
        resultado = resultado*(-1)
        self.ids.input_text.text = str(resultado)

    def calcular (self):
        try:
            resultado = eval(self.ids.input_text.text)
            self.ids.input_text.text = str(resultado)
        except:
            pass
            

#classe que herda da classe app, para execução do aplicativo
class Calculadora_App(App):
    def build(self):
        return Calculadora()



if __name__ == '__main__':
    Calculadora_App().run()