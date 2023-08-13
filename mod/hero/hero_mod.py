# -*- coding: utf-8 -*-
# @Time ： 2023/8/12 18:25
# @Auth ： JeremyChim
# @File ：hero_mod.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import os
from configparser import ConfigParser


def _main_(old_file, new_file, config):
    old_data = open(old_file)
    new_data = open(new_file,'w')

    lines = old_data.readlines()

    cf = ConfigParser()
    cf.read(config, encoding='utf-8')

    key_lst = cf.options('dec_point')

    for old_line in lines:
        new_line = _ret_newline_(key_lst, old_line, cf)

        if new_line:
            new_data.write(new_line)
            print(old_line, new_line)
        else:
            new_data.write(old_line)

    old_data.close()
    new_data.close()


def _ret_newline_(key_lst, old_line, cf):
    for keyword in key_lst:

        key_line = _find_key_(old_line, keyword)
        dec_point = cf.getint('dec_point', keyword)

        try:
            mul_arg = cf.get('mul_arg', keyword)
        except:
            mul_arg = 1

        try:
            add_arg = cf.get('add_arg', keyword)
        except:
            add_arg = 0

        if key_line:
            old_lst = key_line.replace('\t', '').replace('\n', '')
            old_lst = old_lst.split('"')

            old_arg = old_lst[3]

            new_arg = _calc_(dec_point, old_arg, mul_arg, add_arg)
            new_line = key_line.replace(old_arg, new_arg)

            return new_line


def _calc_(dec_point, old_arg, mul_arg, add_arg):
    if dec_point == 0:
        new_arg = _int_calc_(old_arg, mul_arg, add_arg)
        return new_arg

    else:
        new_arg = _float_calc_(old_arg, dec_point, mul_arg, add_arg)
        return new_arg


def _find_key_(line, keyword):
    line_low = line.lower()
    key_low = keyword.lower()

    if key_low in line_low:
        return line


def _float_calc_(old_arg, dec_point, mul_arg, add_arg):
    old_arg = float(old_arg)
    mul_arg = float(mul_arg)
    add_arg = float(add_arg)

    new_arg = old_arg * mul_arg + add_arg
    new_arg = f'%.{dec_point}f' % new_arg
    new_arg = str(new_arg)

    return new_arg


def _int_calc_(old_arg, mul_arg, add_arg):
    old_arg = float(old_arg)
    mul_arg = float(mul_arg)
    add_arg = float(add_arg)

    new_arg = old_arg * mul_arg + add_arg
    new_arg = int(new_arg)
    new_arg = str(new_arg)

    return new_arg


if __name__ == '__main__':
    _main_('hero_old.txt',
           'hero_new.txt',
           'hero_config.ini',
           )
