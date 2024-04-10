estudantes = ['Maria', 'João', 'Ana', 'Helena', 'Kauane', 'Juliana', 'Gabriel', 'Pedro', 'Felipe']
disciplinas = ['Filosofia', 'Raciocínio Computacional', 'Eletroeletrônica Aplicada', 'Matemática']
professores = ['Carlos', 'Eleoni', 'José', 'Fabiola', 'Eduardo', 'Fausto', 'Danilo', 'Marta']
turmas = ['TDS 1', 'TDS 2', 'DTA 1', 'DTA 2', 'ADS 1', 'ADS 2', 'ADS 3', 'Big Data 1']
matriculas = ['12345', '54321', '13579', '24682', '98765', '54673']

while True:
    option = int(input("\nSelecione a opção desejada:\n1-Estudante\n2-Disciplina\n3-Professor\n4-Turma\n5-Matrícula\n6-Sair\n>>>"))

    if 2 <= option <= 5:
        print(">>>EM DESENVOLVIMENTO")
        continue

    match option:
        case 1:
            print("==== Estudante ====")
            opt = "estudante"
        case 6:
            break

    crud = int(input(f"\nSelecione a funcionalidade desejada para '{opt}':\n1-Incluir novo\n2-Ver todos\n3-Deletar\n4-Atualizar\n>>>"))

    match crud:
        case 1:
            print("=== Incluir novo ===")

            if option == 1:
                novo = input(f"Digite o nome do novo cadastro {opt}: ")
                estudantes.append(novo)
                print(estudantes)
            else:
                print("EM DESENVOLVIMENTO")
        case 2:
            print("===== Ver todos =====")
            if opt == "estudante":
                if len(estudantes)>0:
                    for i in estudantes:
                        print(i)
                else:
                    print("Não há estudantes para mostrar")
            else:
                print("EM DESENVOLVIMENTO")
        case 3:
            print("====== Deletar ======")
            print("EM DESENVOLVIMENTO")
        case 4:
            print("===== Atualizar =====")
            print("EM DESENVOLVIMENTO")
