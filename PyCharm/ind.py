#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def external_str(string):
    def name_surname(n, s):
        new_str = string.replace("%N%", n)
        new_str = new_str.replace("%F%", s)
        return new_str
    return name_surname


if __name__ == "__main__":
    common_string = (
        "«Уважаемый %F% %N%! Вы делаете работу по замыканиям функций."
    )
    name, surname = input("Enter your name and surname: ").split()
    print(external_str(common_string)(name, surname))

