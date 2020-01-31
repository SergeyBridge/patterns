import random
from unittest import TestCase
import tkinter as tk


class System:
    def __init__(self, map_):
        self.map_ = map_  # self.grid = [[0 for i in range(30)] for _ in range(20)]
        # self.map_[5][7] = 1  # Источники света
        # self.map_[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map_)


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class MappingAdapter:
    def __init__(self, adapt):
        self._adapt = adapt

    @staticmethod
    def _transform_grid(grid_transposed, event):
        result = []
        for i in range(grid_transposed[0]):
            for j in range(grid_transposed[1]):
                if grid_transposed[i][j] == event:
                    result.append((i, j))
        return result

    def lighten(self, grid):
        grid_transposed = [
            [row[i] for row in grid] for i in range(grid[0])
        ]
        self._adapt.set_lights(self._transpose_grid(grid_transposed, 1))
        self._adapt.set_obstacles(self._transpose_grid(grid_transposed, -1))
        return self._adapt.generate_lights()


def get_curr_screen_geometry():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    geometry = root.winfo_geometry()
    root.destroy()
    geometry = tuple(geometry.replace("+", "x").split("x")[:2])
    return geometry


# class unitestLight(TestCase):
#    def test_generate_lights(self):
#        self.assertEqual()


if __name__ == "__main__":
    map_ = [[random.choice([-1, 1]) for i in range(30)] for _ in range(20)]

    system = System()
    light = Light(dim=(800, 600))
    adapter = MappingAdapter(light)
    system.get_lightening(adapter)
