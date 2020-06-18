print('*********artimetic operators*********')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
op = str(input('Digite um operador +, -, *, /, **, //, %: '))

def switch_demo(op):
        switcher = {
            '+': print('{} + {} == {}'.format(n1,n2, n1 + n2)),
            '-': print('{} - {} == {}'.format(n1,n2, n1 - n2)),
            '*': print('{} * {} == {}'.format(n1,n2, n1 * n2)),
            '/': print('{} / {} == {}'.format(n1,n2, n1 / n2)),
            '**': print('{} ** {} == {}'.format(n1,n2, n1 ** n2)),
            '//': print('{} // {} == {}'.format(n1,n2, n1 // n2)),
            '%': print('{} + {} == {}'.format(n1,n2, n1 % n2))   ,    
        }
        
