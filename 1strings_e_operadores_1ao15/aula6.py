# Conversão de tipos, coerção
# Type convertion, typecasting, coercion
# É o ato de converter um tipo em outro
# tipos imutáveis e primitivos: str, int, float, bool
print(1 + 1) # int com float, o python entende
print('a' + 'b') #Só é possivel concatenar str com str, com int não funcionaria.
print('1', type('1'))

print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')


