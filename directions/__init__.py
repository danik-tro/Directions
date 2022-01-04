def direction(facing: str, turn: int) -> str:
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    if facing not in directions:
        raise ValueError(f"Not allowed facing({facing})! Choose from {directions}!")

    if not isinstance(turn, int) or turn % 45 != 0 or not (-1080 <= turn <= 1080):
        raise ValueError(
            f"Invalid turn({turn}). Turn must be integer and a multiple of 45, between -1080 and 1080."
        )

    return directions[(directions.index(facing) + turn // 45) % 8]


__all__ = ["direction"]
