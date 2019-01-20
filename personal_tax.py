#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Author: Yoge
#   Time: 2019/01/20

tax_map = {
    0: 0.03,
    36000: 0.1,
    144000: 0.2,
    300000: 0.25,
    420000: 0.3,
    660000: 0.35,
    960000: 0.45
}
old_tax_map = {
    0: 0.03,
    3000: 0.1,
    12000: 0.2,
    25000: 0.25,
    35000: 0.3,
    55000: 0.35,
    80000: 0.45,
}

quick_deduct_map = {}
old_quick_deduct_map = {}

def load_quick_deduct_map(tax_map, quick_deduct_map):
    levels = sorted(tax_map.keys())
    for i, level in enumerate(levels):
        if i == 0:
            quick_deduct_map[level] = 0
        else:
            quick_deduct_map[level] = (tax_map[level]-tax_map[levels[i-1]])*level + quick_deduct_map[levels[i-1]]
    return quick_deduct_map


def find_tax_level(tax_map, sum_salary):
    if sum_salary < 0:
        raise Exception("salary could not be negative")
    levels = sorted(tax_map.keys())
    for i, level in enumerate(levels):
        if sum_salary < level:
            return levels[i-1]
    else:
        return levels[-1]

def cal_every_month_tax(salary, tax_map, quick_deduct_map):
    month = 12
    _map = {}
    for i in range(month):
        i += 1
        tax_level = find_tax_level(tax_map, salary*i)
        quick_deduct = quick_deduct_map[tax_level]
        tax_rate = tax_map[tax_level]

        if i == 1:
            sum_tax = 0
        else:
            sum_tax = sum(_map.values())
        _map[i] = (salary * i) * tax_rate - quick_deduct - sum_tax
    return _map

def cal_old_every_month_tax(salary, tax_map, quick_deduct_map):
    month = 12
    _map = {}
    for i in range(month):
        i += 1
        tax_level = find_tax_level(tax_map, salary)
        quick_deduct = quick_deduct_map[tax_level]
        tax_rate = tax_map[tax_level]
        _map[i] = (salary - quick_deduct) * tax_rate
    return _map


def main():
    salary = int(input("input you salary: "))
    deduct = int(input("input all your deduct: "))
    month = 12
    quick_deduct_map = {}
    old_quick_deduct_map = {}
    load_quick_deduct_map(tax_map, quick_deduct_map)
    load_quick_deduct_map(old_tax_map, old_quick_deduct_map)
    month_map = cal_every_month_tax(salary-deduct, tax_map, quick_deduct_map)
    old_month_map = cal_old_every_month_tax(salary-deduct, old_tax_map, old_quick_deduct_map)
    print 'tax of each month:', month_map
    print 'year salary:', salary * month
    print 'sum tax: ', sum(month_map.values())
    print 'old_tax of each month:', old_month_map
    print 'sum old tax: ', sum(old_month_map.values())

if __name__ == "__main__":
    main()

