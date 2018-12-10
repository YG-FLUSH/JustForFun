#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Yoge on 2018-12-10
"""
# todatetime timestamp

from datetime import datetime
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='timstamp convert to datetime')

    parser.add_argument('-t', '--timestamp', metavar='1544418300', default="", required=True, help='Input the timestamp')

    args = parser.parse_args()
    timestamp = float(args.timestamp)
    datetime = datetime.fromtimestamp(timestamp)
    print datetime

