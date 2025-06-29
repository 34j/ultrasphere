from __future__ import annotations

import ivy
from ivy import Array, NativeArray


def is_same_shape(*shapes: tuple[int, ...]) -> bool:
    """
    Check if the shapes are the same shape, ignoring 1s.

    Returns
    -------
    bool
        True if the shapes are the same shape, False otherwise.

    """
    try:
        ivy.broadcast_shapes(*shapes)
    except ValueError:
        return False
    return True


def check_same_shape(*shapes: tuple[int, ...] | Array | NativeArray) -> None:
    """
    Check if the shapes are the same shape, ignoring 1s.

    Raises
    ------
    ValueError
        If the shapes are not the same shape.

    """
    shapes_: list[tuple[int, ...]] = [
        tuple(shape.shape) if hasattr(shape, "shape") else shape for shape in shapes
    ]
    if not is_same_shape(*shapes_):
        raise ValueError(f"Shapes {shapes_} are not the same shape.")
