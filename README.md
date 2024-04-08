# EnDeCoder

**EnDeCoder** - это скрипт на питоне, шифрующий переданный текст и имеющий обширный функционал.

## Требования
- Установленный Python 3.x версии.

## Установка и настройка
- Склонируйте репозиторий
```
git clone https://github.com/koloideal/EnDeCoder.git
```

## Особенности использования
- Для запуска скрипта перейдите в консоли в каталог, куда скопировали репозиторий, а после введите `python main.py` в windows и `python3 main.py` в linux
- Вам будет предложено выбрать один из четырёх вариантов:
  - `0. Get help on encryption methods`
    - Данный пункт даёт возможность получить информацию о различных методах шифровки и дешифровки.
    - Для получения справки про конкретную функцию введите её порядковый номер(на экране будут отображены все функции и их порядковые номера).
    - Функция бесконечно зациклена, для выхода из режима получения справки необходимо ввести `stop`.
  - `1. From the file`
    - При выборе данного пункта будет осуществлена шифровка или дешифровка с входными данными из определённого файла.
    - Перед запуском скрипта необходимо добавить файл, который вы хотите шифровать/расшифровывать в папку `content` в директории проекта.
    - Необходимо ввести название файла без расширения, после вам будет необходимо выбрать метод шифровки/дешифровки и уникальные для каждого метода настройки.
    - После окончания работы скрипта будет создан файл с именем исходного файла и постфиксом `(encoded)` или `(decoded)` в зависимости от выбранного режима работы.
    - `.txt` единственное расширение файла, при котором будет работать скрипт.
  - `2. Typing manually`
    - При выборе данного пункта будет осуществлена шифровка/дешифровка текста, введённого в консоль.
    - При выборе метода шифрования вам будет необходимо ввести соответствующие настройки(сдвиг, ключ-фраза и т.д.).
    - После окончания работы скрипта в консоль будет выведен результат работы.
  - `3. Select a saved configuration`
    - Данный пункт является режимом работы с конфигурациями.
    - В корне проекта находится файл `configs.json`, в котором находятся все сохранённые конфиги.
    - Изначально в файле записаны две дефолтные конфигурации, их нельзя удалять, скрипт может работать некорректно.
    - После выбора данного пункта у вас будет три возможных вариантов действий:
      - `"id конфига"`
        - Если вы хотите использовать сохранённый конфиг, то просто введите его id(будет отображаться на экране), а дальше следуйте указаниям.
      - `0`
        - При вводе `0` в консоль вы перейдёте в режим добавления конфигураций.
        - Вам будет необходимо выбрать имя конфигурации и все последующие настройки, которые будут сохранены в файле и будут доступны для быстрого использования.
        - При корректном вводе всех настроек будут созданы два конфига: первый, тот, который вы создали, и второй, которой будет создан автоматически с постфиксом `(to_encode)` или `(to_decode)` он полностью повторяет созданный вами конфиг за исключением двух пунктов: `id` будет отличаться на одну единицу, и шифрование будет заменено на расшифровывание, или же наоборот, другими словами будет создан "зеркальный конфиг", для быстрого использования обратного способа шифрования/дешифрования с теми же настройками.
      - `-0`
        - При вводе `-0` в консоль вы перейдёте в режим удаления конфигураций.
        - Вам будет необходимо ввести имя конфигурации для удаления.
        - При наличии конфигурации с введённым именем и постфиксом  `(to_encode)` или `(to_decode)` он будет также удалён.
- Осуществлено логирование ошибок и начала/конца работы скрипта, все данные записываются в файл `traceback.txt`, который будет создан после первого запуска скрипта.
  
**Важно:** при ручном изменении файла конфигурации возможна нештатная работа.

**Очень важно:** скрипт работает ТОЛЬКО с английским языком, при наличии любого другого языка текст не будет корректно зашифрован/расшифрован.


**Ремарка:** Функционал данного скрипта не является исчерпывающим, поэтому всегда рад вашим предложениям и идеям.

