# final_project_qa

Это репозиторий для финального проекта [курса QA](https://stepik.org/lesson/201964/step/15?unit=176022). В нем содержатся все необходимые файлы для выполнения тестов.

## Описание проекта

В этом проекте реализованы автоматизированные UI-тесты для сайта http://selenium1py.pythonanywhere.com. Тесты проверяют основные функциональные возможности сайта, такие как:

- Добавление товара в корзину
- Отображение сообщения об успешном добавлении товара
- Соответствие названия и цены товара
- Регистрация юзера
- Клики по кнопкам

## Установка

Для запуска тестов на вашем компьютере, вам потребуется:

1. Установить Python версии 3.7 или выше.
2. Установить зависимости из файла requirements.txt:

   pip install -r requirements.txt

3. Убедиться, что у вас установлен Pytest и Selenium WebDriver.

## Запуск тестов

Для запуска всех тестов, выполните в терминале следующую команду:

- pytest

Для запуска тестов, которые подлежат review кода выполните:

- pytest -v --tb=line --language=en -m need_review

Вы также можете запустить отдельные тесты, используя фильтры Pytest:

- pytest -k test_guest_can_add_product_to_basket

## Отчеты

Результаты тестов отображаются в консоли при запуске тестов. Кроме того, вы можете генерировать отчеты о тестах в различных форматах, таких как HTML или XML, используя инструменты тестирования, такие как pytest-html или allure-pytest.

Для генерации HTML-отчета установите пакет pytest-html и запустите следующую команду:

pytest --html=report.html test_practice_form_page.py

Это создаст файл report.html в директории проекта, который можно открыть в веб-браузере для просмотра результатов тестов.

## Настройка

Основные настройки проекта находятся в файле pytest.ini. Здесь вы можете изменить директории для поиска тестов, уровень логирования и другие параметры.

## Внесение изменений

Если вы хотите внести изменения в проект, пожалуйста, создайте новую ветку и оформите pull request. Все изменения должны соответствовать стилю кода и пройти успешные тесты.

## Контакты

Если у вас возникли вопросы или предложения, вы можете связаться со мной по почте: [inactive0073@gmail.com]

Спасибо за интерес к моему проекту!
