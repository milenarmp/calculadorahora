import datetime
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty

class TelaInicial(Widget):
    hora = ObjectProperty(None)
    minuto = ObjectProperty(None)
    horariosaida = StringProperty()
    somahora = ObjectProperty(None)
    minutosoma = ObjectProperty(None)

    def btn(self):
        if len(self.hora.text) > 0 and len(self.minuto.text) > 0 and len(self.somahora.text) > 0 and len(self.minutosoma.text) > 0:
            inicio = datetime.datetime(2020, 1, 1, int(self.hora.text), int(self.minuto.text), 00, 000000)
            fim = inicio + datetime.timedelta(hours = int(self.somahora.text), minutes= int(self.minutosoma.text))
            horastring = str(fim)
            horaseparado = horastring.split()
            self.horariosaida = horaseparado[1][:5]
        else:
            self.horariosaida = 'Formato inválido!'

class calculadorahora(App): # <- Main Class
    def build(self):
        return TelaInicial()

if __name__ == '__main__':
    calculadorahora().run()