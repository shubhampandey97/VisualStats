from logic.insights import generate_distribution_insight


def test_symmetric_normal():
    text = generate_distribution_insight(
        "Symmetric", True, 0, 0, 0
    )
    assert "symmetric" in text.lower()


def test_right_skew_non_normal():
    text = generate_distribution_insight(
        "Right Skewed", False, 5, 3, 1
    )
    assert "right-skewed" in text.lower()


def test_left_skew():
    text = generate_distribution_insight(
        "Left Skewed", False, 1, 3, 5
    )
    assert "left-skewed" in text.lower()
