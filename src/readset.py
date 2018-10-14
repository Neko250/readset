#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def extract(file=None, path=None):
  """
  Extract all of the YouTube links within a Headset user-made list.

  :param file: headset json export file path
  :param path: json path to extract, you can use [JSON Columns](http://json-columns.com) to get it
  :return: `list` containing all of the links in the list
  """
  if not file or not path:
    print('error: file or json path not provided...')
    return None

  # todo: implement
  pass


if __name__ == '__main__':
  extract()
