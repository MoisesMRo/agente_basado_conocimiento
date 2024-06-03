from experta import *

soft_skills = [
    "comunicacion",
    "trabajo_en_equipo",
    "creatividad",
    "resolucion_problemas",
    "organizacion",
    "liderazgo",
    "empatia",
    "atencion_al_detalle",
    "etica_profesional"
]

hard_skills = [
    "desarrollo_software",
    "seguridad_informatica",
    "gestion_redes",
    "estrategias_marketing",
    "analisis_datos",
    "gestion_campañas",
    "gestion_cadena_suministro",
    "control_calidad",
    "mejora_procesos",
    "gestion_recursos_humanos",
    "legislacion_laboral",
    "sistemas_rrhh",
    "contabilidad"
]

certificaciones = [
    "certificado_TI",
    "certificado_marketing",
    "certificado_operaciones",
    "certificado_rrhh",
    "certificado_finanzas"
]


# Definición de los hechos de la empresa y postulante
class Empresa(Fact):
    nombre = Field(str)
    area = Field(str)
    vacantes_ofrecidas = Field(int)

class Postulante(Fact):
    nombre = Field(str)
    habilidades_blandas = Field(list)
    habilidades_duras = Field(list)
    area_postulacion = Field(str)
    certificaciones = Field(list)

# Motor de conocimiento para la selección de practicantes
class SeleccionPracticante(KnowledgeEngine):
    seleccionados = []
    no_seleccionados = []

    def __init__(self):
        super().__init__()
        self.vacantes_restantes = {}

    @Rule(AND(
        Empresa(nombre=MATCH.nombreEmpresa, area="TI", vacantes_ofrecidas=MATCH.vacantes),
        Postulante(nombre=MATCH.nombrePostulante, habilidades_blandas=MATCH.blandas, habilidades_duras=MATCH.duras, area_postulacion="TI", certificaciones=MATCH.certificaciones),
        TEST(lambda duras: all(skill in duras for skill in ["desarrollo_software", "seguridad_informatica", "gestion_redes"])),
        TEST(lambda blandas: "comunicacion" in blandas and "trabajo_en_equipo" in blandas)
    ))
    def seleccionar_practicante_ti(self, nombreEmpresa, nombrePostulante, certificaciones, vacantes):
        puntos = 5
        if "certificado_TI" in certificaciones:
            puntos += 2
        if self.vacantes_restantes[nombreEmpresa] > 0:
            self.seleccionados.append((nombrePostulante, nombreEmpresa, "TI", puntos))
            self.vacantes_restantes[nombreEmpresa] -= 1
        else:
            self.no_seleccionados.append((nombrePostulante, nombreEmpresa, "TI", puntos))

    @Rule(AND(
        Empresa(nombre=MATCH.nombreEmpresa, area="Marketing", vacantes_ofrecidas=MATCH.vacantes),
        Postulante(nombre=MATCH.nombrePostulante, habilidades_blandas=MATCH.blandas, habilidades_duras=MATCH.duras, area_postulacion="Marketing", certificaciones=MATCH.certificaciones),
        TEST(lambda duras: all(skill in duras for skill in ["estrategias_marketing", "analisis_datos", "gestion_campañas"])),
        TEST(lambda blandas: "creatividad" in blandas and "comunicacion" in blandas)
    ))
    def seleccionar_practicante_marketing(self, nombreEmpresa, nombrePostulante, certificaciones, vacantes):
        puntos = 5
        if "certificado_marketing" in certificaciones:
            puntos += 2
        if self.vacantes_restantes[nombreEmpresa] > 0:
            self.seleccionados.append((nombrePostulante, nombreEmpresa, "Marketing", puntos))
            self.vacantes_restantes[nombreEmpresa] -= 1
        else:
            self.no_seleccionados.append((nombrePostulante, nombreEmpresa, "Marketing", puntos))

    @Rule(AND(
        Empresa(nombre=MATCH.nombreEmpresa, area="Operaciones", vacantes_ofrecidas=MATCH.vacantes),
        Postulante(nombre=MATCH.nombrePostulante, habilidades_blandas=MATCH.blandas, habilidades_duras=MATCH.duras, area_postulacion="Operaciones", certificaciones=MATCH.certificaciones),
        TEST(lambda duras: all(skill in duras for skill in ["gestion_cadena_suministro", "control_calidad", "mejora_procesos"])),
        TEST(lambda blandas: "resolucion_problemas" in blandas and "organizacion" in blandas)
    ))
    def seleccionar_practicante_operaciones(self, nombreEmpresa, nombrePostulante, certificaciones, vacantes):
        puntos = 5
        if "certificado_operaciones" in certificaciones:
            puntos += 2
        if self.vacantes_restantes[nombreEmpresa] > 0:
            self.seleccionados.append((nombrePostulante, nombreEmpresa, "Operaciones", puntos))
            self.vacantes_restantes[nombreEmpresa] -= 1
        else:
            self.no_seleccionados.append((nombrePostulante, nombreEmpresa, "Operaciones", puntos))

    @Rule(AND(
        Empresa(nombre=MATCH.nombreEmpresa, area="Recursos Humanos", vacantes_ofrecidas=MATCH.vacantes),
        Postulante(nombre=MATCH.nombrePostulante, habilidades_blandas=MATCH.blandas, habilidades_duras=MATCH.duras, area_postulacion="Recursos Humanos", certificaciones=MATCH.certificaciones),
        TEST(lambda duras: all(skill in duras for skill in ["gestion_recursos_humanos", "legislacion_laboral", "sistemas_rrhh"])),
        TEST(lambda blandas: "liderazgo" in blandas and "empatia" in blandas)
    ))
    def seleccionar_practicante_rrhh(self, nombreEmpresa, nombrePostulante, certificaciones, vacantes):
        puntos = 5
        if "certificado_rrhh" in certificaciones:
            puntos += 2
        if self.vacantes_restantes[nombreEmpresa] > 0:
            self.seleccionados.append((nombrePostulante, nombreEmpresa, "Recursos Humanos", puntos))
            self.vacantes_restantes[nombreEmpresa] -= 1
        else:
            self.no_seleccionados.append((nombrePostulante, nombreEmpresa, "Recursos Humanos", puntos))

    @Rule(AND(
        Empresa(nombre=MATCH.nombreEmpresa, area="Finanzas", vacantes_ofrecidas=MATCH.vacantes),
        Postulante(nombre=MATCH.nombrePostulante, habilidades_blandas=MATCH.blandas, habilidades_duras=MATCH.duras, area_postulacion="Finanzas", certificaciones=MATCH.certificaciones),
        TEST(lambda duras: all(skill in duras for skill in ["contabilidad", "gestion_cadena_suministro"])),
        TEST(lambda blandas: "atencion_al_detalle" in blandas and "organizacion" in blandas)
    ))
    def seleccionar_practicante_finanzas(self, nombreEmpresa, nombrePostulante, certificaciones, vacantes):
        puntos = 5
        if "certificado_finanzas" in certificaciones:
            puntos += 2
        if self.vacantes_restantes[nombreEmpresa] > 0:
            self.seleccionados.append((nombrePostulante, nombreEmpresa, "Finanzas", puntos))
            self.vacantes_restantes[nombreEmpresa] -= 1
        else:
            self.no_seleccionados.append((nombrePostulante, nombreEmpresa, "Finanzas", puntos))

    def ordenar_seleccionados(self):
        self.seleccionados.sort(key=lambda x: x[3], reverse=True)
        return self.seleccionados

# Función para ingresar los datos de los postulantes por teclado
def ingresar_datos_postulante():
    nombre = input("Ingrese el nombre del postulante: ")
    area_postulacion = input("Ingrese el área de postulación del postulante: ")
    habilidades_blandas = input("Ingrese las habilidades blandas del postulante (separadas por coma): ").split(",")
    habilidades_duras = input("Ingrese las habilidades duras del postulante (separadas por coma): ").split(",")
    certificaciones = input("Ingrese las certificaciones del postulante (separadas por coma): ").split(",")
    
    return Postulante(
        nombre=nombre.strip(),
        habilidades_blandas=[habilidad.strip() for habilidad in habilidades_blandas],
        habilidades_duras=[habilidad.strip() for habilidad in habilidades_duras],
        area_postulacion=area_postulacion.strip(),
        certificaciones=[certificacion.strip() for certificacion in certificaciones]
    )

# Inicialización del motor de reglas
engine = SeleccionPracticante()

# Declaración de empresas
empresas = [
    Empresa(nombre="Empresa1", area="TI", vacantes_ofrecidas=2),
    Empresa(nombre="Empresa2", area="Marketing", vacantes_ofrecidas=1),
    Empresa(nombre="Empresa3", area="Operaciones", vacantes_ofrecidas=1),
    Empresa(nombre="Empresa4", area="Recursos Humanos", vacantes_ofrecidas=1),
    Empresa(nombre="Empresa5", area="Finanzas", vacantes_ofrecidas=1)
]

for empresa in empresas:
    engine.declare(empresa)
    engine.vacantes_restantes[empresa['nombre']] = empresa['vacantes_ofrecidas']

print("**************************************************************")
print("BIENVENIDO AL PROGRAMA DE AYUDA A LA SELECCION DE PRACTICANTES")
print("**************************************************************\n")
# Bucle para ingresar postulantes y ejecutar el motor de reglas
while True:
    postulantes = []

    for postulante in postulantes:
        engine.declare(postulante)

    # Ingresar datos de postulante por teclado
    postulante = ingresar_datos_postulante()
    engine.declare(postulante)

    # Ejecutar el motor de reglas
    engine.run()

    # Ordenar seleccionados por puntaje y mostrar resultados
    seleccionados_finales = engine.ordenar_seleccionados()

    if seleccionados_finales==[]:
        print(f"\n>> No has sido Seleccionado")

    for seleccionado in seleccionados_finales:
        print(f"\n>> Felicitaciones a sido seleccionado: {seleccionado}")

    # Mostrar no seleccionados
    for no_seleccionado in engine.no_seleccionados:
        print(f"\n>> No has sido Seleccionado: {no_seleccionado}")

    # Preguntar si se desea continuar o salir
    print("\n")
    print("*"*60)
    continuar = input("\n¿Desea continuar ingresando postulantes? (s/n): ")
    if continuar.lower() != 's':
        break
