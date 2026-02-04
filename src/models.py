import calendar
from dataclasses import dataclass
from datetime import date, timedelta

import holidays
import pymorphy3
from num2words import num2words

from constants import MONTHS_RU

mf = pymorphy3.MorphAnalyzer()


@dataclass
class Requisites:

    unp: str
    address: str
    bank_account: str
    name_of_bank: str
    bic: str
    mobile_num: str
    e_mail: str


@dataclass
class Organization:
    id: int
    name: str
    manager_name: str
    agreement: str
    fee: float
    act_counter: int
    date: date
    requisites: Requisites
    last_issued_num: int = 0

    @property
    def month_year(self):
        # возвращает данные в формате "январь 2026"
        return f"{MONTHS_RU[self.date.month][0]} {self.date.year}"

    @property
    def day_month_year(self):
        # возвращает данные вформате " 30 января 2026"
        return f"{self.date.day} {MONTHS_RU[self.date.month][1]} {self.date.year}"

    @property
    def formated_fee(self):
        # integer
        return int(self.fee)

    @property
    def num_to_word(self) -> str:
        # преорбазовывает число в текст
        rubles = int(self.fee)
        kop = round((self.fee - rubles) * 100)
        str_num = num2words(rubles, lang="ru")
        num_to_check = str(rubles)
        result = None
        nums_for_rublia = set(["2", "3", "4"])
        nums_for_not_rublia = set(["12", "13", "14"])

        if num_to_check[-1] == "1" and num_to_check != "11":
            result = "белорусский рубль"
        elif (
            num_to_check[-1] in nums_for_rublia
            and num_to_check not in nums_for_not_rublia
        ):
            result = "белорусских рубля"
        else:
            result = "белорусских рублей"

        return f"({str_num}, {kop}0 копеек) {result}"  # Удалить 0, если будут Float

    @property
    def manager_name_gent(self) -> str:  # Функция склоняет ФИО в родительном падеже

        if not self.manager_name:
            return ""
        split_name = self.manager_name.split()
        res = []
        for word in split_name:
            parse = mf.parse(word)[0]
            if parse.word[-1] == "о":
                res.append(parse.word.capitalize())

            else:
                inflected = parse.inflect({"gent"})

                res.append(inflected.word.capitalize() if inflected else word)

        return " ".join(res)

    def prepare_next_period(self):
        # Функция увеличивает счетчик актов и записывает номер уже созданного акта, чтобы избежать повторов.
        if self.act_counter == self.last_issued_num:
            print("Акт уже был создан")
            return
        self.last_issued_num = self.act_counter
        self.date = self._incriment_date(self.date)
        self.act_counter += 1

    @staticmethod
    def _incriment_date(
        current_date: date,
    ) -> date:  # функция увеличивает год, и берет последний рабочий день месяца

        bel_holidays = holidays.country_holidays("BY")

        month = current_date.month
        year = current_date.year
        next_month = month + 1
        next_year = year
        if next_month > 12:
            next_month = 1
            next_year += 1

        last_day = calendar.monthrange(next_year, next_month)[1]
        new_date = date(next_year, next_month, last_day)
        while new_date.weekday() >= 5 or new_date in bel_holidays:
            new_date -= timedelta(days=1)

        return new_date
