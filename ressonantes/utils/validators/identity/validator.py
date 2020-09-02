from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from .cnpj import validate as is_cnpj_valid
from .cpf import validate as is_cpf_valid


@deconstructible
class IdentityValidator:

    def __call__(self, *args, **kwargs):

        if not is_cnpj_valid(args) or not is_cpf_valid(args):
            raise ValidationError(
                'O número do documento de identificação informado é inválido!'
            )
