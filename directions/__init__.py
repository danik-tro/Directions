def direction(facing: str, turn: int) -> str:
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    return directions[(directions.index(facing) + turn // 45) % 8]


__all__ = ["direction"]
