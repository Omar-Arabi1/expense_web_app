# expense_web_app
an expense tracker web app made in Django

## endpoints

> [!NOTE]
> *these endpoints should be accessed through the frontend not manually they are lited just for knowledge*

- `GET /`: lists all expenses
- `POST add_expense`: adds an expense and takes in a price and an expense
- `DELETE remove_expense/<expense_id>`: removes an expense by taking its id
- `PUT update_expense/<expense_id>`: updates an expense price or expense or both
- `GET calculate`: adds all the prices from all the expenses and returns how much money was lost
- `export`: turns the db tables into a csv file with the expenses and their prices and downloads them

## setting up
to use this application follow these steps:

> [!NOTE]
> *the commands shown are for linux and MacOS the steps are the same, but some of the commands will change on windows*

- clone the repo `git clone https://github.com/Omar-Arabi1/expense_web_app.git`
- install the depenedencies `pip install -r pyproject.toml`

> [!TIP]
> *this tool was made with **uv** so if you use uv write `uv sync` and that will install the dependencies*

- run the server `python3 manage.py runserver`
- enter the url

from here you will have the ability to interact with the frontend to do the requests

> [!NOTE]
> *you could access the admin panel through the normal admin/ url it has the username: **admin** and password: **testpassword**.*