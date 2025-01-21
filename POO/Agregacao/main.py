from classes import CarrinhoCompras, Produto

carrinho = CarrinhoCompras()

p1 = Produto('Camisa',45)
p2 = Produto('Calca',90)
p3 = Produto('Tenis',125)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())