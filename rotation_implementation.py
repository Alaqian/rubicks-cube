def rotate_face(cube, face, rotation):
    face_mapping = [(1, 0, 2), (2, 0, 1), (3, 2, 0), (4, 0, 2), (5, 2, 0), (0, 0, 1)]
    rotation_mapping = [1, -1, 2]
    
    axis0, axis1, axis2 = face_mapping[face]
    rotate = rotation_mapping[rotation]
    
    if axis0 == axis1:
        cube[axis0, :, :] = np.rot90(cube[axis0, :, :], rotate, (0, 1))
    else:
        cube[[axis0, axis1], :, [0, 2]] = cube[[axis1, axis0], :, [2, 0]]
        cube[axis2, [0, 2], :] = np.flip(cube[axis2, [2, 0], :], axis=0)
        cube[axis2, 1, :] = np.rot90(cube[axis2, 1, :], rotate, (0, 1))
    
    return cube
