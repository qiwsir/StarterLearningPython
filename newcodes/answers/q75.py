#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Particle:
    def __init__(self, name="", position=(0.0, 0.0, 0.0), velocity=(0.0, 0.0, 0.0), spin=0.0):
        self.position = position
        self.velocity = velocity
        self.name = name
        self.spin = spin
    def __str__(self):
        pos = "({0:.2f}:{1:.2f}:{2:.2f})".format(self.position[0], self.position[1], self.position[2])
        vel = "({0:.2f}:{1:.2f}:{2:.2f})".format(self.velocity[0], self.velocity[1], self.velocity[2])
        the_str = "{0}\n at {1}\n with velocity {2}\n and spin {3}\n".format(self.name, pos, vel, self.spin)
        return the_str

class MassParticle(Particle):
    def __init__(self, name="", position=(0.0, 0.0, 0.0), velocity=(0.0, 0.0, 0.0), spin=0.0, mass=0.0):
        super(MassParticle, self).__init__(name, position, velocity, spin)
        self.mass = mass
    def __str__(self):
        temp_str = super(MassParticle, self).__str__()
        temp_str = temp_str + " and mass {0}\n".format(self.mass)
        return temp_str

class ChargeParticle(MassParticle):
    def __init__(self, name="", position=(0.0, 0.0, 0.0), velocity=(0.0, 0.0, 0.0), spin=0.0, mass=0.0, charge=0.0):
        super(ChargeParticle, self).__init__(name, position, velocity, spin, mass)
        self.charge = charge
    def __str__(self):
        temp_str = super(MassParticle, self).__str__()
        temp_str = temp_str + " and charge {0}".format(self.charge)
        return temp_str

if __name__ == "__main__":
    photon = Particle(name="photon", spin=1.0)
    tau = ChargeParticle(name="tau", spin=0.5, charge=-1.0, mass=1.777)
    print(photon)
    print(tau)
