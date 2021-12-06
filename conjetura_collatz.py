#conjetura de collatz python 3.9.9
import os
import pathlib
from datetime import datetime
import matplotlib.pyplot as plt
NOW = datetime.now()

def fGranizos(value):
    auxvalue = value
    output = [value]
    while(auxvalue > 1) :
        if(auxvalue % 2 == 0) :
            auxvalue = int(auxvalue / 2)
        else :
            auxvalue = int((auxvalue * 3) + 1)
        output.append(auxvalue)
    return output

def contarGranizos(value):
    granizos_primerd = []
    for x in value:
        granizos_primerd.append(int(str(x)[0]))
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in granizos_primerd:
        if(x == 1):
            output[0] = output[0] + 1
        if(x == 2):
            output[1] = output[1] + 1
        if(x == 3):
            output[2] = output[2] + 1
        if(x == 4):
            output[3] = output[3] + 1
        if(x == 5):
            output[4] = output[4] + 1
        if(x == 6):
            output[5] = output[5] + 1
        if(x == 7):
            output[6] = output[6] + 1
        if(x == 8):
            output[7] = output[7] + 1
        if(x == 9):
            output[8] = output[8] + 1
    return output

def sizeGraph(value):
    output = [6.4, 4.8]
    if(len(value) >= 10 and len(value) < 25): output = [12, 10]
    if(len(value) >= 25): output = [20, 12]
    return output

def pathGraph():
    output = str(pathlib.Path(__file__).parent.absolute())
    if(os.path.exists(output + "/graficos")):
        output = output + "/graficos"
    return output

def graficos(valor_entrada, granizos):
    ## Declaramos valores para el eje x
    eje_x1 = range(1, len(granizos)+1)
    eje_x2 = range(1, 10) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

    ## Declaramos valores para el eje y
    eje_y2 = contarGranizos(granizos)
    print("Granizos Primeros Digitos Contados: ", eje_y2)
    ## Creamos Gráfica
    plot1 = plt.figure(figsize=sizeGraph(granizos))
    plot1.tight_layout()
    plot1.subplots_adjust(left=0.125,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.2, 
                        hspace=0.6)
    
    ## Definimos primer subplot
    ax1 = plot1.add_subplot(2,1,1) 
    ax1.plot(eje_x1, granizos, 'bo', eje_x1, granizos, 'black') #Grafico
    
    for index, value in enumerate(granizos): 
        if(len(str(value)) < 5): ax1.text(index + 1.1, value - .2, str(value),  color = 'black', fontsize = 6, fontweight = 'normal') 

    ax1.grid(which='both')
    ax1.set_ylabel('Granizos') ## Legenda en el eje y
    ax1.set_xlabel('Iteraciones: ' + str(len(granizos))) ## Legenda en el eje x
    ax1.set_title('conjetura de collatz para: ' + str(valor_entrada)) ## Título de Gráfica

    ## Definimos segundo subplot
    ax2 = plot1.add_subplot(2,1,2) 
    ax2.axis([0, len(eje_y2)+1, 0, max(eje_y2)+1]) ## Se define ancho y alto del grafico previamente
    ax2.bar(eje_x2, eje_y2, color="green") # Grafico
    
    for index, value in enumerate(eje_y2): 
        if(value != 0): ax2.text(index + .9, value - .3, str(value),  color = 'black', fontsize = 10, fontweight = 'bold') 
        
    ax2.set_ylabel('Cantidad de veces repetido') ## Legenda en el eje y
    ax2.set_xlabel('Numeros') ## Legenda en el eje x
    ax2.set_title('ley de benford (distribucion del grafico)') ## Título de Gráfica

    ## Guardamos imagen
    plot1.savefig(pathGraph() + "/" + NOW.strftime("%Y%m%d%H%M%S") + "-" + str(valor_entrada) + ".png", bbox_inches='tight')

    ## Mostramos Gráficos
    plt.show()
    return bool(1)

def _main_():
    ENTRADA = int(input("Escriba un numero mayor que cero: "))
    if(ENTRADA <= 0) :
        quit()

    print("Conjetura de Collatz para: ", ENTRADA)

    ##Definir Granizos para el numero de entrada
    GRANIZOS = fGranizos(ENTRADA)
    print("Granizos: ", GRANIZOS)

    graficos(ENTRADA,GRANIZOS)
    
_main_()