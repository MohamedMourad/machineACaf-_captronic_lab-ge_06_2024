import unittest
from machine_a_cafe import*


class TestRomainConverter(unittest.TestCase):

    def test_nominal_case(self):
        cases = [ 1, 2 , 8]
        for number_of_pieces_inserted in cases:
            with self.subTest(number_of_pieces_inserted):
                # GIVEN ( coffe machine )
                machine = coffe_machine()
                # WHEN (some pieces where inserted )
                machine.insert(number_of_pieces_inserted)

                amount_of_coffe_to_prepare = machine.amount_of_coffe_to_prepare()

                #THEN ( we expect to have one coffe )
                self.assertEqual(amount_of_coffe_to_prepare, 1)


# ETANT DONNER / QUAND / ALORS

if __name__ == '__main__':
    unittest.main()
