class Measurement:
    def __init__(
        self, value=None, required=True, unit='cm'
    ):
        self.value = value
        self.required = required
        self.unit = unit

    def __str__(self):
        r = '(opcional)' if not self.required else ''
        return f'{self.value}{self.unit} {r}'

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value