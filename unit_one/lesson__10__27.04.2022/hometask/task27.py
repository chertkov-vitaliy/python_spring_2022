#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
написать Save Game по следующему сценарию:
В запущенной игре по нажатию клавиши S появляется вывод:
1. Продолжить
2. Сохранить игру

При выборе пункта 1. игра продолжается.
При выборе пункта 2. пользователю предлагается ввести название для
сохранения, после чего нужно сделать сериализацию состояния игры.
Законсервировать все объекты которые отвечают за состоянии игры в файл
game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.

При старте игры пользователю должен предлагатся выбор
1. Новая игра
2. Восстановить игру
При выборе 1. начинается новая игра.
При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.