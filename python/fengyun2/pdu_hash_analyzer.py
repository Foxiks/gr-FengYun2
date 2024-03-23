# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PDU Hash Analyzer
# GNU Radio version: 3.10.7.0

import pmt
from gnuradio import gr

class pdu_hash_analyzer(gr.sync_block):
    """PDU Hash Analyzer"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='PDU Hash Analyzer',
            in_sig=[],
            out_sig=[])
        self.hash_tab=[]
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg1)

    def handle_msg1(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg = pmt.u8vector_elements(msg)
        current_hash=hash(bytes(msg))
        if current_hash not in self.hash_tab:
            msg_out = pmt.init_u8vector(len(msg), msg)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
            self.hash_tab.append(current_hash)
        else:
            pass