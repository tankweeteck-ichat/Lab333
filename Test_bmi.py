import Lab002_2420.bmi as BMI

def test_calc_bmi_underweight():
    expected = -1
    result = BMI.calculate_bmi(weight=35.0, height=1.80)
    assert(result == expected)


def test_calc_bmi_normalweight():
    expected = 0
    result = BMI.calculate_bmi(weight=65.0, height=1.80)
    assert(result == expected)


def test_calc_bmi_overweight():
    expected = 1
    result = BMI.calculate_bmi(weight=95.0, height=1.80)
    assert(result == expected)

