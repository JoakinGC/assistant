from graphviz import Digraph

# Crear un nuevo objeto Digraph
dot = Digraph(comment='Mapa Mental: Permiso B en Lectura Fácil')

# Nodo principal
dot.node('Permiso B', 'Permiso B en Lectura Fácil')

# Temas
temas = [
    "Definiciones",
    "Documentación",
    "El estado del conductor",
    "Obligaciones de conductores y peatones",
    "Dispositivos de seguridad en el vehículo",
    "Elementos del vehículo y normas para usarlos",
    "Sistema de luces de los vehículos",
    "Señales de circulación",
    "La vía",
    "Velocidad y distancias",
    "Maniobras",
    "Normas de preferencia para circular",
    "Transportar personas y cargas",
    "Conducir de forma segura",
    "Mecánica y mantenimiento del vehículo",
    "Accidentes de tráfico",
    "Conducción preventiva y eficiente",
    "Anexo puntos: El permiso de conducir por puntos"
]

# Añadir los temas como nodos y conectarlos al nodo principal
for tema in temas:
    dot.node(tema, tema)
    dot.edge('Permiso B', tema)

# Subtemas para algunos temas (ejemplo)
subtemas_definiciones = [
    "Vehículos sin motor", 
    "Vehículos a motor", 
    "Otro tipo de vehículos con motor",
    "Conductor",
    "Peatón",
    "Titular del vehículo",
    "Conductor habitual",
    "Categorías de los vehículos dependiendo de su uso"
]

# Añadir subtemas al tema Definiciones
for subtema in subtemas_definiciones:
    dot.node(subtema, subtema)
    dot.edge("Definiciones", subtema)

# Renderizar el gráfico
dot.render('mapa_mental_permisob.gv', view=True)
