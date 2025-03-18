###### .env в репе для простоты

### развертывание локально

1. git clone https://github.com/tveri/tl_group.git
2. cd tl_group
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser --username admin --email admin@example.com --skip-checks
8. python generate_mock_data.py
9. python manage.py runserver


главная страница по маршруту: "/"

