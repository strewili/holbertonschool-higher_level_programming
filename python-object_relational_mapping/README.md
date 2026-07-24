# 0x0F. Python - Object-relational mapping (ORM)

## Description

This project covers accessing a MySQL database from Python, first with
raw SQL queries via `MySQLdb`, then through Object-Relational Mapping
(ORM) using `SQLAlchemy`.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- `MySQLdb` (`mysql-connector-python` / `mysqlclient`)
- `SQLAlchemy` 1.2.x
- All scripts are executable and follow the pycodestyle (PEP8) style
- Every module, class, and function has a docstring

## Files

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all states from the database `hbtn_0e_0_usa` |
| `1-filter_states.py` | Lists all states with a name starting with `N` |
| `2-my_filter_states.py` | Lists states matching a name argument (SQL injection unsafe, for demonstration) |
| `3-my_safe_filter_states.py` | Lists states matching a name argument, safely (parameterized query) |
| `4-cities_by_state.py` | Lists all cities with their state |
| `5-filter_cities.py` | Lists all cities of a given state, safely |
| `model_state.py` | `State` class, mapped to the MySQL `states` table |
| `6-model_state.py` | Creates the `states` table via SQLAlchemy |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists all `State` objects containing letter `a` |
| `10-model_state_my_get.py` | Prints the id of a `State` object matching a name argument |
| `11-model_state_insert.py` | Adds the `State` object "Louisiana" to the database |
| `12-model_state_update_id_2.py` | Changes the name of the `State` object with `id = 2` |
| `13-model_state_delete_a.py` | Deletes all `State` objects containing letter `a` |
| `model_city.py` | `City` class, mapped to the MySQL `cities` table, linked to `State` |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects with their state |

## Usage

Most scripts take MySQL credentials and a database name as arguments:

```
./script.py <mysql_username> <mysql_password> <database_name> [extra_args]
```

Example:

```
$ ./0-select_states.py root root hbtn_0e_0_usa
```
