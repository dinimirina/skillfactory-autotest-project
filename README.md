
# Финальный проект в  рамках курса SkillFactory: INTQAP

Проект автоматизированного тестирования на сервис
[Новый интерфейс авторизации ЛК Ростелеком](https://b2c.passport.rt.ru)


## Тестовая документация

[Тест-кейсы](https://docs.google.com/spreadsheets/d/1EvddgkaWi0hATz2wGO8gTkFOwaQOr9bE0LIiPiFko1E/edit#gid=457798835)

[Обнаруженные дефекты](https://docs.google.com/spreadsheets/d/1EvddgkaWi0hATz2wGO8gTkFOwaQOr9bE0LIiPiFko1E/edit#gid=1771879806)


## Инструменты

 - [Python 3.11.2](https://docs.python.org/3.11/)
 - [Pytest](https://docs.pytest.org/en/7.2.x/)
 - [Selenium](https://selenium-python.readthedocs.io/)
 - [Temporary Mail API](https://apilayer.com/marketplace/temp_mail-api#authentication)
 - [Geckodriver](https://github.com/mozilla/geckodriver)
 - [Page Object Model](https://selenium-python.readthedocs.io/page-objects.html)


## Список зависимостей



```bash
pytest==7.2.1
selenium==4.8.0
requests==2.28.2
```
    
## Запуск тестов

Клонировать проект

```bash
  git clone https://github.com/dinimirina/skillfactory-autotest-project.git
```

Перейти в директорию

```bash
  cd skillfactory-autotest-project
```

Установить зависимости

```bash
  pip install requirements.txt
```

Запуск тестов

```bash
  python -m pytest -v --tb=line  tests\
```


## Скриншот

![App Screenshot](https://i.postimg.cc/FzgZK3RS/image.png)

