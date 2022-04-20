print(f'{" LOJAS NASCIMENTO ":=^40}')
preço = float(input('Preço das compras? R$:'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Sua opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com juros.')
else:
    total = preço
    print('\033[1;31mOPÇÃO DE PAGAMENTO INVÁLIDA. TENTE NOVAMENTE!\33[m')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')


