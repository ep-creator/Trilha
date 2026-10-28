#primeiro fiz c string (sem pesquisar resoluções)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        lista = list(str(x))
        tam = len(str(x))

        for i in range(tam//2):
            if lista[i] != lista[tam - 1 - i]:
                return False

        return True

#ai depois eu pesquisei e vi q tinha um jeito muito mais facil com string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

#ai depois eu vi esse algoritmo que acaba rodando mais rapido por que casting pra str é custoso
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #se o numero for negativo ou terminar em zero(e não for zero) já nao pode ser palindromo
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        numero_invertido = 0
        while x > numero_invertido:
            #reconstroi o numero ao contrário por que 
            #a cada passada primeiro numero (x%10) vai sendo jogado 
            #pra esquerda pelo *10
            numero_invertido = (numero_invertido * 10) + x % 10
            x = x // 10
            
        return x == numero_invertido or x == numero_invertido // 10