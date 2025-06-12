import math

def test_matrix_inverse():
    # Test 2x2 matrix
    A = [[1, 2], [3, 4]]
    expected = [[-2, 1], [1.5, -0.5]]
    result = matrix_inverse(A)
    assert all(math.isclose(result[i][j], expected[i][j]) for i in range(2) for j in range(2)), "2x2 test failed"

    # Test 3x3 matrix
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result = matrix_inverse(B)
    assert all(math.isclose(result[i][j], expected[i][j]) for i in range(3) for j in range(3)), "3x3 identity test failed"

    # Test singular matrix (should raise error)
    try:
        C = [[1, 1], [1, 1]]
        matrix_inverse(C)
        assert False, "Singular matrix test failed (no error raised)"
    except ValueError:
        pass

    print("All tests passed!")

# Run tests
if __name__ == "__main__":
    test_matrix_inverse()