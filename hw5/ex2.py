'''Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии.
Не забудьте распечатать в конце результат.'''


def gen_dict_bonus(lst_names : str, lst_salaries : int, lst_bonuses : float)-> dict[str: float]:
    return {name: round(salary * (float(bonus.strip('%')) / 100),2) for name, salary, bonus in zip(lst_names, lst_salaries, lst_bonuses)}

names = ["Grace", "John", "Linda"]
salary = [6200, 5800, 7500]
bonus = ["9%", "3%", "12%"]

print(gen_dict_bonus(names, salary, bonus))