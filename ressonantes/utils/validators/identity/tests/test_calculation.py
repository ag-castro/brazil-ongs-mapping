from django.test import TestCase
from utils.validators.identity import calculation as calc


class CalculationTests(TestCase):

    def setUp(self):
        self.cpf_first_part = '111444777'
        self.cnpj_first_part = '114447770001'

    # CPF digits tests
    def test_cpf_first_digit_calculation_true(self):
        """Test CPF first digit calculation is true"""

        correct_first_digit = '3'
        self.assertEqual(correct_first_digit,
                         calc.calculate_first_digit(self.cpf_first_part))

    def test_cpf_first_digit_calculation_false(self):
        """Test CPF first digit calculation is false"""

        incorrect_first_digit = '6'
        self.assertNotEqual(incorrect_first_digit,
                            calc.calculate_first_digit(self.cpf_first_part))

    def test_cpf_second_digit_calculation_true(self):
        """Test CPF second digit calculation is true"""

        updated_cpf_number = self.cpf_first_part + \
            calc.calculate_first_digit(
                self.cpf_first_part)
        correct_second_digit = '5'
        self.assertEqual(correct_second_digit,
                         calc.calculate_second_digit(updated_cpf_number))

    def test_cpf_second_digit_calculation_false(self):
        """Test CPF second digit calculation is false"""

        updated_cpf_number = self.cpf_first_part + \
            calc.calculate_first_digit(
                self.cpf_first_part)
        incorrect_second_digit = '7'
        self.assertNotEqual(incorrect_second_digit,
                            calc.calculate_second_digit(updated_cpf_number))

    # CNPJ digits tests
    def test_cnpj_first_digit_calculation_true(self):
        """Test CNPJ first digit calculation is true"""

        correct_first_digit = '6'
        self.assertEqual(correct_first_digit,
                         calc.calculate_first_digit(self.cnpj_first_part))

    def test_cnpj_first_digit_calculation_false(self):
        """Test CNPJ first digit calculation is false"""

        correct_first_digit = '7'
        self.assertNotEqual(correct_first_digit,
                            calc.calculate_first_digit(self.cnpj_first_part))

    def test_cnpj_second_digit_calculation_true(self):
        """Test CNPJ second digit calculation is true"""

        correct_second_digit = '1'
        updated_cnpj_number = self.cnpj_first_part + \
            calc.calculate_first_digit(
                self.cnpj_first_part)
        self.assertEqual(correct_second_digit,
                         calc.calculate_second_digit(updated_cnpj_number))

    def test_cnpj_second_digit_calculation_false(self):
        """Test CNPJ second digit calculation is false"""

        correct_second_digit = '2'
        updated_cnpj_number = self.cnpj_first_part + \
            calc.calculate_first_digit(
                self.cnpj_first_part)
        self.assertNotEqual(correct_second_digit,
                            calc.calculate_second_digit(updated_cnpj_number))
