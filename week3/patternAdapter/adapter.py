class MappingAdapter:
    def __init__(self, adapt):
        self._adapt = adapt

    @staticmethod
    def _transform_grid(grid_, event):
        result = []
        for i, raw in enumerate(grid_):
            for j, el in enumerate(raw):
                if el == event:
                    result.append((j, i))

        return result

    def lighten(self, grid):
        self._adapt.set_dim((len(grid[0]), len(grid)))

        self._adapt.set_lights(self._transform_grid(grid, 1))
        self._adapt.set_obstacles(self._transform_grid(grid, -1))

        result = self._adapt.generate_lights()
        return result

