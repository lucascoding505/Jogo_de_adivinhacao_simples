# Jogo da Forca
import random
import os

continuar = True
frase_formada = ''
letra_acertada = ''
tentativa_count = 0
tentativa_archive = ''
tentativa_res = 10

lista_palavras = [
    "cachorro", "lustre", "parafuso", "nuvem", "tijolo",
    "espelho", "tapete", "colher", "girassol", "martelo",
    "pinguim", "canela", "farol", "cobertor", "serrote",
    "borboleta", "alicate", "queijo", "bengala", "poeira",
    "foguete", "chinelo", "ferradura", "manga", "pistao",
    "coruja", "isqueiro", "pedreira", "balcao", "termometro",
    "raposa", "cimento", "toalha", "pitanga", "tambor",
    "escova", "cogumelo", "parede", "limonada", "buzina",
    "palito", "ventania", "cadeira", "mostarda", "prego",
    "telhado", "gaivota", "fivela", "biscoito", "fumaça",
    "caracol", "trinco", "papagaio", "cebola", "escada",
    "torpedo", "almofada", "petala", "chumbo", "gaveta",
    "espiga", "torneira", "lagarto", "vassoura", "polvo",
    "rolha", "tijela", "jacare", "fosforo", "canudo",
    "portao", "reboque", "passaro", "cravos", "macaneta",
    "granizo", "chiclete", "lamina", "camarao", "campainha",
    "bigode", "moldura", "garrafa", "tablete", "patolino",
    "cortina", "enxada", "peneira", "tamandua", "caixote",
    "pardal", "macaco", "telha", "macarrao", "formiga",
    "pipoca", "colchão", "ziper", "badejo", "borracha"
]

print('Jogo da Forca')

while continuar:
    estilo_jogo = input('Como você deseja jogar? \n1 - Sozinho \n2 - Em Dupla \n3 - Sair do jogo \nEscolha: ')

    try:
        estilo_jogo_int = int(estilo_jogo)
    except:
        os.system('cls')
        print('Informe uma opção válida.')
        continue

    if estilo_jogo_int < 1 or estilo_jogo_int > 3:
        os.system('cls')
        print('Informe uma opção válida')
        continue

    if estilo_jogo_int == 3:
        break

    if estilo_jogo_int == 1:
        frase_secret = random.choice(lista_palavras)

    os.system('cls')

    while estilo_jogo_int == 1:
        tentativa = input('Digite uma letra: ').lower()

        if len(tentativa) > 1:
            print('Digite apenas uma letra')
            continue

        if tentativa in tentativa_archive:
            print('Você ja tentou essa letra!')
            continue
        else:
            tentativa_archive += tentativa

        tentativa_count += 1

        if tentativa in frase_secret:
            letra_acertada += tentativa
        else:
            tentativa_res -= 1


        frase_formada = ''
        for letra in frase_secret:
            if letra in letra_acertada:
                frase_formada += letra
            else:
                frase_formada += '*'

        print(frase_formada)
        print(f'Tentativas restantes: {tentativa_res}')

        if tentativa_res == 0:
            os.system('cls')
            print('Você perdeu!')
            print(f'Frase: {frase_secret}')
            tentativa_count = 0
            frase_secret = ''
            frase_formada = ''
            letra_acertada = ''
            tentativa_res = 10
            tentativa_archive = ''
            break

        
        if frase_formada == frase_secret:
            os.system('cls')
            print('Você ganhou!')
            print(f'Tentativas: {tentativa_count}')
            print(f'Frase: {frase_secret}')
            tentativa_count = 0
            frase_secret = ''
            frase_formada = ''
            letra_acertada = ''
            tentativa_res = 10
            tentativa_archive = ''
            break
    
    while estilo_jogo_int == 2:
        frase_secret = input('Informe a frase que você quer: ').lower()
        os.system('cls')

        while continuar:
            tentativa = input('Digite uma letra: ').lower()

            if len(tentativa) > 1:
                print('Digite apenas uma letra')
                continue

            tentativa_count += 1

            if tentativa in frase_secret:
                letra_acertada += tentativa
            else:
                tentativa_res -= 1
            
            if tentativa in tentativa_archive:
                print('Você já tentou essa letra!')
            else:
                tentativa_archive += tentativa

            frase_formada = ''
            for letra in frase_secret:
                if letra in letra_acertada:
                    frase_formada += letra
                else:
                    frase_formada += '*'

            print(frase_formada)
            print(f'Tentativas restantes: {tentativa_res}')

            if tentativa_res == 0:
                os.system('cls')
                print('Você perdeu!')
                print(f'Frase: {frase_secret}')
                tentativa_count = 0
                frase_secret = ''
                frase_formada = ''
                letra_acertada = ''
                tentativa_res = 10
                tentativa_archive = ''
                break
        
            if frase_formada == frase_secret:
                os.system('cls')
                print('Você ganhou!')
                print(f'Tentativas: {tentativa_count}')
                print(f'Frase: {frase_secret}')
                tentativa_count = 0
                frase_secret = ''
                frase_formada = ''
                letra_acertada = ''
                tentativa_res = 10
                tentativa_archive = ''
                break
        break

        
os.system('cls')
print(12 * '-')
print('Fim de Jogo')
print(12 * '-')