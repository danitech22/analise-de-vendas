vendas =[
{"loja":"centro","produto":"celular","valor":2890},
{"loja":"bairro","produto":"carregador","valor":236},
{"loja":"centro","produto":"fone", "valor":170,}
]

total_por_loja = {} 

for item in vendas: 
    loja = item["loja"] 
    valor = item["valor"] 
    if loja not in total_por_loja: 
        total_por_loja[loja] = 0 

    total_por_loja[loja]+= valor 

print("total por loja:",total_por_loja)
