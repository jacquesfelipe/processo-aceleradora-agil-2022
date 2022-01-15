class Accelerator:
    def __init__(self, nomeCliente, quantidadeEnergetico):
        self.nomeCliente = nomeCliente
        self.quantidadeEnergetico = quantidadeEnergetico

    def valorMercadoria(self):
        return self.quantidadeEnergetico * (4.5)

    def calculoIcms(self):
        return self.valorMercadoria() * (18/100)

    def calculoIpi(self):
        return self.valorMercadoria() * (4/100)

    def calculoPis(self):
        return self.valorMercadoria() * (1.86/100)

    def calculoCofins(self):
        return self.valorMercadoria() * (8.54/100)

    def totalImpostos(self):
        return self.valorMercadoria() * (32.4/100) # 32.4 = Todos os impostos (ICMS+IPI+PIS+COFINS) somados.
    
    def valorTotal(self):
        return self.valorMercadoria() + self.totalImpostos()

    #Calculo de bonificação de 3% para compras de produtos para clientes que comprarem em grande quantidade.
    def bonificacao(self):
        return (self.valorMercadoria() * (3/100))
            
    def relatorioClientes(self):
        print(f'Cliente: {self.nomeCliente}')
        print(f'ICMS: R$ {self.calculoIcms():.2f}; IPI: R$ {self.calculoIpi():.2f}; PIS: R$ {self.calculoPis():.2f}; COFINS: R$ {self.calculoCofins():.2f}; Total: R$ {self.valorTotal():.2f}\n')
        if self.quantidadeEnergetico > 2000: #Calculo de bonificação para clientes que comprarem acima de 2000 produtos.
            print(f'Bonificação para o Cliente {self.nomeCliente}: R$ {self.bonificacao():.2f}\n')

    def relatorioGeral(clienteUm, clienteDois):       
        somaImpostos = clienteUm.totalImpostos() + clienteDois.totalImpostos()
        totalMercadorias = clienteUm.valorMercadoria() + clienteDois.valorMercadoria()
        totalGeral = clienteUm.valorTotal() + clienteDois.valorTotal()
        print(f'Total Impostos: R$ {somaImpostos:.2f}')
        print(f'Total Mercadorias: R$ {totalMercadorias:.2f}')
        print(f'Total Geral: R$ {totalGeral:.2f}')


clienteUm = Accelerator("Supermercado Dosul", 350)
clienteDois = Accelerator("Super Zottis", 400)

clienteUm.relatorioClientes()
clienteDois.relatorioClientes()

Accelerator.relatorioGeral(clienteUm, clienteDois)


