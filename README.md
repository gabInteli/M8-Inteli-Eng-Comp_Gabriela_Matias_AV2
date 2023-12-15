# Avaliação 2 - Módulo 8 
## Engenharia da Computação - Gabriela Rodrigues Matias 

### Contexto do Projeto
Sua tarefa é montar uma prova de conceito de uma aplicação que utiliza arquiteturas modernas de aprendizado profundo como ferramenta de sintetização de voz, potencialmente agindo como uma ponte valiosa para a comunicação, permitindo que pessoas com desafios na fala, incluindo aquelas no espectro autista, se expressem de maneira mais eficaz em seu cotidiano. Para tal, deve-se desenvolver:
1. Uma interface de terminal. O usuário deve ser capaz de inserir frases para sintetização de forma contínua, sem precisar reinicializar a aplicação cada vez que precisar inserir uma frase.
2. Integração com um modelo de machine learning capaz de sintetização de fala. 
3. Reprodução do áudio gerado pelo modelo de sintetização de fala.

### Estrutura do Sistema 
Foi desenvolvido um código responsável por captar as informações fornecidas pelo usuário via terminal. Após essa captação a resposta é transformada em uma saída de audio chamada de "Output.mp3". 

### Como Executar 

1. Clone o repositório: 
```
git clone https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias_AV2.git
```

2. Instale as Dependências: 
```
pip install -r requirements.txt
```
3. Execute o Arquivo Principal:
```
python3 main.py
```

4. Digite o seu texto: 
```
Olá, tudo bem ? Serei seu sistema responsável por transcrever seus textos em um formato de aúdio
O que você gostaria de dizer ?
```

5. Ouça o Output Gerado. 

