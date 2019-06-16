n = int(input('DIGITE UM NÚMERO PARA CRIPTOGRAFAR COM 4 DÍGITOS: '))
while n<0 or n>9999:
    print('VALOR INVÁLIDO !!!!')
    n = int(input('DIGITE UM NÚMERO PARA CRIPTOGRAFAR COM 4 DÍGITOS: '))
u1 = n // 1 % 10
d1 = n // 10 % 10
c1 = n // 100 % 10
m1 = n // 1000 % 10
u1 = (u1+6)%10
d1 = (d1+6)% 10
c1 = (c1+6)% 10
m1 = (m1+6)% 10
nu1 = c1
nc1 = u1
nd1 = m1
nm1 = d1
l = [nm1, nc1, nd1, nu1]
print('O NUMERO CRIPTOGRAFADO É : ', l[0], l[1], l[2], l[3])


n2 = int(input('DIGITE UM NÚMERO PARA DESCRIPTOGRAFAR COM 4 DÍGITOS: '))
while n<0 or n>9999:
    print('VALOR INVÁLIDO !!!!')
    n = int(input('DIGITE UM NÚMERO PARA DESCRIPTOGRAFAR COM 4 DÍGITOS: '))
U2 = n2//1%10
d2 = n2//10%10
c2 = n2//100%10
m2 = n2//1000%10
nu2 = c2
nc2 = U2
nd2 = m2
nm2 = d2
l = [nm2, nc2, nd2, nu2]
for c in range(0,4):
    if l[c]<6:
        l[c] = l[c] + 4
    else:
        l[c] = l[c] - 6
print('O NUMERO DESCRIPTOGRAFADO É : ',l[0],l[1],l[2],l[3])

