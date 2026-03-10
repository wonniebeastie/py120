class SmartLamp:
    def __init__(self, color):
        self.color = color

    def glow(self):
        return (f'The lamp glows {self.color}.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color

