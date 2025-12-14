"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


    def test_add_too_large_value_raises_exception(self):
        calc = Calculator()

        with pytest.raises(InvalidInputException):
            calc.add(1_000_001, 1)
        with pytest.raises(InvalidInputException):
            calc.add(1,1_000_001)


    def test_add_too_small_value_raises_exception(self):
        calc = Calculator()

        with pytest.raises(InvalidInputException):
            calc.add(-1_000_001, -1)

    def test_add_allows_max_boundary(self):
        calc = Calculator()
        result = calc.add(1_000_000, 0)
        assert result == 1_000_000


    def test_add_allows_min_boundary(self):
        calc = Calculator()
        result = calc.add(-1_000_000, 0)
        assert result == -1_000_000

    def test_add_rejects_both_sides_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1_000_001, -1_000_001)


    def test_add_strict_operation(self):
        calc = Calculator()
        assert calc.add(10, 1) == 11
        assert calc.add(1, 10) == 11

    def test_add_operation_is_addition(self):
        calc = Calculator()
        assert calc.add(10, 1) == 11


    def test_add_out_of_range_exception_message(self):
        calc = Calculator()

        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(1_000_001, 1)

        assert "outside the valid range" in str(excinfo.value)



class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_is_not_commutative(self):
        calc = Calculator()
        assert calc.subtract(10, 3) == 7
        assert calc.subtract(3, 10) == -7



    def test_subtract_too_large_value_raises_exception(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1_000_001, 0)
        with pytest.raises(InvalidInputException):
            calc.subtract(0, 1_000_001)

    def test_subtract_allows_max_boundary(self):
        calc = Calculator()
        assert calc.subtract(1_000_000, 0) == 1_000_000
        assert calc.subtract(-1_000_000, 0) == -1_000_000

    def test_subtract_rejects_both_sides_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1_000_001, -1_000_001)

    def test_subtract_strict_operation(self):
        calc = Calculator()
        assert calc.subtract(10, 1) == 9
        assert calc.subtract(1, 10) == -9


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_is_not_addition(self):
        calc = Calculator()
        assert calc.multiply(4, 3) == 12
        assert calc.multiply(3, 4) == 12

    
    def test_multiply_out_of_range_raises_exception(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(0, -1_000_001)
        with pytest.raises(InvalidInputException):
            calc.multiply(1_000_001, 0)

    def test_multiply_allows_boundary_values(self):
        calc = Calculator()
        assert calc.multiply(1_000_000, 1) == 1_000_000
        assert calc.multiply(-1_000_000, 1) == -1_000_000

    def test_multiply_rejects_both_sides_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1_000_001, -1_000_001)

    def test_multiply_strict_operation(self):
        calc = Calculator()
        assert calc.multiply(10, 1) == 10
        assert calc.multiply(1, 10) == 10


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 6
        b = 3
        expected = 2.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_order_matters(self):
        calc = Calculator()
        assert calc.divide(8, 2) == 4
        assert calc.divide(2, 8) == 0.25



    def test_divide_out_of_range_raises_exception(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1_000_001, 1)
        with pytest.raises(InvalidInputException):
            calc.divide(0, 1_000_001)

    def test_divide_allows_boundary_values(self):
        calc = Calculator()
        assert calc.divide(1_000_000, 1) == 1_000_000
        assert calc.divide(-1_000_000, 1) == -1_000_000

    def test_divide_rejects_both_sides_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1_000_001, -1_000_001)
    
    def test_divide_strict_operation(self):
        calc = Calculator()
        assert calc.divide(10, 1) == 10
        assert calc.divide(1, 10) == 0.1

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -6
        b = 3
        expected = -2.0
        # Act
        result = calc.divide(a, b)
        assert result == expected



