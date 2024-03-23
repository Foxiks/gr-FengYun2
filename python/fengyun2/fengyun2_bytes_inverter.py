# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Bytes Inverter
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import pmt
    
class fengyun2_bytes_inverter(gr.sync_block):
    """
    FengYun-2 S-VISSR2.0 Bytes Inverter
    """
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='FengYun-2 S-VISSR2.0 Bytes Inverter',
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg1)

    def handle_msg1(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_o = pmt.u8vector_elements(msg)
        in_bytes_arr=bytearray(msg_o)
        out_bytes_arr=bytearray()
        for i in range(0,44356,2):
            out_bytes_arr.append(int(in_bytes_arr[i]))
            out_bytes_arr.append(int((~in_bytes_arr[i+1]) & 0x00ff))
        msg_out=list(out_bytes_arr)
        msg_out = pmt.init_u8vector(len(msg_out), msg_out)
        msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
        self.message_port_pub(pmt.intern('out'), msg_out)