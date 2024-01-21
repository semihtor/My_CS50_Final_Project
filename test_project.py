import pytest
from program import generate_secret_code
from program import evaluate_guess
from program import display_board


def main():
    test_generate_secret_code()
    test_evaluate_guess()
    test_display_board()


def test_generate_secret_code():
    # since i check that the difficulty is always [2, 5] and duplicates is always boolean in the while loop, the only test i can do is length of the generated code
    # (which will always be equal to the difficulty)
    assert len(generate_secret_code(2, False)) == 2
    assert len(generate_secret_code(3, False)) == 3
    assert len(generate_secret_code(4, False)) == 4
    assert len(generate_secret_code(5, False)) == 5
    assert len(generate_secret_code(2, True)) == 2
    assert len(generate_secret_code(3, True)) == 3
    assert len(generate_secret_code(4, True)) == 4
    assert len(generate_secret_code(5, True)) == 5

def test_evaluate_guess():
    # since i check that the answer is always entered according to difficulty, i can't test that answer is different length compared to code
    assert evaluate_guess("12", "12") == (2, 0)
    assert evaluate_guess("123", "123") == (3, 0)
    assert evaluate_guess("1234", "1234") == (4, 0)
    assert evaluate_guess("12345", "12345") == (5, 0)
    assert evaluate_guess("12", "21") == (0, 2)
    assert evaluate_guess("123", "231") == (0, 3)
    assert evaluate_guess("1234", "4123") == (0, 4)
    assert evaluate_guess("12345", "51234") == (0, 5)
    assert evaluate_guess("123", "132") == (1, 2)
    assert evaluate_guess("1234", "1243") == (2, 2)
    assert evaluate_guess("12345", "12954") == (2, 2)

def test_display_board():
    # since this function creates a table to be printed by tabulate in the main function, i test it for errors
    with pytest.raises(TypeError):
        display_board(132, 123)
    with pytest.raises(IndexError):
        display_board("test")


if __name__ == "__main__":
    main()
