#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:mylogging.py
@time(UTC+8):16/8/21-16:35
'''

import logging

# GET A LOGGER
my_logger = logging.getLogger("TEST-LOG")

# create 2 handler stream logger and file handler
sh = logging.StreamHandler()
fh = logging.FileHandler("example_logging.log")
sh.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
stream_formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(name)s-%(message)s")
file_formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(name)s-%(message)s")

# realated
sh.setFormatter(stream_formatter)
fh.setFormatter(file_formatter)
my_logger.addHandler(sh)
my_logger.addHandler(fh)


# TEST my_logger
my_logger.info("info")
my_logger.debug("debug")
my_logger.warning("warnning")
my_logger.error("error")
my_logger.critical("critical")
