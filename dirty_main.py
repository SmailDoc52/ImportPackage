from datetime import *

from application.db.people import get_employees
from application.salary import *
from application.db import *

if __name__ == '__main__':
    now = datetime.now()
    print(now.strftime("%d.%m.%Y"))
    calculate_salary()
    print(now.strftime("%d.%m.%Y"))
    get_employees()