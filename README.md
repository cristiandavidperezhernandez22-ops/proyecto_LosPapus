# proyecto_LosPapus

### No hables de /c/
### NO se habla de /c/
### Somos /c/
### /c/ es legión
### /c/ nunca perdona 



Sistema de gestión de una concesionaria de vehículos, desarrollado como proyecto académico para practicar **Programación Orientada a Objetos** en Python: herencia, clases abstractas, enums y patrones de diseño (Registry).

## Descripción

El proyecto modela distintos tipos de vehículos (`Car`, `Truck`, `Motorbike`, `Tractor`) que heredan de una clase base común (`Vehicle`), y una clase `Concessionarie` que actúa como contenedor central: cada vehículo que se crea se registra automáticamente en ella, sin necesidad de agregarlo a mano.

## Estructura del proyecto

```
proyecto_LosPapus/
├── __init__.py
├── main.py                    # Punto de entrada del programa
├── logic/
│   ├── __init__.py
│   └── Concessionarie.py      # Contenedor y lógica de búsqueda de vehículos
├── model/
│   ├── __init__.py
│   ├── Vehicle.py             # Clase base abstracta
│   ├── Car.py
│   ├── Truck.py
│   ├── Motorbike.py
│   └── Tractor.py
├── utils/
│   ├── __init__.py
│   ├── Car_type.py            # Enum: COMPACT, PICKUP, SUV
│   ├── Charge_capacity.py     # Enum: LIGHT, MEDIUM, HEAVY
│   └── Fuel_type.py           # Enum: DIESEL, ELECTRIC, GASOLINE
└── view/                      # (en construcción) interfaz de usuario
```

## Cómo ejecutar

Este proyecto usa **imports relativos**, por lo que debe ejecutarse como módulo desde la carpeta que **contiene** `proyecto_LosPapus` (no desde dentro de ella).

```bash
# Párate en la carpeta padre del proyecto
cd ruta/a/la/carpeta/que/contiene/proyecto_LosPapus

# Ejecuta como módulo
python -m proyecto_LosPapus.main
```

> No se puede ejecutar dando "Run" directamente sobre ningún archivo dentro del proyecto (ni `main.py`, ni `Car.py`, etc.) — los imports relativos requieren que Python reconozca el paquete completo, algo que solo pasa al invocarlo con `-m`.

## Componentes principales

### `Vehicle` (clase base abstracta)
Define los atributos comunes a todo vehículo: número de llantas, capacidad de carga, tipo de combustible, pasajeros, marca y precio. Al ser `ABC`, no puede instanciarse directamente — solo a través de sus subclases.

### Subclases de `Vehicle`
| Clase | Atributos propios |
|---|---|
| `Car` | `doors`, `trunk_capacity`, `has_air_conditioning`, `car_type` |
| `Truck` | `doors`, `trunk_capacity`, `has_air_conditioning` |
| `Motorbike` | (sin atributos adicionales) |
| `Tractor` | `doors`, `has_air_conditioning` (llantas y pasajeros fijos por diseño) |

### `Concessionarie`
Actúa como contenedor de vehículos con auto-registro:

```python
from proyecto_LosPapus.logic.Concessionarie import Concessionarie
from proyecto_LosPapus.model import Car, Tractor

concesionaria = Concessionarie()

Car(brand="Toyota")          # se registra solo, sin llamar .add()
Tractor(brand="John Deere")  # se registra solo

print(concesionaria.find(Car))              # [Car(brand='Toyota', ...)]
print(concesionaria.find(Car, Tractor))     # ambos
print(len(concesionaria))                    # 2
```

**Métodos disponibles:**
- `add(vehicle)` — agrega un vehículo manualmente
- `remove(vehicle)` — elimina un vehículo
- `find(*vehicle_classes)` — filtra vehículos por una o varias clases, usando `isinstance()`
- Soporta iteración directa (`for v in concesionaria`) y `len(concesionaria)`

### Auto-registro (patrón Registry)
`Vehicle` mantiene una referencia estática (`_registry`) a la `Concessionarie` activa. Cuando se crea cualquier vehículo, su constructor revisa si hay un registro activo y se agrega solo. Esto elimina la necesidad de llamar `.add()` manualmente cada vez.

> **Limitación conocida:** como `_registry` es un atributo de clase compartido por todos los `Vehicle`, solo puede existir una `Concessionarie` "activa" a la vez. Si se crea una segunda instancia, la primera deja de recibir nuevos vehículos automáticamente.

## Tecnologías

- Python 3.14
- `abc` (clases abstractas)
- `enum` (tipos de combustible, capacidad de carga, tipo de auto)

## Pendientes / mejoras futuras

- [ ] Interfaz de usuario en `view/` (menú por consola)
- [ ] Métodos abstractos en `Vehicle` para forzar comportamiento en subclases
- [ ] Validaciones de datos (precios negativos, cantidades inválidas, etc.)
- [ ] `__repr__` personalizado por subclase
