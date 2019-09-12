Заголовок 1 уровня
==================

Заголовок 2 уровня
------------------

Заголовок 3 уровня
~~~~~~~~~~~~~~~~~~

Заголовок 4 уровня
""""""""""""""""""

**жирный текст**

*курсив текст*

``«как есть»``

#. Один
#. Два
#. Три

Или:
5. Пять
6. Шесть
#. Семь

* Один
* Два
* Три

* Первый уровень
    * Второй уровень
        * Третий уровень

#. Один
    * Маркер
#. Два
    #. Номер

:Первый: В прямоугольном треугольнике квадрат длины
         гипотенузы равен сумме квадратов длин катетов.

Второй
    В прямоугольном треугольнике квадрат длины
    гипотенузы равен сумме квадратов длин катетов.

Основной текст:

    Цитата неизвестного человека

    --Аноним

.. epigraph::

   *«Если бы двери восприятия были чисты, всё
   предстало бы человеку таким, как оно есть — бесконечным»*

   -- Уильям Блэйк

.. epigraph::

   *«Если бы двери восприятия были чисты, всё
   предстало бы человеку таким, как оно есть — бесконечным»*

   -- |nbsp| Уильям Блэйк

   .. |nbsp| unicode:: U+00A0

Числовая сноска [5]_.

.. [5] Сюда ведет числовая сноска.

Сноски с автоматической [#]_ нумерацией [#]_.

.. [#] Это первая сноска.
.. [#] Это вторая сноска.

Авто­символ сносок используйте вот так [*]_ и [*]_.

.. [*] Это первый символ.
.. [*] Это второй символ.

Ссылки на цитаты выглядят так [CIT2002]_.

.. [CIT2002] Это цитата
(как часто используемая в журналах).

.. Это комментарий
   Многострочный комментарий

Посмотрим на исходный код:
::

    Пример исходного кода


Посмотрим на исходный код: ::

    Пример исходного кода

Посмотрим на исходный код::

    Пример исходного кода

Язык |ReST| — очень гибкий язык разметки (подстановки).

.. |ReST| replace:: *reStructuredText*

Copyright |copy| 2015, |LibreRussia (TM)| |---| все права защищены.

.. |copy| unicode:: 0xA9 .. знак копирайта
.. |LibreRussia (TM)| unicode:: LibreRussia U+2122 .. символ торговой марки
.. |---| unicode:: U+02014 .. длинное тире

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

Текущая дата |date| и время |time|

.. include:: имя_файла

--------

________

1. Внешние ссылки выглядят так: ссылка_.

.. _ссылка: http://librerussia.blogspot.ru/

2. Если несколько слов, тогда так: `ссылка в несколько слов`_.

.. _`ссылка в несколько слов`: http://librerussia.blogspot.ru/

3. `Более компактная запись ссылок <http://librerussia.blogspot.ru/>`_

Внутренние ссылки делаются так_

.. _так:

Ссылка на раздел создается так `Таблицы`_ .
Достаточно в обратных кавычках написать название заголовка.


Вставка изображения между слов |кубик-рубика| осуществляться с помощью функции автозамены:

.. |кубик-рубика| image:: _static/favicon.ico


.. figure:: _static/favicon.png
       :scale: 300 %
       :align: center
       :alt: Альтернативный текст

       Подпись изображения

       Легенда изображения.

.. image:: picture.jpeg
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

.. table:: Заголовок таблицы (Внимание! Отступ таблицы относительно
           команды ..``table::`` обязателен)

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | Cells may span columns.          |
    +------------------------+------------+---------------------+
    | body row 3             | Cells may  | - Table cells       |
    +------------------------+ span rows. | - contain           |
    | body row 4             |            | - body elements.    |
    +------------------------+------------+---------------------+


.. table:: Простая таблица
    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======


.. table:: Простая таблица со сложной шапкой

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

.. csv-table:: CSV-таблица
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

.. list-table:: Таблица в виде списка
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. tip:: Блок **Совет**, команда: ``.. tip::``
.. warning::
.. note::
.. important::
.. hint::
.. error::
.. danger::
.. caution::
.. attention::

.. meta::
   :description: The reStructuredText plaintext markup language
   :keywords: plaintext, markup language

.. meta::
   :description lang=en: An amusing story
   :description lang=fr: Une histoire amusante

.. meta::
   :http-equiv=Content-Type: text/html; charset=ISO-8859-1