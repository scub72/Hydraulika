
# Calculates the velocity with given:
# - flow [l/min]
# - diameter [mm]
#
#   calculation result is velocity in [m/s]


def calculateVelocity( flow, diameter):
    velocity = flow/1000.0/60.0/(3.14*pow(diameter/1000.0, 2)/4.0)
    return velocity


