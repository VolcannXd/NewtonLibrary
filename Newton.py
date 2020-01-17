# ###############################
# NEWTON LIBRARY
# ###############################
# Open source library for computing gravity simulation
# Save as Images sequences or video files
#
# Licence CC BY-NC-SA
# Arthur Detaille - january 2020
# Based on Uriot 'DIMENSION' Anglel's work

# ###############################
# IMPORT
# ###############################

# Utilities: Simulation & stuff
import math                             # Math
import random                           # Random

# Rendering Managment
import PIL                              # PILLOW: Python Imaginary Library
from PIL import Image                   # PILLOW: Python Imaginary Library's Image module
from PIL import ImageDraw               # PILLOW: Python Imaginary Library's ImageDraw module

# Image Saving Managment
from datetime import date, datetime     # DateTime: date & dateTime
import time
import os                               # OS: import for directory managment

# ###############################
# STAR OBJECT
# ###############################
class Star:
    def __init__(self, x, y, minMass, MaxMass) :
        self.x = x
        self.y = y
        self.minMass = minMass
        self.MaxMass = MaxMass
        self.mass = random.randint(minMass, MaxMass)

    def move(self, space) :
        for star in space.stars :
            if star != self :
                distance = math.sqrt((star.x - self.x) * (star.x - self.x) + (star.y - self.y) * (star.y - self.y))
                
                force = space.gravity * ((star.mass * self.mass) / (distance * distance))

                direction = Vec2(
                    star.x - self.x,
                    star.y - self.y
                )

                self.x += direction.x * force
                self.y += direction.y * force

    def draw(self, g, scale) :
        # Draw a white point on g at (self.x * scale, self.y * scale)
        px = self.x * scale
        py = self.y * scale

        ellipseScale = 20

        shape = [
            (
                px - math.ceil(self.mass / ellipseScale),
                py - math.ceil(self.mass / ellipseScale)
            ),
            (
                px + math.ceil(self.mass / ellipseScale),
                py + math.ceil(self.mass / ellipseScale)
            )
        ]

        g.ellipse(shape, fill="white")

# ###############################
# VECTOR 2D OBJECT
# ###############################
class Vec2:
    # Vector 2D Class
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def normalizeVec2(self, x, y) :
        # Return vector2D norm. Don't need it but it's just in case...
        return math.sqrt(x*x + y*y)

    def logVector2d(self) :
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Space:
    # Space Class
    def __init__(self, size, gravity) :
        self.size = size
        self.gravity = gravity
        self.stars = []

    def populate(self, n) :
        for i in range(0, n) :

            # Assign random position for each stars in x:[0, Space.size] and y:[0, Space.size]
            x = random.random() * self.size.x
            y = random.random() * self.size.y

            star = Star(
                x,
                y,
                10,
                100
            )

            self.stars.append(star)

    def update(self) :
        for star in self.stars :
            star.move(self)
            pass

# ###############################
# RENDERER OBJECT
# ###############################
class Renderer:
    def __init__(self, filename, scale) :
        self.filename = filename
        self.scale = scale
        self.frame = 0
        self.frames = []

    def renderHasGif(self) :
        self.frames[0].save(self.filename + '.gif', format='GIF', append_images=self.frames[1:], save_all=True, duration=50, loop=0)

    def computeCache(self, space) :
        # Setting up image for rendering
        img = Image.new(
            mode = "RGB",
            size = (space.size.x * self.scale, space.size.y * self.scale)
        )

        for i in range(0, len(space.stars)) :
            g = PIL.ImageDraw.Draw(img)
            space.stars[i].draw(g, self.scale)

        self.frames.append(img)
        self.frame += 1

        logInfos = "'" + self.filename + "' cached."
        return logInfos

# ###############################
# SIMULATION OBJECT
# ###############################
class Simulation:
    def __init__(self, deltaTime, frames, space, renderer) :
        self.deltaTime = deltaTime
        self.frames = frames
        self.space = space
        self.renderer = renderer

    def simulate(self) :
        start_time = time.time()
        print("LOG: Start simulation caching...")
        for f in range(0, self.frames) :
            for dt in range(0, self.deltaTime) :
                self.space.update()

            self.renderer.computeCache(self.space)

            frameCount = "[" + str(f) + "/" + str(self.frames) + "]"
            print("LOG: simulation cycle completed. " + frameCount)
        
        elapsed_time = time.time() - start_time
        elapsed_time_logged = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print("LOG: Caching done. Time elapsed: " + elapsed_time_logged)

        self.renderer.renderHasGif()
        print("LOG: Render done.")

# ###############################
# LOADING LOG
# ###############################
print("LOG: Newton library correctly imported.")