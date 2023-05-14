class Figure:
    def __init__(self, name: str):
        self.name = name

    @property
    def area(self) -> float:
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        raise ValueError(f'Object {figure} is not subclass of Figure class')
