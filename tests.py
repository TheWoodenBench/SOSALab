import math
import unittest
import dodatak_A

class TestDodatakA(unittest.TestCase):
    
    #
    #   Division tests
    #
    def test_div_poz_poz(self):
        unit = dodatak_A.OperationsManager(3.0, 2.0)

        self.assertEqual(unit.perform_division(), 1.5)

    def test_div_poz_neg(self):
        unit = dodatak_A.OperationsManager(3.0, -2.0)

        self.assertEqual(unit.perform_division(), -1.5)

    def test_div_neg_poz(self):
        unit = dodatak_A.OperationsManager(-3.0, 2.0)

        self.assertEqual(unit.perform_division(), -1.5)

    def test_div_neg_neg(self):
        unit = dodatak_A.OperationsManager(-3.0, -2.0)

        self.assertEqual(unit.perform_division(), 1.5)

    def test_div_zero_poz(self):
        unit = dodatak_A.OperationsManager(0.0, 2.0)

        self.assertEqual(unit.perform_division(), 0.0)

    def test_div_zero_neg(self):
        unit = dodatak_A.OperationsManager(0.0, -2.0)

        self.assertEqual(unit.perform_division(), 0.0)
    
    def test_div_bignum(self):
        unit = dodatak_A.OperationsManager(1000000000000000000000000000000000000000000000000.0, -2.0)

        self.assertEqual(unit.perform_division(), -500000000000000000000000000000000000000000000000.0)



    def test_div_poz_zero(self):
        unit = dodatak_A.OperationsManager(2.0, 0.0)

        self.assertTrue(math.isnan(unit.perform_division()))

    def test_div_neg_zero(self):
        unit = dodatak_A.OperationsManager(-2.0, 0.0)

        self.assertTrue(math.isnan(unit.perform_division()))


    # 
    #   Root tests
    #
    def test_root_poz_poz(self):
        unit = dodatak_A.OperationsManager(3.0, 2.0)

        self.assertAlmostEqual(unit.perform_root(), math.sqrt(3.0))

    def test_root_poz_neg(self):
        unit = dodatak_A.OperationsManager(3.0, -2.0)

        self.assertAlmostEqual(unit.perform_root(), 1.0/math.sqrt(3.0))

    def test_root_neg_poz(self):
        unit = dodatak_A.OperationsManager(-3.0, 2.0)

        self.assertTrue(math.isnan(unit.perform_root()))

    def test_root_neg_neg(self):
        unit = dodatak_A.OperationsManager(-3.0, -2.0)

        self.assertTrue(math.isnan(unit.perform_root()))

    def test_root_zero_poz(self):
        unit = dodatak_A.OperationsManager(0.0, 2.0)

        self.assertEqual(unit.perform_root(), 0.0)

    def test_root_zero_neg(self):
        unit = dodatak_A.OperationsManager(0.0, -2.0)

        self.assertEqual(unit.perform_root(), 0.0)


    def test_root_poz_zero(self):
        unit = dodatak_A.OperationsManager(2.0, 0.0)

        self.assertTrue(math.isnan(unit.perform_root()))

    def test_root_neg_zero(self):
        unit = dodatak_A.OperationsManager(-2.0, 0.0)

        self.assertTrue(math.isnan(unit.perform_root()))


    

        


if __name__ == '__main__':
    unittest.main()