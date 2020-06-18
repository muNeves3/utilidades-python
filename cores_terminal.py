#\033[style(text style 0-7);text(text colors 30-37);back(background colors 40-47)
#python- padrão ansi

print('\033[0;30;41mHello, World!\033[m') #fundo vermelho letra branca
print('\033[4;33;44mHello, World!\033[m') #fundo azul letra amarela sublinhada
print('\033[35;43mHello, World!\033[m')   #fundo amarelo letra roxa
print('\033[mHello, World!\033[m')        #fundo padrão letra branca
print('\033[7;30mHello, World!\033[m')    #fundo branco letra preta(invertido)

nome = 'Murilo'

print('Olá, muito prazer em te conhecer, {}{}{}'.format('\033[4;34m',nome,'\033[m'))
