# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)  # Calcula o custo da chamada
        if self.plano.verificar_saldo() >= custo:  # Verifica se o saldo é suficiente
            self.plano.deduzir_saldo(custo)  # Deduz o custo do saldo
            return f"Chamada para {destinatario} completada com sucesso. Saldo restante: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para completar a chamada."
# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':

# TODO: Verifique se o saldo do plano é suficiente para a chamada.

# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.

# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:

    # Método para verificar o saldo
    def verificar_saldo(self):
        return self.saldo

    # Método para calcular o custo da chamada
    def custo_chamada(self, duracao):
        custo_por_minuto = 0.10  # Supondo custo de $0.10 por minuto
        return duracao * custo_por_minuto

    # Método para deduzir o valor do saldo
    def deduzir_saldo(self, custo):
        self.saldo -= custo
# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input("nome")
numero = input("numero")
saldo_inicial = float(input("saldo"))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))