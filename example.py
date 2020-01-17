import Newton
import os

space = Newton.Space(
    Newton.Vec2(800, 600),                          # univer's size -> Vec2(xSize, ySize)
    0.001                                           # gravity constant
)

space.populate(500)                                 # populate space with n=500 stars

renderer = Newton.Renderer(
    "final_render",                                 # file name
    1                                               # Adjusting rendered image scale
)

sim = Newton.Simulation(
    1,                                              # steps computed each frames
    100,                                            # numbers of frame (at 30 fps)
    space,                                          # space to compute reference
    renderer                                        # renderer reference
)

sim.simulate()                                      # start simulation of var space

print()
input("Press ENTER to continue...")