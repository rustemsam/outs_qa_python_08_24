import pytest

from src.circle import Circle


@pytest.fixture
def circle():
    def _circle(radius):
        return Circle(radius)

    return _circle


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize(
    "radius, expected_perimeter",
    [
        (5, 31.42),
        (5.5, 34.56),
    ],
)
def test_circle_perimeter(circle, radius, expected_perimeter):
    c = circle(radius)
    assert (
        round(c.perimeter, 2) == expected_perimeter
    ), f"Perimeter should be {expected_perimeter}"


@pytest.mark.positive
@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (5, 78.54),
        (5.5, 95.03),
    ],
)
def test_circle_area(circle, radius, expected_area):
    c = circle(radius)
    assert round(c.area, 2) == expected_area, f"Area should be {expected_area}"


@pytest.mark.negative
@pytest.mark.parametrize(
    "radius",
    [
        0,
        -1,
    ],
)
def test_circle_invalid_radius(circle, radius):
    with pytest.raises(ValueError, match="The radius of the circle must be positive."):
        circle(radius)
