def csv_para_texto():
    arquivo_csv = input("Por favor, digite o nome do arquivo CSV: ")

    componentes = []
    problemas = []
    solucoes = []
    maquinas = []
    dados_sensoriais = []

    with open(arquivo_csv, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if 'nome: ' in linha:
                nome = linha.split('nome: ')[1].strip('"}""})')
                if 'Componente' in linha:
                    componentes.append(nome)
                elif 'Problema' in linha:
                    problemas.append(nome)
                elif 'Solucao' in linha:
                    solucoes.append(nome)
                elif 'Maquina' in linha:
                    maquinas.append(nome)
                elif 'DadoSensorial' in linha:
                    dados_sensoriais.append(nome)

    with open('saida.txt', 'w') as saida:
        for componente in componentes:
            for maquina in maquinas:
                for problema in problemas:
                    for solucao in solucoes:
                        for dado_sensorial in dados_sensoriais:
                            saida.write(f"O componente: {componente} é parte da Máquina: {maquina}, seus possiveis problemas são: {problema}, que geralmente e causado por: {dado_sensorial}, e pode ser solucionado com: {solucao}\n")

csv_para_texto()
