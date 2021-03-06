#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Использовать словарь, содержащий следующие ключи:
# название пункта назначения;номер поезда; время отправления.
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по времени отправления поезда;
# вывод на экран информации о поездах, направляющихся в пункт,
# название которого введено с клавиатуры;
# если таких поездов нет,выдать на дисплей соответствующее сообщение


import sys


if __name__ == '__main__':
    stations = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == 'add':
            punkt = input("Пункт назначения: ")
            nomer = input("Номер поезда: ")
            time = input("Время отправления: ")

            station = {
                'punkt':  punkt,
                'nomer': nomer,
                'time': time,
                }

            stations.append(station)

            if len(stations) > 1:
                stations.sort(key=lambda item: item.get('time', ''))

        elif command == 'select':
            punkt = input("Введите пункт прибытия для поиска: ")

            if not punkt:
                print("Вы ничего не ввели")

            else:
                for station in stations:
                    if station.get('punkt', '') == punkt:
                        print(
                            "Город прибытия: ", station.get('punkt', ''),
                            " Номер поезда: ", station.get('nomer', ''),
                            " Время отправления: ", station.get('time', '')
                            )
                        break
                    else:
                        print(f"Такого города нет: {punkt}", file=sys.stderr)

        elif command == "show":
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Город прибытия",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            for idx, station in enumerate(stations, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        station.get('punkt', ''),
                        station.get('nomer', ''),
                        station.get('time', '')
                    )
                )

            print(line)

        elif command == 'help':
            print("Список команд:\n")
            print("add - для добовления маршрутов")
            print("select - для поиска маршпута")
            print("show - для демонстрации всех машрутов")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
