# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date: 2018-08-18 03:05:40
# @Last Modified by: shubhambansal
# @Last Modified time: 2018-08-18 03:06:22

from eve import Eve
app = Eve(settings='settings/production.py')

if __name__ == '__main__':
  app.run()

