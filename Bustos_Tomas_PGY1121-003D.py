from os import system
import random
import statistics

trabajadores=[]
lista=[]
sueldos=[]

def salir():
    print("""
Finalizando programa...
Desarrollado por Tomás Bustos
RUT 20.948.368-8
          """)
    import sys
    sys.exit()

def generar_sueldo(trabajadores):
    sueldo1=random.randint(300000,2500000)
    sueldo2=random.randint(300000,2500000)
    sueldo3=random.randint(300000,2500000)
    sueldo4=random.randint(300000,2500000)
    sueldo5=random.randint(300000,2500000)
    sueldo6=random.randint(300000,2500000)
    sueldo7=random.randint(300000,2500000)
    sueldo8=random.randint(300000,2500000)
    sueldo9=random.randint(300000,2500000)
    sueldo10=random.randint(300000,2500000)
    sueldos={
        "sueldo1":sueldo1,
        "sueldo2":sueldo2,
        "sueldo3":sueldo3,
        "sueldo4":sueldo4,
        "sueldo5":sueldo5,
        "sueldo6":sueldo6,
        "sueldo7":sueldo7,
        "sueldo8":sueldo8,
        "sueldo9":sueldo9,
        "sueldo10":sueldo10}
    lista.append(sueldos)
    trabajadores.append(sueldos)
    print("sueldos generados exitosamente")



def estadisticas(lista,sueldos):
    for lista in sueldos:
        sueldos_max=sueldos.max()
        print(f"Sueldo mas alto:${sueldos_max}")
    for lista in sueldos:
        sueldos_min=sueldos.min()
        print(f"Sueldo mas bajo:${sueldos_min}")
    #print(f"el sueldo promedio es de:{}")

def reporte(sueldos):
    #print(f"""
    #Nombre              Sueldo base                 Descuento salud             Descuento AFP                                   Sueldo Líquido
    #1.- Juan Perez      ${sueldos['sueldo1']}        ${sueldos['sueldo1'*.07]}      ${sueldos[('sueldo1'*0.7)*.12]}       ${sueldos[('sueldo1'-(('sueldo1'*0.7)*.12))]}                """)


    f=open("reporte.csv","w")
    f.write("Nombre;Sueldo Base;Descuento salud;Descuento AFP;Sueldo líquido\n")
    for sueldos in lista:
        f.write(f"Juan Perez,${sueldos['sueldo1']}\n María Garcia,${sueldos['sueldo2']}\n Carlos Lopez,${sueldos['sueldo3']}\n Ana Martinez,${sueldos['sueldo4']}\n Pedro Rodriguez,${sueldos['sueldo5']}\n Laura Hernandez,${sueldos['sueldo6']}\n Miguel Sanchez,${sueldos['sueldo7']}\n Isabel Gomez,${sueldos['sueldo8']}\n Francisco Diaz,${sueldos['sueldo9']}\n Elena Fernandez,${sueldos['sueldo10']}\n")
        print("archivo creado exitosamente")

def ordenar():
    while True:
        print(""" ORDENAR SUELDOS 
              1.- Sueldos menores a 800.000
              2.- Sueldos entre 800.000 y 2.000.000
              3.- Sueldos superiores a 2.000.000""")
        opcion=int(input("ingrese una opcion:"))
        if opcion==1:
            pass
        elif opcion==2:
            pass
        elif opcion	==3:
            pass
        
        

while True:
    print("""
1.- Asignar sueldos aleatorios
2.- Clasificar sueldos
3.- Reporte de sueldos
4.- Ver estadísticas
5.- Salir del programa""")
    op=int(input("ingrese una opcion:"))
    if op==1:
        generar_sueldo(trabajadores)
    elif op==2:
        ordenar()
    elif op==3:
        reporte(lista)
    elif op==4:
        estadisticas()
    elif op==5:
        salir()
    else:
        print("Opción invalida!")
        break


