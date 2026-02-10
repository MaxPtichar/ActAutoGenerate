from datetime import datetime

from src.constants import ALLOWED_CHARS


class ValidationError(Exception):
    pass


class OrgValidator:

    @staticmethod
    def validate_name_org(name: str):
        if not all(ch in ALLOWED_CHARS for ch in name):
            raise ValidationError("Название содержит недопустимые символы")
        if not (2 <= len(name) <= 300):
            raise ValidationError("Длина строки должна быть от 2 до 300 символов")

        return True

    @staticmethod
    def validate_manager_name(manager_name: str):
        if not all(ch.isalpha() or ch in " -." for ch in manager_name):
            raise ValidationError("Имя содержит недопустимые символы")
        if not (2 <= len(manager_name) <= 300):
            raise ValidationError("Длина строки должна быть от 2 до 300 символов")

        return True

    @staticmethod
    def validate_agreement(agreement: str):
        if not all(ch in ALLOWED_CHARS for ch in agreement):
            raise ValidationError("Номер договора содержит недопустимые символы")
        if not (2 <= len(agreement) <= 140):
            raise ValidationError("Длина строки должна быть от 2 до 140 символов")

        return True

    @staticmethod
    def validate_fee(fee: str):
        try:
            value = float(fee)
        except ValueError:
            raise ValidationError("Введите целое число")
        if not (0 < value < 1_000_000):
            raise ValidationError("Число не может быть меньше 0 и больше 1 000 000")

        return True

    @staticmethod
    def validate_act_counter(act_counter: int):
        try:
            value = int(act_counter)
        except ValueError:
            raise ValidationError("Введите число")
        if not (0 < value < 1_000):
            raise ValidationError("Число не может быть меньше 0 и больше 1 000 ")

        return True

    @staticmethod
    def validate_date(date: str):  ## stop
        try:
            datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            raise ValidationError("Формат даты: ДД.ММ.ГГГГ")

        return True

    @staticmethod
    def validate_unp(unp: str):
        if not unp.isdigit():
            raise ValidationError("УНП содержит недопустимые символы")
        if len(unp) != 9:
            raise ValidationError("УНП должно содержать 9 цифр")

        return True

    @staticmethod
    def validate_address(address: str):
        if not all(ch in ALLOWED_CHARS for ch in address):
            raise ValidationError("Адрес содержит недопустимые символы")
        if not (2 <= len(address) <= 300):
            raise ValidationError("Длина строки должна быть от 2 до 300 символов")

        return True

    @staticmethod
    def validate_bank_account(bank_account: str):
        if not bank_account.isalnum():
            raise ValidationError("Адрес содержит недопустимые символы")
        if len(bank_account) != 28:
            raise ValidationError("Cчет должен быть в формате BY25MTBK + 20 цифр")

        return True

    @staticmethod
    def validate_name_of_bank(name_of_bank: str):
        if not all(ch.isalpha() or ch in ' -"' for ch in name_of_bank):
            raise ValidationError("Название содержит недопустимые символы")
        if not (2 <= len(name_of_bank) <= 50):
            raise ValidationError("Длина строки должна быть от 2 до 50 символов")

        return True

    @staticmethod
    def validate_bic(bic: str):
        if not bic.isalnum():
            raise ValidationError("Адрес содержит недопустимые символы")
        if len(bic) != 8:
            raise ValidationError("BIC должен иметь 8 символов")

        return True

    @staticmethod
    def validate_mobile_num(mobile_num: str):
        if not mobile_num.isdigit():
            raise ValidationError("УНП содержит недопустимые символы")
        if not (6 <= len(mobile_num) <= 20):
            raise ValidationError("Номер телефона от 6 до 20 символов")

        return True

    @staticmethod
    def validate_e_mail(e_mail: str):
        if "@" not in e_mail or "." not in e_mail:
            raise ValidationError("Неверный e-mail")
        if not (5 <= len(e_mail) <= 320):
            raise ValidationError("Номер телефона от 5 до 320 символов")

        return True
