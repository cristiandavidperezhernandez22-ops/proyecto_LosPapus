class VehicleRegistry:
    _por_id: dict = {}
    _por_nombre: dict = {}
    @classmethod
    def register(cls, identificador: str, nombre_visible: str):
        def decorador(clase):
            cls._por_id[identificador] = clase
            cls._por_nombre[nombre_visible] = clase
            clase.TYPE_ID = identificador
            clase.NOMBRE_VISIBLE = nombre_visible
            return clase
        return decorador
    @classmethod
    def tipos_disponibles(cls) -> list:
        """Para llenar el Combobox de la GUI sin hardcodear nombres."""
        return list(cls._por_nombre.keys())
    @classmethod
    def obtener_por_nombre(cls, nombre: str):
        return cls._por_nombre[nombre]
    @classmethod
    def obtener_por_id(cls, identificador: str):
        return cls._por_id[identificador]
    @classmethod
    def crear_desde_fila(cls, fila: list):
        if not fila:
            raise ValueError("Fila vacía, no se puede reconstruir un vehículo")
        Clase = cls.obtener_por_id(fila[0])
        return Clase.from_row(fila[1:])