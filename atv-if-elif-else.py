# Atividade 01:
# Crie um algoritmo que peça o nome de dois times de futebol e quantos gols cada time fez na partida.
# Com os dados coletados, informe qual time venceu, qual time perdeu ou se houve empate.
time1 = input("Insira o nome do time 01: ")
gol_time1 = int(input("Quantos gols o time {0}: ".format(time1)))
time2 = input("Insira o nome do time 02: ")
gol_time2 = int(input("Quantos gols o time {0}: ".format(time2)))

if gol_time1 > gol_time2:
    print(f"Partida encerrada e o resultado final foi: {time1} {gol_time1} x {gol_time2} {time2} \n O campeão foi o time {time1}!!!")
elif gol_time1 < gol_time2: 
    print(f"Partida encerrada e o resultado final foi: {time1} {gol_time1} x {gol_time2} {time2} \n O campeão foi o time {time2}!!!")
else:
    print(f"Partida encerrada e o resultado final foi: {time1} {gol_time1} x {gol_time2} {time2} \n Deu empate!!!")

# Atividade 02:
# Solicite ao usuário a resposta (sim ou não) às perguntas abaixo e imprima a conclusão.
# 1) Febre alta?
# 2) Dores de cabeça?
# 3) Dores musculares?
# 4) Manchas vermelhas na pele?
# Conclusões:
# a) Se o usuário responder sim a pelo menos três perguntas,
# informe que ele está com dengue e peça para ele procurar um médico.
# b) Se o usuário responder sim a duas ou menos, informe que ele deve ficar em repouso e continuar observando a evolução dos sintomas.
# DICA: Será necessário utilizar INCREMENTO.

respostas_sim = 0

resposta = input("Você está com febre alta? (sim/não): ")
if resposta.lower() == "sim":
    respostas_sim += 1

resposta = input("Você está com dores de cabeça? (sim/não): ")
if resposta.lower() == "sim":
    respostas_sim += 1

resposta = input("Você está com dores musculares? (sim/não): ")
if resposta.lower() == "sim":
    respostas_sim += 1

resposta = input("Você tem manchas vermelhas na pele? (sim/não): ")
if resposta.lower() == "sim":
    respostas_sim += 1

if respostas_sim >= 3:
    print("Você pode estar com dengue. Procure um médico!")
elif respostas_sim >= 1:
    print("Fique em repouso e continue observando a evolução dos sintomas.")
else:
    print("Você não apresenta sintomas graves. Fique atento à sua saúde.")
