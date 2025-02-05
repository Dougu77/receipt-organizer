from utils import messages

messages.start()
years = messages.get_years()
full_years = messages.check_if_full_year()
if full_years:
    months = messages.get_full_years()
else:
    months = messages.get_months()
messages.set_folders(years, months)
messages.end()
