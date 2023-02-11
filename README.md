# Rubick's Cube Solver

## Rubik's Cube Encoding

### Colors
There are 6 colors in the cube. They will be encoded as follows:

- `0` represent the color red
- `1` represent the color blue
- `2` represent the color green
- `3` represent the color yellow
- `4` represent the color orange
- `5` represent the color white

### Faces
A Rubik's Cube has 6 sides. Imagine you are looking directly at one of the faces ('Front'). There are 2 faces on the left and right ('Left', 'Right'), 2 faces directly above and below ('Up', 'Down'), and 1 face behind ('Back')

Each face of the Cube will be represented as a 3x3 array:

- `0` or 'F' represents the 'front' face or the face you are looking at
- `1` or 'L' represents the 'left' face
- `2` or 'R' represents the 'right' face
- `3` or 'U' represents the 'up' face
- `4` or 'D' represents the 'down' face
- `5` or 'B' represents the 'back' face

The whole cube can be represented as a 6x3x3 array:

cube = [front, left, right, up, down, back]

### Moves:

#### Rotating Faces
Each face of the cube can be rotated in one of three ways:
- `0` represents rotating the face clockwise
- `1` represents rotating the face anti-clockwise
- `2` represents rotating the face 180 degrees (or 2 clockwise/anti-clockwise rotations in a row)

With 6 total faces, with 3 moves per face, there are a total of 18 moves. 'F0' would be rotating the front face clockwise. 'L1' would be to rotate the left face anti-clockwise as if you are facing the cube.