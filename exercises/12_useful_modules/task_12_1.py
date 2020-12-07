# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
import ipaddress





def ping_ip_addresses (ip_list):
   broken_ip = []
   true_ip = []
   for i in ip_list:
       ping = subprocess.run(['ping', '-c', '1', '-n', f'{i}'])
       if ping.returncode == 0:
           true_ip.append(i)
       else:
           broken_ip.append(i)
   result = (true_ip, broken_ip)
   print(result)
   return result








#list_of_ips = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
#convert_ranges_to_ip_list(list_of_ips)
