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

# test tweak 10

# rename var 18

# doc touch 19

# rename var 22

# rename var 28

# doc touch 33

# doc touch 34

# doc touch 38

# add comment 39

# refactor 41

# test tweak 44

# fix typo 46

# doc touch 51

# rename var 52

# refactor 57

# test tweak 58
