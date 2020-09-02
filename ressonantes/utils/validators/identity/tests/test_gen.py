from django.test import TestCase
from utils.validators.identity import gen, cnpj, cpf


class CPFGeneratorTests(TestCase):

    def setUp(self):
        """Set a masked valid CPF number"""
        self.cpf_mask_valid = gen.cpf_with_punctuation()

    def test_cpf_masked_valid_true(self):
        """Test that CPF masked valid is true"""
        self.assertTrue(cpf.validate(self.cpf_mask_valid))

    def test_cpf_no_masked_valid_true(self):
        """Test that CPF without masked is valid"""
        cpf_result = (self.cpf_mask_valid.replace(
            ".", "")).replace("-", "")
        self.assertTrue(cpf.validate(cpf_result))


class CNPJGeneratorTests(TestCase):

    def setUp(self):
        """Set a masked valid CNPJ number"""
        self.cnpj_masked_valid = gen.cnpj_with_punctuation()

    def test_cnpj_masked_valid_true(self):
        """Test that CNPJ masked valid is true"""
        self.assertTrue(cnpj.validate(self.cnpj_masked_valid))

    def test_cnpj_no_masked_valid_true(self):
        """Test that CNPJ without masked is valid"""
        cnpj_result = (self.cnpj_masked_valid.replace(
            ".", "")).replace("-", "")
        self.assertTrue(cnpj.validate(cnpj_result))
