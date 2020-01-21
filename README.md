# Newton Open Library
## A. The Project
### 1. Basic Information
Please, find Newton library as 'Newton.py' and an example of it's use as 'example.py' (available on this rep).<br/>
This Library is a GNU GPL v2 protected program.<br/>
Programmed by Arthur DETAILLE - January 2020 (Based on Uriot 'DIMENSION' Angel's work).

### 2. Genesis
This project was made in one and only one goal: continue to teach myself basics principles of physics and to serve as a portfolio assets.<br/>
Programmed in python 3.8.x this project was made in one evening (for the basic structure) and in one other to polish and debug.

### 3. Special Thanks
- Houri M.D.
- Mamou M.D.

### 4. Deeper Instructions
You may find some other bugs. Please contact me or feel free to post you corrected version on your Git :)

## B. How to use Newton Open Library ?
### 1. Setup the Python file
**Newton Open Library** need few external libraries to work properly and the correct python version. You'll need thoese to correctly use NOL.
#### a. Python
NOL uses Python 3.8.x wich is currently the newest version available. Find deeper informations [here](https://www.python.org/)

#### b. Pillow Library
Follow the instructions on the [official website](https://pillow.readthedocs.io/en/stable/) or use pip to install PIL `pip3 install Pillow`

#### c. Create your python file
Copy and paste or download `Newton.py` on your computer and save it in a folder.
Open any IDE or text editor that you know capable of saving (and maybe execute) python 3.8.x and create a new file `[name].py` that you will save in the same folder as `Newton.py`. Then, import newton library as so : `import Newton`.

### 2. Configure `Newton.Space` object

#### a. Setup `space` object
You will need to create a `space` object to perform calculations. `Newton.Space` is a dual argument object that will store basic informations about your space (the actual object that your stars live in).

##### Two arguments :
- arg 1 : Size (Vector 2D)
- arg 2 : Gravity constant (float)

##### Example :
```python
space = Newton.Space(
  Newton.Vec2(500, 500),
  0.0001
)
```

#### b. Populate your space with stars
`Newton.Space.populate(n)` is a mono argument function part of the `Newton.Space` object.

##### One argument :
n (int) -> number of stars in your space

##### Example :
```python
space = Newton.Space(
  Newton.Vec2(500, 500),
  0.0001
)

space.populate(100)
```
