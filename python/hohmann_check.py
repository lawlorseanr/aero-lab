"""Hohmann transfer delta-v check between circular orbits."""
import math

def hohmann_dv(r1, r2, mu):
    a = (r1 + r2) / 2
    v1 = math.sqrt(mu / r1)
    vp = math.sqrt(mu * (2/r1 - 1/a))
    va = math.sqrt(mu * (2/r2 - 1/a))
    v2 = math.sqrt(mu / r2)
    return (vp - v1, v2 - va)

# doc touch 6

# cleanup 8

# test tweak 9
