import json


def carregar_leads():
    try:
        with open("leads.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []


def salvar_leads(leads):
    with open("leads.json", "w") as arquivo:
        json.dump(leads, arquivo, indent=4)


def validar_lead(lead):
    if "nome" not in lead or "renda" not in lead or "interesse" not in lead:
        return False
    if not isinstance(lead["renda"], (int, float)):
        return False
    return True


def classificar_lead(lead):
    if lead["renda"] >= 7000 and lead["interesse"] == "alto":
        return "🔥 QUENTE"
    elif lead["renda"] >= 4000:
        return "🟡 MORNO"
    else:
        return "❄️ FRIO"


def analisar_leads(leads):
    quente, morno, frio, invalidos = 0, 0, 0, 0
    relatorio = ""

    for lead in leads:

        if not validar_lead(lead):
            invalidos += 1
            continue

        classificacao = classificar_lead(lead)

        if "QUENTE" in classificacao:
            quente += 1
        elif "MORNO" in classificacao:
            morno += 1
        else:
            frio += 1

        linha = f"{lead['nome']} → {classificacao}\n"
        relatorio += linha

    resumo = (
        f"\n📊 RESUMO:\n"
        f"🔥 Quentes: {quente}\n"
        f"🟡 Mornos: {morno}\n"
        f"❄️ Frios: {frio}\n"
        f"⚠️ Inválidos: {invalidos}\n"
    )

    relatorio += resumo

    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)

    print(relatorio)


def adicionar_lead(leads):
    nome = input("Nome: ")
    renda = float(input("Renda: "))
    interesse = input("Interesse (alto/medio/baixo): ")

    novo = {"nome": nome, "renda": renda, "interesse": interesse}
    leads.append(novo)
    salvar_leads(leads)

    print("✅ Lead adicionado!")


def menu():
    leads = carregar_leads()

    while True:
        print("\n==============================")
        print("📊 SISTEMA DE LEADS")
        print("==============================")
        print("1 - Ver leads")
        print("2 - Adicionar lead")
        print("3 - Gerar relatório")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            for lead in leads:
                print(lead)

        elif opcao == "2":
            adicionar_lead(leads)

        elif opcao == "3":
            analisar_leads(leads)

        elif opcao == "0":
            break

        else:
            print("❌ Opção inválida")


menu()
