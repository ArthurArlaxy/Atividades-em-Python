tabela=('Botafogo','Palmeiras', 'Flamengo', 'Internacional', 'Fortaleza', 'São paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'EC Vitória', 'Grêmio', 'Vasco','Atlético MG', 'Athletico PR','Juventude', 'Fluminense', 'Criciúma','Bragantino','Cuiabá','Atlético- GO')

posição = tabela.index('Flamengo')

print(10*'-=','TABELA DO BRASILEIRÂO',10*'-=')
print(f'Os times presentes na série A do Brasileirão: {tabela}')
print(30*'-=')
print(f'Os primeiros 5 colocados são {tabela[0:5]}')
print(30*'-=')
print(f'Os Ultimos 5 Colocados são {tabela[15:]}')
print(30*'-=')
print(f'Os times em ordem Alfabetica são {sorted(tabela)}')
print(30*'-=')
print(f'O flamengo está na {posição + 1}° posição')
