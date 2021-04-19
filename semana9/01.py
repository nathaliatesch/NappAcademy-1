def juros_simples(capital, taxa=0.1, n_periodos=2):
    if capital <= 0:
        raise Exception('Capital precisa ser maior que zero.')
    if taxa < 0 or taxa > 1:
        raise Exception('Taxa precisa estar entre 0 e 1.')
    if n_periodos <= 0:
        raise Exception('Período precisa ser maior que zero.')
    return capital + capital * taxa * n_periodos