import pytest

from src.validators.org_validators import OrgValidator, ValidationError


def test_validate_name_org_positive():
    assert OrgValidator.validate_name_org("ООО Ромашка") is True


def test_validate_manager_name_positive():
    assert OrgValidator.validate_manager_name("Иванов Иван Иванович") is True


def test_validate_agreement_positive():
    assert OrgValidator.validate_agreement("ДОГ-123/24") is True


def test_validate_fee_positive():
    assert OrgValidator.validate_fee(1) is True
    assert OrgValidator.validate_fee("999999.99") is True


def test_validate_act_counter_positive():
    assert OrgValidator.validate_act_counter(1) is True
    assert OrgValidator.validate_act_counter(999) is True


def test_validate_date_positive():
    assert OrgValidator.validate_date("01.01.2024") is True


def test_validate_unp_positive():
    assert OrgValidator.validate_unp("123456789") is True


def test_validate_address_positive():
    assert OrgValidator.validate_address("г. Минск, ул. Ленина, 1") is True


def test_validate_bank_account_positive():
    assert OrgValidator.validate_bank_account("BY25MTBK12345678901234565897") is True


def test_validate_name_of_bank_positive():
    assert OrgValidator.validate_name_of_bank("Беларусбанк") is True


def test_validate_bic_positive():
    assert OrgValidator.validate_bic("MTBKBY22") is True


def test_validate_mobile_num_positive():
    assert OrgValidator.validate_mobile_num("375291234567") is True


def test_validate_email_positive():
    assert OrgValidator.validate_e_mail("test@mail.com") is True
