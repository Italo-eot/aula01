base_ano = 1000

# 1) Solicita ao usuário que digite seu nome
nome_funcionario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o percentual de bonus: "))

# 4) Calcule o valor do bônus final
valor_bonus = (base_ano + salario) * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome_funcionario}, o seu bônus foi de {valor_bonus} !")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# conseguimos inserir valores negativos tanto em salário quanto em bônus, podendo assim criar um resultado fora da realidade do funcionário.