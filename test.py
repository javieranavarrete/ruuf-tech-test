from Panel_Calculator import calculate_panels
from Panel_Calculator import INVALID_PARAMETER, INVALID_NUMBER, INVALID_PARAMS_AMOUNT

class TestRuuf:
    def test_enteros(self):
        inputs = [
            [1,2,2,4],
            [1,2,3,5],
            [2,2,1,10],
            [3,2,6,5]
        ]
        results = [4,7,0,5]
        for idx, case in enumerate(inputs):
            assert calculate_panels(case) == results[idx]

    def test_reales(self):
        inputs = [
            [1,2.5,2,5],
            [1,2,3,5.5],
        ]
        results = [4,7]
        for idx, case in enumerate(inputs):
            assert calculate_panels(case) == results[idx]

    def test_invalidos(self):
        inputs = [
            [-1,-2,-2,-4],
            [2,3,0,9],
            ['dummy',2,3,4],
            [4,5,6]
        ]
        results = [INVALID_NUMBER, INVALID_NUMBER, INVALID_PARAMETER, INVALID_PARAMS_AMOUNT]
        for idx, case in enumerate(inputs):
            assert calculate_panels(case) == results[idx]