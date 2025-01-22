# Calculadora de IMC

Este projeto consiste em uma calculadora de IMC (\*\*\*\*\*\*\*) criada com Python e a biblioteca `tkinter` para a interface gráfica.

## Funcionalidades

- Interface amigável para entrada de dados.
- Cálculo do IMC baseado no peso e altura fornecidos.
- Exibição do resultado diretamente na janela do aplicativo.

## Requisitos

- Python 3.6 ou superior.

## Como usar

1. Clone este repositório ou copie o código fonte.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o script com o comando:
   ```bash
   python nome_do_arquivo.py
   ```
4. Uma janela será aberta:
   - Insira seu peso (em kg) no campo correspondente.
   - Insira sua altura (em metros) no campo correspondente.
   - Clique no botão **Calcular**.
5. O resultado do cálculo do IMC será exibido na janela.

## Estrutura do Projeto

- **Interface Gráfica:** Utiliza `tkinter` para criar os elementos visuais (Labels, Entry, Button).
- **Função de Cálculo:** A função `calcula_imc` é responsável por realizar o cálculo matemático e exibir o resultado.

## Fórmula do IMC

A fórmula usada para o cálculo é:

\[ IMC = \frac{Peso \ (kg)}{Altura \ (m)^2} \]

## Exemplo de Uso

- **Peso:** 70 kg
- **Altura:** 1.75 m
- **Cálculo:**
  \[ IMC = \frac{70}{1.75^2} = 22.86 \]
- **Resultado:** "O seu IMC é 22.86"

## Personalização

Se desejar alterar ou expandir o projeto:

- Adicione categorias de classificação do IMC (e.g., abaixo do peso, peso normal, sobrepeso).
- Modifique o layout ou estilo da interface.

## Licença

Este projeto é de uso livre. Sinta-se à vontade para modificar e compartilhar.

## Autor

- **Seu Nome**

