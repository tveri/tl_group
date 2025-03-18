### развертывание локально

1. git clone https://github.com/tveri/tl_group.git
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser --username admin --email admin@example.com --skip-checks
7. python generate_mock_data.py
8. python manage.py runserver


главная страница по маршруту: "/"

