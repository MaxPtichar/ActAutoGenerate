import pytest

from src.validators.org_validators import OrgValidator, ValidationError


def test_validate_name_org_negative():
    with pytest.raises(ValidationError):
        OrgValidator.validate_name_org("ООО Ромашка 🚀")


def test_validate_manager_name_negative():
    with pytest.raises(ValidationError):
        OrgValidator.validate_manager_name("Иванов123")


def test_validate_agreement_negative():
    with pytest.raises(ValidationError):
        OrgValidator.validate_agreement("ДОГ123'🚀?")


@pytest.mark.parametrize("fee", [-1, 0, 1_000_000, "abc"])
def test_validate_fee_negative(fee):
    with pytest.raises(ValidationError):
        OrgValidator.validate_fee(fee)


@pytest.mark.parametrize("counter", [0, -1, 1_000, "abc"])
def test_validate_act_counter_negative(counter):
    with pytest.raises(ValidationError):
        OrgValidator.validate_act_counter(counter)


@pytest.mark.parametrize("date", ["32.01.2024", "2024-01-01", "01/01/2024"])
def test_validate_date_negative(date):
    with pytest.raises(ValidationError):
        OrgValidator.validate_date(date)


@pytest.mark.parametrize("unp", ["12345", "12345678a", ""])
def test_validate_unp_negative(unp):
    with pytest.raises(ValidationError):
        OrgValidator.validate_unp(unp)


@pytest.mark.parametrize("address", ["@", "", " "])
def test_validate_address_negative(address):
    with pytest.raises(ValidationError):
        OrgValidator.validate_address(address)


@pytest.mark.parametrize("account", ["BY25MTBK123", "BY25MTBK!234567890123456"])
def test_validate_bank_account_negative(account):
    with pytest.raises(ValidationError):
        OrgValidator.validate_bank_account(account)


@pytest.mark.parametrize("bank", ["B@@@", ""])
def test_validate_name_of_bank_negative(bank):
    with pytest.raises(ValidationError):
        OrgValidator.validate_name_of_bank(bank)


@pytest.mark.parametrize("bic", ["123", "MTBKBY2!", ""])
def test_validate_bic_negative(bic):
    with pytest.raises(ValidationError):
        OrgValidator.validate_bic(bic)


@pytest.mark.parametrize("mobile", ["+375291234567", "abc", "123"])
def test_validate_mobile_num_negative(mobile):
    with pytest.raises(ValidationError):
        OrgValidator.validate_mobile_num(mobile)


@pytest.mark.parametrize("email", ["testmail.com", "test@", ""])
def test_validate_email_negative(email):
    with pytest.raises(ValidationError):
        OrgValidator.validate_e_mail(email)
