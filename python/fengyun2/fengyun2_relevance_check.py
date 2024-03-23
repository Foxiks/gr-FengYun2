# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Soniks FengYun-2 S-VISSR2.0 Frames Relevance Check
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import pmt
from hexhamming import hamming_distance_string
    
class fengyun2_relevance_check(gr.sync_block):
    """
    Frames add
    """
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='FengYun-2 S-VISSR2.0 Frames Relevance Check',
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg1)
        self.sync=str('0'*128)

    def handle_msg1(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        err=int(hamming_distance_string(hex(int.from_bytes(bytes(msg_out[2300:2364]),'big'))[2:].zfill(128), self.sync))
        if(err<=192):
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass