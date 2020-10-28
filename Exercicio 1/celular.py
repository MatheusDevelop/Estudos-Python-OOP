class Celular:    
    def __init__(self,cor,modelo,tamanho,ligado):
        self.cor =cor 
        self.modelo = modelo
        self.tamanho = tamanho
        self.ligado = ligado
    
    def LigarCelular(self):
        if self.ligado:
            print("O celular ja esta ligado")
            return 
        self.ligado = True
        print("Celular ligado")

    def DesligarCelular(self):
        self.ligado = False
        print("Celular desligado")
    
    def FazerLigacao(self,numero):
        if not self.ligado:
            return
        print("Ligando para "+numero)
    
    def EnviarMensagem(self,mensagem,numero):
        if not self.ligado:
            return
        print("Mensagem '"+mensagem+"'enviada para "+numero)
    
    @classmethod
    def SetarCarregador(cls,tipoCarregador):        
        cls.carregador = tipoCarregador
    @staticmethod
    def CarregarCelular(celular):
        print(celular+" carregando")
        
        

#Testando metodos de instancia
nokia = Celular('Preto','Windows Phone','25p',True)
nokia.FazerLigacao("190")
nokia.EnviarMensagem("Ola mundo","9999-99999")
nokia.DesligarCelular()
nokia.LigarCelular()
nokia.LigarCelular()

iphone = Celular("Vermelho","6S","35p",True)
print(iphone.modelo)


#Testando metodos de classe
iphone.SetarCarregador("Iphone charge")
print(nokia.carregador)

nokia.SetarCarregador("Universal")
print(iphone.carregador)

#Testando metodos estaticos
nokia.CarregarCelular(nokia.modelo)

iphone.CarregarCelular(iphone.modelo)

Celular.CarregarCelular("Samsung")


