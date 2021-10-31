from math import log10

def interestRate(income_src, credit_score, credit_amnt, credit_purp):
    interest = 10.0
    credit_purp_mdf = {
        "ипотека": -2.0,
        "развитие бизнеса": -0.5,
        "автокредит": 0.0,
        "потребительский": 1.5
    }
    credit_score_mdf = {
        "-1": 1.5,
        "0": 0.0,
        "1": -0.25,
        "2": -0.75
    }
    income_src_mdf = {
        "пассивный доход": 0.5,
        "наёмный работник": -0.25,
        "собственный бизнес": 0.25,
    }
    interest += (credit_purp_mdf[credit_purp] + credit_score_mdf[str(credit_score)] + income_src_mdf[income_src] + log10(credit_amnt))
    return interest*0.01

def creditPayment(credit_amnt, credit_term, interest):
    return (credit_amnt*(1+credit_term*interest)/credit_term)

def isCreditPaymentMoreThanIncomeHalf(income_val, credit_pay):
    return (2*credit_pay > income_val)

def isUnempoyed(income_src):
    return income_src == "безработный"

def isLowestCreditScore(credit_score):
    return credit_score == -2

def isCreditAmountMoreThanIncomeThird(income_val, credit_amnt, credit_term):
    return (3*credit_amnt > income_val*credit_term)

def isRetired(age, gender, credit_term):
    curr_year = 2021
    if gender == "M":
        if curr_year + credit_term in (2022, 2023) and age + credit_term >= 62:
            return True
        elif curr_year + credit_term in (2024, 2025) and age + credit_term >= 63:
            return True
        elif curr_year + credit_term in (2026, 2027) and age + credit_term >= 64:
            return True
        elif curr_year + credit_term >= 2028 and age + credit_term >= 65:
            return True
        else:
            return False
    elif gender == "F":
        if curr_year + credit_term in (2022, 2023) and age + credit_term >= 57:
            return True
        elif curr_year + credit_term in (2024, 2025) and age + credit_term >= 58:
            return True
        elif curr_year + credit_term in (2026, 2027) and age + credit_term >= 59:
            return True
        elif curr_year + credit_term >= 2028 and age + credit_term >= 60:
            return True
        else:
            return False

def credit_decision(age, gender, income_src, income_val, credit_score, credit_amnt, credit_term, credit_purp):
    if isUnempoyed(income_src) or isLowestCreditScore(credit_score) or isRetired(age, gender, credit_term) or isCreditAmountMoreThanIncomeThird(income_val, credit_amnt, credit_term):
        return "Кредит не выдаётся"
    else:
        interest = interestRate(income_src, credit_score, credit_amnt, credit_purp)
        credit_pay = creditPayment(credit_amnt, credit_term, interest)
        if isCreditPaymentMoreThanIncomeHalf(income_val, credit_pay):
            return "Кредит не выдаётся"
        else:
            if ((income_src == "пассивный доход" or credit_score == -1) and credit_amnt > 1) or ((income_src == "наёмный работник" or credit_score == 0) and credit_amnt > 5):
                return "Кредит не выдаётся"
            else:
                return "Кредит выдаётся\nГодовой платёж по кредиту: " + str(round(credit_pay, 3))

#print(credit_decision(29, "M", "пассивный доход", 1, 0, 0.5, 5, "потребительский"))
#print(credit_decision(33, "F", "собственный бизнес", 2, -1, 7.2, 11, "потребительский"))

