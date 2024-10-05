import os

def cls():
    """Comando para limpar a tela dependendo do sistema operacional"""
    os.system('cls' if os.name=='nt' else 'clear')

def calcular_imc(peso, altura):
    """Calcula o IMC a partir do peso (kg) e altura (m)."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com os padrões da OMS."""
    if imc <= 0:
        raise Exception('Desculpe, mas não são aceitos números iguais ou menores a zero.')
    
    elif imc < 18.5:
        return 'Abaixo do peso'
    
    elif 18.5 <= imc < 24.9:
        return 'Peso normal'
    
    elif 25 <= imc < 29.9:
        return 'Sobrepeso'
    
    else:
        return 'Obesidade'

def main():
    # Inicialização da variável res com 'S' para garantir que o loop execute ao menos uma vez
    res = 'S'
    
    while res == 'S':
        print('=== Cálculo de IMC ==='.center(25))
        try:
            peso = float(input('Digite seu peso em kg: '))
            if peso <= 0:
                raise ValueError('Desculpe, mas não são aceitos números iguais ou menores a zero.')

            altura = float(input('Digite sua altura em metros: '))
            if altura <= 0:
                raise ValueError('Desculpe, mas não são aceitos números iguais ou menores a zero.')

            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)

            print(f'Seu IMC: {imc:.2f}\nClassificação: {classificacao}')
        
        except ValueError as ve:
            print(f"Erro: {ve}")
        
        res = input('\nDeseja refazer o cálculo? (S/N)\nOpção: ').strip().upper()
        
        if res == 'N':
            print('Encerrando...')
            break
        else:
            cls()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('=== ERRO ==='.center(25))
        print(f'Ocorreu um erro: {e}')
