class Conductor:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia
        self.horarios = []  # Lista de horarios asignados

    def asignar_horario(self, horario):
        if horario in self.horarios:
            return False  # El horario ya está asignado
        self.horarios.append(horario)
        return True

    def __str__(self):
        return f"Conductor: {self.nombre}, Licencia: {self.licencia}, Horarios: {self.horarios}"


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []  # Lista de horarios asignados al bus
        self.conductor = None  # Conductor asignado

# todavia me falta profesor  el jueves lo envio todo hecho 