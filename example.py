import Newton

space = Newton.Space(
    Newton.Vec2(500, 500),                          # univer's size -> Vec2(xSize, ySize)
    0.0001                                          # gravity constant
)

space.populate(200)                                 # populate space with n=200 stars

renderer = Newton.Renderer(
    "render_500x500_450f_0-0001g_5dt_200s",         # file name
    1                                               # Adjusting rendered image scale
)

sim = Newton.Simulation(
    5,                                              # steps computed each frames
    450,                                            # numbers of frame (at 30 fps)
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
# compute this simulation in 30 to 32 seconds.
# ################################
