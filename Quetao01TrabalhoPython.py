def percent(p):
    return (p/soma)*100
def b_mb(r):
    return float(r)/(1024**2)
arq = open('usuarios.txt','r')
cont = 0
l = [1,2,3,4,5,6]
for linha in arq:
    linha= linha.strip()
    l[cont] = linha
    cont = cont + 1
p =[]
for n in range(0,6):
    p.append(l[n].split())

arq.close()

e=[1,2,3,4,5,6]
soma = 0
for k in range(0,6):
    e[k] = b_mb(p[k][1])
    soma = soma + e[k]

ç = [1,2,3,4,5,6]
for w in range(0,6):
    ç[w] = percent(e[w])

media = soma/6
for w in range(0,6):
    p[w][0] = p[w][0] + ' ' * (15 - len(p[w][0]))

t = open('relatorio.txt','w')
t.write('ACME  Inc.                Uso de espaço em disco pelo usuario \n')
t.write('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
t.write('Nr .  Usuário        Espaço Utilizado     % do uso \n')
t.write('\n')
t.write('\n') 
for y in range(0,6):
    t.write('{}    {}     {:>8.2f}MB      {:>8.2f}%\n'.format(y+1,p[y][0],e[y],ç[y]))
t.write('\n')
t.write('\n')
t.write('Espaço total ocupado:   {:.2f}\n'.format(soma))
t.write('Espaço médio ocupado:   {:.2f}'.format(media))
t.close()

