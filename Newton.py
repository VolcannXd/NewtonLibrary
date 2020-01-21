# ###############################
# NEWTON LIBRARY
# ###############################
# Open source library for computing gravity simulation
# Save as Images sequences or video files
#
# Licence CC BY-NC-SA
# Arthur Detaille - january 2020
# Based on Uriot 'DIMENSION' Angel's work

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
from PIL import ImageFont

# Image Saving Managment
from datetime import date, datetime     # DateTime: date & dateTime
import time
import os                               # OS: import for directory managment

# ###############################
# UNIVERS CONFIGURATION OBJECT
# ###############################
class SimConfig:
    RANDOM_POSITION_AND_ROTATION = 0
    ROTATE_AROUND = 1

# ###############################
# STAR OBJECT
# ###############################
class Star:
    def __init__(self, position, minMass, MaxMass, behavior) :
        self.position = position
        self.minMass = minMass
        self.MaxMass = MaxMass
        self.mass = random.randint(minMass, MaxMass)

        self.pastPosition = Vec2

        self.speed = Vec2(0, 0)

        self.speed = self.initStarBehavior(behavior)

        self.color = (
            255,
            random.randint(0, 255),
            random.randint(0, 10)
        )

    def initStarBehavior(self, behavior) :
        if behavior == SimConfig.ROTATE_AROUND   : return Vec2.computeDirectionToPointAfromB(self.position, Vec2(500, 500)).rotateVector2d(0.5 * math.pi).MultiplyDouble(0.2)
        else : return Vec2(random.random(), random.random())


    def draw(self, g, scale) :
        # Draw a white point on g at (self.x * scale, self.y * scale)
        # scale (float) represent grid scale
        px = self.position.x * scale
        py = self.position.y * scale

        shapeScale = self.minMass * 7

        # define shape
        shape = [
            (
                px - math.ceil(self.mass / shapeScale),
                py - math.ceil(self.mass / shapeScale)
            ),
            (
                px + math.ceil(self.mass / shapeScale),
                py + math.ceil(self.mass / shapeScale)
            )
        ]

        g.ellipse(shape, fill=self.color)

    def computeForce(self, star, space) :
        distance = math.sqrt((star.position.x - self.position.x) * (star.position.x - self.position.x) + (star.position.y - self.position.y) * (star.position.y - self.position.y))
        force = space.gravity * ((star.mass * self.mass) / (distance * distance))

        return force

    def computeDirection(self, star) :
        dir = Vec2(
            star.position.x - self.position.x,
            star.position.y - self.position.y
        )

        return dir

    def computeAcceleration(self, space) :
        Forces = Vec2(0, 0)
        for star in space.stars :
            if star != self :
                # Prevent Runtime error : Division by zero
                force = self.computeForce(star, space)
                Forces.AddVec2d(
                    self.computeDirection(star).MultiplyDouble(force)
                )

        acc =  Forces.DivideConstBySelf(self.mass)

        return acc

    def move(self, space) :
        self.speed.AddVec2d(self.computeAcceleration(space)).MultiplyDouble(space.deltaTime)

        self.position.AddVec2d(self.speed)

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

    def computeDirectionToPointAfromB(A, B) :
        return Vec2(
            A.x - B.x,
            A.y - B.y
        )

    def AddVec2d(self, vec) :
        self.x += vec.x
        self.y += vec.y
        return self

    def SubVec2d(self, vec) :
        self.x -= vec.x
        self.y -= vec.y
        return self

    def MultiplyVec2d(self, vec) :
        self.x *= vec.x
        self.y *= vec.y
        return self

    # SCALAR PRODUCT OF VECTOR (self)
    def MultiplyDouble(self, double) :
        self.x *= double
        self.y *= double
        return self

    def DivideConstBySelf(self, const) :
        const / self.x
        const / self.y
        return self

    def rotateVector2d(self, alpha) :
        return Vec2(
            math.cos(alpha) * self.x - math.sin(alpha) * self.y,
            math.cos(alpha) * self.x + math.sin(alpha) * self.y
        )

class Space:
    # Space Class
    def __init__(self, size, gravity) :
        self.size = size
        self.gravity = gravity
        self.stars = []
        self.deltaTime = 0
        self.config = SimConfig.RANDOM_POSITION_AND_ROTATION

    def setConfig(self, config) :
        self.config = config

    def populate(self, n) :
        for i in range(0, n) :

            # Assign random position for each stars in x:[0, Space.size] and y:[0, Space.size]
            x = random.random() * self.size.x
            y = random.random() * self.size.y

            star = Star(
                Vec2(x, y),     # Postion
                10000,          # Minimal position
                100000,         # Maximal position
                self.config
            )

            self.stars.append(star)

    def update(self) :
        for star in self.stars :
            star.move(self)

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
        self.frame += 1
        # Setting up image for rendering
        img = Image.new(
            mode = "RGB",
            size = (space.size.x * self.scale, space.size.y * self.scale)
        )

        # Draw module reference
        g = PIL.ImageDraw.Draw(img)

        for i in range(0, len(space.stars)) :
            space.stars[i].draw(g, self.scale)

        g.text((10, 10), self.filename + " | frame #" + str(self.frame), font=ImageFont.truetype("arial"))
        g.text((10, 25), "Newton library (open source) by Arthur Detaille", font=ImageFont.truetype("arial"))

        self.frames.append(img)

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
        space.deltaTime = self.deltaTime

    def simulate(self) :
        start_time = time.time()
        print("#######################################")
        print("FILE : " + self.renderer.filename + ".gif")
        print("#######################################")
        print("LOG: Start simulation caching...")
        for f in range(0, self.frames) :
            sim = self
            self.space.update()
            self.renderer.computeCache(self.space)

            frameCount = "[" + str(f + 1) + "/" + str(self.frames) + "]"
            print("LOG: Cached " + frameCount)

        elapsed_time = time.time() - start_time
        elapsed_time_logged = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print("#######################################")
        print("LOG: Caching done. Time elapsed: " + elapsed_time_logged)

        print("LOG: Start rendering")
        self.renderer.renderHasGif()
        print("LOG: Render done. Saved as: '" + self.renderer.filename + ".gif'")

# ###############################
# LOADING LOG
# ###############################
print("LOG: Newton library correctly imported.")
