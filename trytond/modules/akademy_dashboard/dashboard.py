# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool, PoolMeta


class Action(metaclass=PoolMeta):
    "Dashboard Action"
    __name__ = "dashboard.action"
    