from logic.report import generate_text_report


def test_report_generation():
    text = generate_text_report(
        dataset_name="test",
        mean=1,
        median=1,
        mode=1,
        variance=0,
        std_dev=0,
        skewness=0,
        insight="Sample insight",
    )

    assert "STATISTICS EXPLORER REPORT" in text
    assert "Sample insight" in text
