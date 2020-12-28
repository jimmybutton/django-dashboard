# Django Dashboard

A simple Django app that demonstrates how to fetch data asynchronously from JavaScript and display it in a Chart.js chart.

It's based on the article https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html but uses the more up to date Javascript Fetch API to make the async request.

The data has been dumped using Django fixtures like so
```
python manage.py dumpdata cities.City --indent 2 -o cities/fixtures/cities.json
```
It should be possible to load it with `manage.py loaddata`. For more info see https://docs.djangoproject.com/en/3.1/howto/initial-data/.