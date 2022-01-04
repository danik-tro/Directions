from typing import Any

import pytest

from directions import direction


@pytest.mark.parametrize(
    "facing,turn,result",
    (
        ("N", 45, "NE"),
        ("N", -45, "NW"),
        ("SE", 720, "SE"),
        ("SE", -720, "SE"),
        ("SE", 765, "S"),
        ("SE", -765, "E"),
        ("E", 270, "N"),
        ("E", -270, "S"),
        ("E", 0, "E"),
        ("E", -0, "E"),
    ),
)
def test_direction_ok(facing: str, turn: int, result: str):
    assert direction(facing, turn) == result


@pytest.mark.parametrize(
    "facing,turn",
    (
        ("W", "sss"),
        ("W", 14636),
        ("W", -14636),
        ("W", 1125),
        ("W", -1125),
    ),
)
def test_direction_invalid_turn(facing: str, turn: Any):
    with pytest.raises(ValueError, match="Invalid turn"):
        direction(facing, turn)


@pytest.mark.parametrize(
    "facing,turn",
    (
        ("EE", 45),
        ("GGG", -45),
        (22, 45),
        (["W"], 45),
        ({"W"}, 45),
    ),
)
def test_direction_invalid_facing(facing: Any, turn: int):
    with pytest.raises(ValueError, match="Not allowed facing"):
        direction(facing, turn)
