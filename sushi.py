from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculadoraPratos(GridLayout):
    def __init__(self, **kwargs):
        super(CalculadoraPratos, self).__init__(**kwargs)
        self.cols = 2  # Layout em 2 colunas
        
        # Inputs para cada tipo de prato
        self.add_widget(Label(text="Pratos Amarelos:"))
        self.amarelo = TextInput(multiline=False)
        self.add_widget(self.amarelo)

        self.add_widget(Label(text="Pratos Azuis:"))
        self.azul = TextInput(multiline=False)
        self.add_widget(self.azul)

        self.add_widget(Label(text="Pratos Vermelhos:"))
        self.vermelho = TextInput(multiline=False)
        self.add_widget(self.vermelho)

        self.add_widget(Label(text="Pratos Verdes:"))
        self.verde = TextInput(multiline=False)
        self.add_widget(self.verde)

        self.add_widget(Label(text="Pratos Pretos:"))
        self.preto = TextInput(multiline=False)
        self.add_widget(self.preto)

        # Botão para calcular
        self.calcular = Button(text="Calcular")
        self.calcular.bind(on_press=self.calcular_total)
        self.add_widget(self.calcular)

        # Labels para mostrar os resultados
        self.resultado_pratos = Label(text="")
        self.add_widget(self.resultado_pratos)

        self.resultado_valor = Label(text="")
        self.add_widget(self.resultado_valor)

    def calcular_total(self, instance):
        try:
            amarelo = int(self.amarelo.text)
            azul = int(self.azul.text)
            vermelho = int(self.vermelho.text)
            verde = int(self.verde.text)
            preto = int(self.preto.text)

            # Preços
            preco_amarelo = 4.45
            preco_azul = 5.45
            preco_vermelho = 6.45
            preco_verde = 7.45
            preco_preto = 8.45

            total_pratos = amarelo + azul + vermelho + verde + preto
            total_valor = (amarelo * preco_amarelo +
                           azul * preco_azul +
                           vermelho * preco_vermelho +
                           verde * preco_verde +
                           preto * preco_preto)

            # Exibir resultados
            self.resultado_pratos.text = f"Total de pratos: {total_pratos}"
            self.resultado_valor.text = f"Valor total: R$ {total_valor:.2f}"

        except ValueError:
            self.resultado_pratos.text = "Erro: insira números válidos"

class PratosApp(App):
    def build(self):
        return CalculadoraPratos()

if __name__ == "__main__":
    PratosApp().run()
