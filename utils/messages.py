from utils import data_manipulation

def start() -> None:
    print(f'''{"-" * 37}
     Organizador de Comprovantes     
{"-" * 37}

- Esse programa cria pastas para cada mês e ano que o usuário quiser.
- Ele pode ser usado para organizar outras coisas por ano e mês, como fotos.
- No case de intervalos de meses ou anos, digite: inicial-final.
''')

def get_years() -> list[str]:
    years = data_manipulation.validate_answer('Qual(is) o(s) ano(s)? ', 'years')
    if years.find('-') != -1:
        return years.split('-')
    else:
        return [years]

def check_if_full_year() -> bool:
    print()
    yes_no = data_manipulation.validate_answer('O(s) ano(s) possui(em) todo(s) o(s) mes(es)? ', 'yes_no')
    if yes_no in ['SIM', 'S']:
        return True
    else:
        return False

def get_full_years() -> list[str]:
    return ['1', '12']

def get_months() -> list[str]:
    print()
    months = data_manipulation.validate_answer('Qual(is) o(s) mes(es)? ', 'months')
    if months.find('-') != -1:
        return months.split('-')
    else:
        return [months]

def set_folders(years:list[str], months:list[str]) -> None:
    print('\nCriando as pastas', end='')
    data_manipulation.create_folders(years, months)

def end() -> None:
    input('\n\nPressione ENTER para encerrar o programa...')
