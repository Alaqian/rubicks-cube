# Rubick's Cube Solver

### Rubik's Cube Encoding

## Colors
There are 6 colors in the cube. They will be encoded as follows:

- `0` represent the color red
- `1` represent the color blue
- `2` represent the color green
- `3` represent the color yellow
- `4` represent the color orange
- `5` represent the color white

## Faces
A Rubik's Cube has 6 sides. Imagine you are looking directly at one of the faces ('Front'). There are 2 faces on the left and right ('Left', 'Right'), 2 faces directly above and below ('Up', 'Down'), and 1 face behind ('Back')

Each face of the Cube will be represented as a 3x3 array:

- `0` represents the 'Front' face or the face you are looking at
- `1` represents the 'Left' face
- `2` represents the 'Right' face
- `3` represents the 'Up' face
- `4` represents the 'Down' face
- `5` represents the 'Back' face

The whole cube can be represented as a 6x3x3 array:

cube = [front, left, right, up, down, back]
