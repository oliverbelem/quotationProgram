import pyfiglet

KILO:int = 10
SEG:float = 0.0033
FINAL:float = 0.96
ICMS:float = 0.04

class cotacao:

    def __init__(self):
        self.definicao:str = "sim"

    def calculo(self, und, nota):

        def frete_peso(und):
            return und * KILO

        def seguro(nota):
            return nota * SEG

        def frete_final(f_peso, seg):
            return (f_peso + seg) / FINAL

        def valor_icms (f_final):
            return f_final * ICMS
        
        f_peso:int = frete_peso(und)
        seg:float = seguro(nota)
        f_final = frete_final(f_peso, seg)
        v_icms = valor_icms(f_final)

        return f_peso, seg, f_final, v_icms
    
    def cabecalho(self):
        print("\n")
        titulo = pyfiglet.figlet_format("COTACAO", font="banner3-D")
        print(titulo)

    def titulo_input(self):
        print( "\n##############################################\n")
        print("Digite os valores de cada parte necessária:")

    def espacamento(self):
        print( "\n##############################################\n")

    def cotacao(self):

        self.titulo_input()
        und = int(input("Unidade (Kg): "))
        nota = float(input("Valor da nota (R$): "))
        self.espacamento()

        f_peso, seg,f_final, v_icms = self.calculo(und, nota)

        print( "############ VALORES DA COTAÇÃO ##############\n")
        print(f"O valor final da sua cotação é: {f_final:.2f}")
        print(f"O valor do seu ICMS: {v_icms:.2f}")
        self.espacamento()

    def run(self):
        self.cabecalho()
        while self.definicao != "NAO":
            self.cotacao()
            self.definicao = input("Quer realizar outra cotação?\n(SIM/NAO)").upper

def main():
    app = cotacao()
    app.run()

if __name__ == "__main__":
    main()