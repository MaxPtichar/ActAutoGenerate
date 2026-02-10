import pytest

from src.validators.org_validators import OrgValidator, ValidationError


def test_validate_name_org_edges():
    assert OrgValidator.validate_name_org("АБ") is True
    assert OrgValidator.validate_name_org("А" * 300) is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_name_org("А")
    with pytest.raises(ValidationError):
        OrgValidator.validate_name_org("А" * 301)


def test_validate_manager_name_edges():
    assert OrgValidator.validate_manager_name("Ия") is True
    assert OrgValidator.validate_manager_name("И" * 300) is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_manager_name("И")
    with pytest.raises(ValidationError):
        OrgValidator.validate_manager_name("И" * 301)


def test_validate_agreement_edges():
    assert OrgValidator.validate_agreement("AA") is True
    assert OrgValidator.validate_agreement("A" * 140) is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_agreement("A")
    with pytest.raises(ValidationError):
        OrgValidator.validate_agreement("A" * 141)


def test_validate_fee_edges():
    with pytest.raises(ValidationError):
        OrgValidator.validate_fee(0)
    assert OrgValidator.validate_fee(0.01) is True
    assert OrgValidator.validate_fee(999_999.99) is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_fee(1_000_000)


def test_validate_act_counter_edges():
    with pytest.raises(ValidationError):
        OrgValidator.validate_act_counter(0)
    assert OrgValidator.validate_act_counter(1) is True
    assert OrgValidator.validate_act_counter(999) is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_act_counter(1_000)


def test_validate_unp_edges():
    with pytest.raises(ValidationError):
        OrgValidator.validate_unp("12345678")
    assert OrgValidator.validate_unp("123456789") is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_unp("1234567890")


def test_validate_mobile_num_edges():
    with pytest.raises(ValidationError):
        OrgValidator.validate_mobile_num("12345")
    assert OrgValidator.validate_mobile_num("123456") is True
    assert OrgValidator.validate_mobile_num("1" * 20) is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_mobile_num("1" * 21)


def test_validate_email_edges():
    assert OrgValidator.validate_e_mail("a@b.cd") is True
    with pytest.raises(ValidationError):
        OrgValidator.validate_e_mail("a" * 321 + "@mail.com")
