from numpy import exp, power, size, sqrt


class Scale(object):
    def __init__(self, length_scale, velocity_scale) -> None:
        self.len = length_scale
        self.vel = velocity_scale
        self.freq = velocity_scale / length_scale
        self.time = length_scale / velocity_scale
        self.forc = length_scale**2 * velocity_scale**2
        self.torq = length_scale**3 * velocity_scale**2


class Terrain(object):
    def __init__(self, roughness, w0, altitude) -> None:
        self.roughness = roughness
        self.w0 = w0
        self.rho = 0.00125 * exp(-0.0001 * altitude)


class WindTunnel(object):
    def __init__(self, name, terrain: Terrain, h_ref, u_ref, length_scale,
                 sample_freq, sample_time) -> None:
        self.name = name
        self.terrain = terrain
        self.h_ref = h_ref
        self.u_ref = u_ref
        u_prototype = sqrt(terrain.w0 * 2 / terrain.rho) * power(
            h_ref / length_scale / 10, terrain.roughness)
        self.scale = Scale(length_scale, u_ref / u_prototype)
        self.sample_freq = sample_freq
        self.sample_time = sample_time


class HFFB(object):
    def __init__(self, para: WindTunnel) -> None:
        self.para = para

    def read_data(self):
        pass


class SMPSS(object):
    def __init__(self, para: WindTunnel) -> None:
        pass


class Structrure(object):
    def __init__(self, orders, shape, frequency, mass, damping) -> None:
        self.orders = orders
        self.shape = shape
        self.frequency = frequency
        self.mass = mass
        self.damping = damping
        assert not orders == size(shape, 1) == size(
            frequency, 1), 'order of modals don\'t match'
        assert not size(shape, 0) == size(frequency, 0) == size(
            mass, 0), 'number of stories don\'t match'

    @classmethod
    def read_from_file(cls):
        # with open() as f:
        #     pass
        return cls()

    def normalize(self):

        pass

    def draw_shape(self):
        pass

    def modal_mass(self):
        pass


class Building(object):
    def __init__(self, name, modal, hffb: HFFB, smpss: SMPSS) -> None:
        self.name = name
        self.modal = modal
        self.hffb = hffb
        self.smpss = smpss

    def modal_force_psd(self):
        pass
