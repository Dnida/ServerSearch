#!/usr/bin/env python3

from textwrap import dedent
from typing import (
    Iterable,
    Set,
)

from openpyxl import load_workbook

TXT_FN = 'serverlist.txt'
XL_FN = 'serverlist.xlsx'


def get_servers_xl(fn: str='serverlist.xlsx') -> Iterable[str]:
    """Get servers from excel file, defaulting to serverlist.xlsx"""
    wb = load_workbook(fn)['Sheet1']
    return [i[0] for i in wb.values]


def get_servers_txt(fn: str='serverlist.txt') -> Iterable[str]:
    """Get servers from txt file, defaulting to serverlist.txt"""
    with open(fn) as f:
        return [i.strip() for i in f.readlines()]


if __name__ == '__main__':
    txt_hosts: Set[str] = set(get_servers_txt())
    xl_hosts: Set[str] = set(get_servers_xl())
    print(dedent(f'''
    Servers only in TXT: {txt_hosts.difference(xl_hosts) or "None only in here"}
    Servers only in XL: {xl_hosts.difference(txt_hosts)}
    Servers in both: {xl_hosts.intersection(txt_hosts)}
    '''))
