# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Soniks Messages Header Skip
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import pmt
    
class messages_skip_head(gr.sync_block):
    """
    Frames add
    """
    def __init__(self, skip):
        gr.basic_block.__init__(
            self,
            name='Soniks Messages Header Skip',
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg1)
        self.skip=skip

    def handle_msg1(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        msg_out = msg_out[self.skip:]
        msg_out = pmt.init_u8vector(len(msg_out), msg_out)
        msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
        self.message_port_pub(pmt.intern('out'), msg_out)