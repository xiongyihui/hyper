# -*- coding: utf-8 -*-
"""
hyper/http20/frame
~~~~~~~~~~~~~~~~~~

Defines framing logic for HTTP/2.0. Provides both classes to represent framed
data and logic for aiding the connection when it comes to reading from the
socket.
"""
class Frame(object):
    def __init__(self):
        self.stream_id = 0
        self.flags = 0

    def serialize(self):
        raise NotImplementedError()
