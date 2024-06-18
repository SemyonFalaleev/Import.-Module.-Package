from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import art
if __name__ == "__main__":
    print(datetime.datetime.now())
    get_employees('Semen', 'Falaleev')
    calculate_salary(12)
    print(art.art("random"))
