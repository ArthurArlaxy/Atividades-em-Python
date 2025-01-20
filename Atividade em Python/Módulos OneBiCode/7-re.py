import re
text = 'OneBitCode: Me tornarei um grande programador'

match = re.search(r'um grande', text)
print('Indice inicial', match.start())
print('Indice final', match.end())

text1 = 'O galinheiro. Filme original'

match = re.search(r'\.', text1)
print(match)

pattern = '[a-n]'
resultado = re.findall(pattern, text)
print(resultado)

rule = r'^A'
phrases = ['A casa pegou fogo','O peito do pa','Arthur é lindo']
for f in phrases:
    if re.search(rule,f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')

rule2 = r'!$'
phrases2= ['Noites de verão!', 'cabelo cortado.','Sonic']
for f in phrases2:
    if re.search(rule2,f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')