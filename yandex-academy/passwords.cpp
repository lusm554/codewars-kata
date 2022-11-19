/*
Пароль от некоторого сервиса должен удовлетворять таким ограничениям:

состоять из символов таблицы ASCII с кодами от 33 до 126;
быть не короче 8 символов и не длиннее 14;
из 4 классов символов — большие буквы, маленькие буквы, цифры, прочие символы — в пароле должны присутствовать не менее трёх любых.
Напишите программу, которая проверит, что введённый пароль подходит под эти ограничения.

Формат ввода
На входе дана одна строка с паролем.

Формат вывода
Выведите YES, если пароль удовлетворяет требованиям, и NO в противном случае.
*/

#include <iostream>
#include <string>
#include <cctype>

int main() {
    int ucnt = 0, lcnt = 0, dcnt = 0, ocnt = 0;
    std::string pwd;

    if (std::cin >> pwd) {
        if (pwd.size() < 8 || pwd.size() > 14) {
            std::cout << "NO" << std::endl;
        } else {
            for (auto c : pwd) {
                if (c < 33 || c > 126) {
                    std::cout << "NO" << std::endl;
                    return 0;
                }
                if (std::isupper(c)) {
                    ucnt = 1;
                } else if (std::islower(c)) {
                    lcnt = 1;
                } else if (std::isdigit(c)) {
                    dcnt = 1;
                } else {
                    ocnt = 1;
                }
            }
            if ((ucnt + lcnt + dcnt + ocnt) < 3) {
                std::cout << "NO" << std::endl;
                return 0;
            }
            std::cout << "YES" << std::endl;
        }       
    }

    return 0;
}

