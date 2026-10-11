
import csv


class imovel:

    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base


class apartamento(imovel):

    def __init__(self, quartos, garagem, filhos):
        super().__init__("Apartamento", 700)

        self.quartos = quartos
        self.garagem = garagem
        self.filhos = filhos

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.quartos == 2:
            valor += 200

        if self.garagem:
            valor += 300

        if not self.filhos:
            valor -= valor * 0.05

        return valor


class casa(imovel):

    def __init__(self, quartos, garagem):
        super().__init__("Casa", 900)

        self.quartos = quartos
        self.garagem = garagem

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.quartos == 2:
            valor += 250

        if self.garagem:
            valor += 300

        return valor


class studio(imovel):

    def __init__(self, vagas):
        super().__init__("Studio", 1200)

        self.vagas = vagas

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.vagas <= 2:
            valor += 250

        else:
            vagas_adicionais = self.vagas - 2
            valor += 250 + (vagas_adicionais * 60)

        return valor


class contrato:

    def __init__(self, parcelas):
        self.valor = 2000
        self.parcelas = parcelas

    def calcular_parcela(self):
        return self.valor / self.parcelas

    def calcular_parcelas(self):

        valor_centavos = 200000
        quantidade = self.parcelas

        valor_base = valor_centavos // quantidade
        resto = valor_centavos % quantidade

        lista_parcelas = []

        for i in range(quantidade):

            if i < resto:
                parcela = valor_base + 1
            else:
                parcela = valor_base

            lista_parcelas.append(parcela / 100)

        return lista_parcelas


print("===== RENTSMART =====")
print("1 - Apartamento")
print("2 - Casa")
print("3 - Studio")

opcao = input("Escolha o tipo de imóvel: ")

print("Você escolheu:", opcao)

imovel_usuario = None


# =========================
# APARTAMENTO
# =========================

if opcao == "1":

    quartos = int(input("Quantos quartos? (1 ou 2): "))

    while quartos < 1 or quartos > 2:
        print("Quantidade inválida. Escolha 1 ou 2 quartos.")
        quartos = int(input("Quantos quartos? (1 ou 2): "))

    garagem = input("Possui garagem? (s/n): ")

    while garagem not in ["s", "n"]:
        print("Resposta inválida. Digite s ou n.")
        garagem = input("Possui garagem? (s/n): ")

    filhos = input("Possui filhos? (s/n): ")

    while filhos not in ["s", "n"]:
        print("Resposta inválida. Digite s ou n.")
        filhos = input("Possui filhos? (s/n): ")

    if garagem == "s":
        garagem = True
    else:
        garagem = False

    if filhos == "s":
        filhos = True
    else:
        filhos = False

    apartamento_usuario = apartamento(
        quartos,
        garagem,
        filhos
    )

    imovel_usuario = apartamento_usuario

    print()
    print("===== RESULTADO =====")
    print("Tipo:", apartamento_usuario.tipo)
    print("Aluguel mensal: R$",
          f"{apartamento_usuario.calcular_aluguel():.2f}")


# =========================
# CASA
# =========================

elif opcao == "2":

    quartos = int(input("Quantos quartos? (1 ou 2): "))

    while quartos < 1 or quartos > 2:
        print("Quantidade inválida. Escolha 1 ou 2 quartos.")
        quartos = int(input("Quantos quartos? (1 ou 2): "))

    garagem = input("Possui garagem? (s/n): ")

    while garagem not in ["s", "n"]:
        print("Resposta inválida. Digite s ou n.")
        garagem = input("Possui garagem? (s/n): ")

    if garagem == "s":
        garagem = True
    else:
        garagem = False

    casa_usuario = casa(
        quartos,
        garagem
    )

    imovel_usuario = casa_usuario

    print()
    print("===== RESULTADO =====")
    print("Tipo:", casa_usuario.tipo)
    print("Aluguel mensal: R$",
          f"{casa_usuario.calcular_aluguel():.2f}")


# =========================
# STUDIO
# =========================

elif opcao == "3":

    vagas = int(input("Quantas vagas de estacionamento? "))

    while vagas < 2:
        print("Quantidade inválida. O pacote inicial possui 2 vagas.")
        vagas = int(input("Quantas vagas de estacionamento? "))

    studio_usuario = studio(vagas)

    imovel_usuario = studio_usuario

    print()
    print("===== RESULTADO =====")
    print("Tipo:", studio_usuario.tipo)
    print("Quantidade de vagas:", studio_usuario.vagas)
    print("Aluguel mensal: R$",
          f"{studio_usuario.calcular_aluguel():.2f}")


# =========================
# OPÇÃO INVÁLIDA
# =========================

else:

    print("Opção inválida.")
    print("Programa encerrado.")


# =========================
# CONTRATO
# =========================

if imovel_usuario is not None:

    print()
    print("===== CONTRATO =====")

    parcelas = int(
        input(
            "Em quantas parcelas deseja pagar a taxa contratual? (1 a 5): "
        )
    )

    while parcelas < 1 or parcelas > 5:

        print("Quantidade inválida. Escolha entre 1 e 5 parcelas.")

        parcelas = int(
            input(
                "Em quantas parcelas deseja pagar a taxa contratual? (1 a 5): "
            )
        )

    contrato_usuario = contrato(parcelas)

    lista_parcelas = contrato_usuario.calcular_parcelas()

    print()
    print("Taxa contratual: R$",
          f"{contrato_usuario.valor:.2f}")

    print("Quantidade de parcelas:",
          contrato_usuario.parcelas)

    print("Parcelas:")

    for i, valor in enumerate(lista_parcelas, start=1):
        print(f"Parcela {i}: R$ {valor:.2f}")


    # =========================
    # RESUMO DO ORÇAMENTO
    # =========================

    print()
    print("================================")
    print("       RESUMO DO ORÇAMENTO")
    print("================================")

    print("Tipo de imóvel:",
          imovel_usuario.tipo)

    print("Valor base: R$",
          f"{imovel_usuario.valor_base:.2f}")

    if imovel_usuario.tipo == "Apartamento":

        if imovel_usuario.quartos == 2:
            print("Adicional 2 quartos: R$ 200.00")

        if imovel_usuario.garagem:
            print("Adicional garagem: R$ 300.00")

        if not imovel_usuario.filhos:
            print("Desconto de 5%: aplicado")

    elif imovel_usuario.tipo == "Casa":

        if imovel_usuario.quartos == 2:
            print("Adicional 2 quartos: R$ 250.00")

        if imovel_usuario.garagem:
            print("Adicional garagem: R$ 300.00")

    elif imovel_usuario.tipo == "Studio":

        print("Vagas de estacionamento:",
              imovel_usuario.vagas)

        print("Pacote inicial de 2 vagas: R$ 250.00")

        if imovel_usuario.vagas > 2:

            vagas_adicionais = imovel_usuario.vagas - 2

            print("Vagas adicionais:",
                  vagas_adicionais)

            print("Valor das vagas adicionais: R$",
                  f"{vagas_adicionais * 60:.2f}")

    print("--------------------------------")

    print("ALUGUEL MENSAL: R$",
          f"{imovel_usuario.calcular_aluguel():.2f}")

    print("--------------------------------")

    print("Taxa contratual: R$",
          f"{contrato_usuario.valor:.2f}")

    print("Quantidade de parcelas:",
          contrato_usuario.parcelas)

    print("================================")


    # =========================
    # PROJEÇÃO DOS 12 MESES
    # =========================

    nome_arquivo = "projecao_rentsmart.csv"

    with open(
        nome_arquivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "Mês",
            "Aluguel",
            "Parcela do contrato",
            "Total esperado"
        ])

        valor_aluguel = imovel_usuario.calcular_aluguel()

        for mes in range(1, 13):

            if mes <= contrato_usuario.parcelas:
                parcela_contrato = lista_parcelas[mes - 1]
            else:
                parcela_contrato = 0

            total = valor_aluguel + parcela_contrato

            escritor.writerow([
                mes,
                f"{valor_aluguel:.2f}",
                f"{parcela_contrato:.2f}",
                f"{total:.2f}"
            ])

    print()
    print("Projeção de 12 meses gerada com sucesso!")
    print("Arquivo:", nome_arquivo)