import os
import time

yes_no_options = ['SIM', 'S', 'NÃO', 'NAO', 'N']
months_of_years = ['Janeiro', 'Fevereiro', 'Março',
                   'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro',
                   'Outubro', 'Novembro', 'Dezembro']

def validate_number(answer:str, is_month:bool):
    try:
        if is_month:
            if 0 < int(answer) <= 12:
                return True
            return False
        else:
            if int(answer) > 0:
                return True
            return False
    except:
        return False

def validate_years_or_months(answer:str, is_month:bool) -> bool:
    if answer.find('-') != -1:
        values = answer.split('-')
        for value in values:
            valid_value = validate_number(value, is_month)
            if not valid_value:
                return False
    else:
        valid_value = validate_number(answer, is_month)
        if not valid_value:
            return False
    return True
        
def validate_yes_no(answer:str) -> bool:
    if answer in yes_no_options:
        return True
    else:
        return False

def validate_answer(question:str, expected_return:str) -> str:
    valid_answer = False
    while True:
        answer = input(question).strip().upper()
        match expected_return:
            case 'years':
                valid_answer = validate_years_or_months(answer, False)
            case 'months':
                valid_answer = validate_years_or_months(answer, True)
            case 'yes_no':
                valid_answer = validate_yes_no(answer)
        if valid_answer:
            break
        else:
            print('Digite uma resposta válida.')

    return answer

def format_month(month:int) -> str:
    if len(str(month)) == 1:
        return f'0{month}'
    else:
        return str(month)

def get_years_or_months_range(years_or_months:list[str]) -> tuple[int, int]:
    if len(years_or_months) > 1:
        begin_value = int(years_or_months[0])
        end_value = int(years_or_months[1]) + 1
    else:
        begin_value = int(years_or_months[0])
        end_value = int(years_or_months[0]) + 1
    return begin_value, end_value

def create_folders(years:list[str], months:list[str]) -> None:
    years_range = get_years_or_months_range(years)
    months_range = get_years_or_months_range(months)
    for year in range(years_range[0], years_range[1]):
        for month in range(months_range[0], months_range[1]):
            os.makedirs(f'Anos/{year}/{format_month(month)} - {months_of_years[month - 1]}', exist_ok=True)
            print('.', end='', flush=True)
            time.sleep(0.2)
