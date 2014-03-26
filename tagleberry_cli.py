#!/usr/bin/env python

x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print 'Invalid Number'
