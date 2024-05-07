Algoritmo "varifica o numero maior"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/03/2024
Var
// Seção de Declarações das variáveis 
peso:real
altura:real
imc:Real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("digite o peso em kg:")
leia(altura)
escreva("digite a altura em metros:")
leia(altura)
imc<-peso/(altura*altura)
escreva("seu imc e:",imc)
 se (imc>=18.5) entao
escreva("voce esta abaixo do peso.")
  senao
   se (imc>=18.5)e(imc<25) entao
    escreva("seu peso esta normal.")
     senao
      se (imc>=25)e(imc <30) entao
       escreva("voce esta com sobrepeso.")
       senao
        se (imc>=30)e(imc <35) entao
         escreva ("voce esta com obesidade grau I.")
        senao
         se (imc>=35)e(imc <40) entao
          escreva("voce esta com obesidade grau II (severa).")
         senao
          escreva("voce esta com obesidade grau III (morbida)>")
         fimse
        fimse
      fimse
   fimse
 fimse
Fimalgoritmo