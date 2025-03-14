import sys
from cubo import *
from problemaRubik import *
from busqueda import *



cubo = Cubo()

print("CUBO SIN MEZCLAR:\n" + cubo.visualizar())


#Mover frontal face
cubo.mover(cubo.F)

print("CUBO resultado del movimiento F:\n" + cubo.visualizar())

movs=int(sys.argv[1])

movsMezcla = cubo.mezclar(movs)

print("MOVIMIENTOS ALEATORIOS:",movs)
for m in movsMezcla:
    print(cubo.visualizarMovimiento(m) + " ")
print()

print("CUBO INICIAL (MEZCLADO):\n" + cubo.visualizar())



# Creación de un problema
# problema = Problema(EstadoRubik(cubo), BusquedaAnchura())
# problema = Problema(EstadoRubik(cubo), BusquedaProfundidad())
# problema = Problema(EstadoRubik(cubo), BusquedaProfundidadIterativa())

# problema = Problema(EstadoRubik(cubo), BusquedaVoraz_manhattan())
# problema = Problema(EstadoRubik(cubo), BusquedaAEstrella_manhattan())
# problema = Problema(EstadoRubik(cubo), BusquedaIDA_manhattan())

# problema = Problema(EstadoRubik(cubo), BusquedaVoraz_comprueba_cara())
# problema = Problema(EstadoRubik(cubo), BusquedaAEstrella_comprueba_cara())
# problema = Problema(EstadoRubik(cubo), BusquedaIDA_comprueba_cara())


print("SOLUCION:")
opsSolucion = problema.obtenerSolucion()

if opsSolucion != None:
    for o in opsSolucion:
        print(cubo.visualizarMovimiento(o.getEtiqueta()) + " ")
        cubo.mover(o.movimiento)
    print()
    print("CUBO FINAL:\n" + cubo.visualizar())
else:
    print("no se ha encontrado solución")

