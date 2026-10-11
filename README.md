RentSmart — Sistema de Orçamento de Locação

1. Sobre o projeto

O RentSmart é um sistema desenvolvido em Python para auxiliar na elaboração de orçamentos de locação de imóveis da R.M. Imóveis.

O programa recebe as características do imóvel, aplica as regras comerciais, calcula o valor mensal do aluguel, apresenta a taxa contratual separadamente e gera uma projeção dos pagamentos para os primeiros 12 meses.

2. Objetivo

Automatizar o cálculo de orçamentos de locação, tornando o processo mais organizado e reduzindo erros de cálculo.

3. Tipos de imóveis

O sistema contempla três tipos de imóveis:

Apartamento

Casa

Studio

4. Regras de negócio

Apartamento

Valor base para 1 quarto: R$ 700,00.

Apartamento com 2 quartos: adicional de R$ 200,00.

Garagem: adicional de R$ 300,00.

Clientes sem filhos recebem desconto de 5% sobre o aluguel após os adicionais.

Casa

Valor base para 1 quarto: R$ 900,00.

Casa com 2 quartos: adicional de R$ 250,00.

Garagem: adicional de R$ 300,00.

Studio

Valor base: R$ 1.200,00.

Pacote inicial de 2 vagas: R$ 250,00.

Cada vaga adicional: R$ 60,00.

Taxa contratual

Valor total: R$ 2.000,00.

Parcelamento em até 5 vezes.

A taxa contratual é apresentada separadamente do aluguel mensal.

5. Funcionalidades

Entrada e validação dos dados do imóvel.

Cálculo do aluguel mensal.

Aplicação de adicionais e descontos.

Cálculo e parcelamento da taxa contratual.

Apresentação do resumo do orçamento.

Geração de projeção financeira de 12 meses em CSV.

6. Programação Orientada a Objetos

O projeto utiliza classes, objetos, atributos, métodos e herança.

Classes implementadas:

imovel: classe base dos imóveis.

apartamento: representa apartamentos e calcula seu aluguel.

casa: representa casas e calcula seu aluguel.

studio: representa studios e calcula seu aluguel.

contrato: calcula as parcelas da taxa contratual.

As classes apartamento, casa e studio herdam da classe imovel.

7. Tecnologias utilizadas

Python 3.

Biblioteca padrão csv do Python.

Draw.io para elaboração do fluxograma.

GitHub para hospedagem e compartilhamento do projeto.

8. Como executar

Instale o Python 3.

Baixe os arquivos do projeto.

Abra o terminal na pasta em que está o arquivo Python.

Execute o comando:

python rentsmart.py

Responda às perguntas apresentadas pelo programa.

Ao finalizar a execução, o sistema gera o arquivo projecao_rentsmart.csv com a projeção dos pagamentos para 12 meses.

9. Arquivo CSV

O arquivo projecao_rentsmart.csv contém:

Mês da projeção.

Valor mensal do aluguel.

Parcela da taxa contratual.

Total esperado em cada mês.

As parcelas contratuais aparecem somente durante a quantidade de meses selecionada pelo usuário.

10. Documentação teórica

O projeto possui um documento teórico com a análise do problema, as regras de negócio, as entradas e saídas, o pensamento algorítmico, o fluxograma e a estrutura das classes.

11. Projeto acadêmico

Disciplina: Algorithmic Thinking & Introduction to Object-Oriented Programming.

12. Referências

Materiais da disciplina disponibilizados no AVA.

Aprendendo do Início com Daniel: https://www.youtube.com/@aprendendo.doinicio

LearnPython.org: https://learnpython.org/
