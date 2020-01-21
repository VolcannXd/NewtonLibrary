import Newton

space = Newton.Space(
    Newton.Vec2(750, 1000),                         # univer's size -> Vec2(xSize, ySize)
    0.0000000006674                                 # gravity constant
)

space.setConfig(Newton.SimConfig.RANDOM_POSITION_AND_ROTATION)     # Set Stars Behavior

space.populate(500)                                 # populate space with n=200 stars

renderer = Newton.Renderer(
    "render_500s_0-5dt_400f_750x1000_v1",           # file name
    1                                               # Adjusting rendered image scale
)

sim = Newton.Simulation(
    0.5,                                            # time step
    400,                                            # numbers of frame (at 30 fps)
    space,                                          # space to compute reference
    renderer,                                       # renderer reference
)

sim.simulate()                                      # start simulation

print()
input("Press ENTER to continue...")

# ################################
# SIDE NOTE :
# ################################
# With those parameters my CPU (Intel I5-6600K 3.5Ghz)
# compute this simulation in about 2 minutes and 30 seconds
# ################################
