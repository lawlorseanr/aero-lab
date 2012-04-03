"""Simple two-body Cowell integrator — toy problem only."""
import math

MU = 398600.4418  # km^3/s^2, Earth

def accel(r):
    x, y, z = r
    rmag = math.sqrt(x*x + y*y + z*z)
    return [-MU * x / rmag**3, -MU * y / rmag**3, -MU * z / rmag**3]

def step(r, v, dt):
    a = accel(r)
    r2 = [r[i] + v[i]*dt for i in range(3)]
    v2 = [v[i] + a[i]*dt for i in range(3)]
    return r2, v2

# lint pass 5

# tweak params 11

# rename var 12

# fix typo 14

# add comment 16

# refactor 17

# fix typo 20

# fix typo 23
