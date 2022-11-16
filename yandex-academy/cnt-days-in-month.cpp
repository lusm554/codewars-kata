/*
Напишите программу, выводящую количество дней в месяце по заданному номеру месяца и году.

Формат ввода
На вход программе подается два целых положительных числа: номер месяца (от 1 до 12) и четырёхзначный год.

Формат вывода
Необходимо вывести одно число — количество дней в заданном месяце.
*/

#include <iostream>

int main() {
	int month = 0, year = 0;
	int days = 0;
	if (std::cin >> month >> year) {
		if (month == 2) {
			if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) {
					days = 29;
			} else {
					days = 28;
			}
		} else {
			if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12) {
					days = 31;
			} else {
					days = 30;
			}
		}
		std::cout << days << std::endl;
	}

	return 0;
}

