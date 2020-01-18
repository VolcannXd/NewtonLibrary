import Newton

space = Newton.Space(
    Newton.Vec2(800, 600),                          # univer's size -> Vec2(xSize, ySize)
    0.001                                           # gravity constant
)

space.populate(200)                                 # populate space with n=100 stars

renderer = Newton.Renderer(
    "render_800x600_350f_10dt",                     # file name
    1                                               # Adjusting rendered image scale
)

sim = Newton.Simulation(
    10,                                             # steps computed each frames
    350,                                            # numbers of frame (at 30 fps)
    space,                                          # space to compute reference
    renderer,                                       # renderer reference
)

sim.simulate()                                      # start simulation of var space

print()
input("Press ENTER to continue...")
