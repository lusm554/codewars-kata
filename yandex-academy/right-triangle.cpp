/*
Напишите программу, которая проверяет является ли треугольник прямоугольным.

Формат ввода
На стандартный поток ввода подаётся три целых положительных числа — стороны треугольника. Числа не превосходят 30000.

Формат вывода
Если полученный треугольник является прямоугольным, напечатайте YES. Если треугольник не является прямоугольным, напечатайте NO. Если с заданными сторонами невозможно построить треугольник, напечатайте UNDEFINED.
*/

#include <iostream>
#include <string>

int main() {
    int x, y, z;
    std::string result;

    if (std::cin >> x >> y >> z) { // is valid triangle
        if (x + y <= z || x + z <= y || y + z <= x) {
            result = "UNDEFINED";
        } else if ((x*x)+(y*y)==(z*z) || (x*x)+(z*z)==(y*y) || (y*y)+(z*z)==(x*x)) { // is right triangle
            result = "YES";
        } else {
            result = "NO";
        }
        std::cout << result << std::endl;
    }
    return 0;
}

