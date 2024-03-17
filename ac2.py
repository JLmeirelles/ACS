"""
AC2 
João Lucas Ferraz Meirelles / 202402116495

"""
 # Exercício
def calcula_salario(valor_hora: float, num_horas: float, irpf: float = 0.275) -> float:
     # Converte irpf para um valor decimal
    irpf = irpf / 100
    """
    valor_hora (float): O valor do salário por hora.
    num_horas (float): O número de horas trabalhadas no mês.
    irpf (float, opcional): A taxa de imposto de renda a ser deduzida, 0.275.

    Retorna:
    float: O salário líquido do funcionário.
    """
    # Calcula o salário bruto
   salario_bruto = valor_hora * num_horas

    # Calcula o salário líquido
    salario_liquido = salario_bruto * (1 - irpf)

    return salario_liquido
