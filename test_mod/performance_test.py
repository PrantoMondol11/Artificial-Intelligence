from sys_module.performance import calculate_performance


def test_performance_calculation():
    score = calculate_performance(10, 20)

    assert score == (20 * 10) - 20

    print("Performance calculation test passed.")