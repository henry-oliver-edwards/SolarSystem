from Colour import Colour


class Planet:

    def __init__(self, name, size, transform=1, sm_axis=None, eccentricity=None, init_angle=0, d_angle=1, position=None,
                 colour=Colour.WHITE.value):
        self.name = name
        self.size = (size * transform)
        self.a = sm_axis
        self.e = eccentricity
        self.theta = init_angle
        self.rotation = d_angle
        self.r = None
        self.position = position
        self.colour = colour
