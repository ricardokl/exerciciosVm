
# Randomização de Exercícios de Física

Este módulo tem o intuito de gerar exercícios aleatórios baseados em **Templates** com um sistema próprio de modificadores.
No **Template** é possível especificar inúmeros parâmetros de randomização dos valores e variáveis globais, como, também, 
o resultado da questão.

Exemplo,

    f=0.06*(x0/tf)
    ---
    Qual é a velocidade escalar média, em km/h, de uma pessoa que percorre a pé {x0|min=1000;max=2000} em {tf|min=10;max=20} min?


Atualmente, há diversas funcionalidades ainda a serem desenvolvidas para o funcionamento completo desse projeto. Por 
enquanto foi apenas desenvolvido um sistema de geração de questão via modificadores pelo Template.

Para rodar o site com o streamlit, rodar o comando:
> streamlit run main.py

### TODO:
- Aplicativo com Streamlit. (Ainda essa semana!)
- Automatização de Geração de listas prontas em PDF e DOCX.
- Mais modificadores.
- Melhorar sistema de Tags e Templates.
- Banco de Dados
- Interface para Geração de Templates.
