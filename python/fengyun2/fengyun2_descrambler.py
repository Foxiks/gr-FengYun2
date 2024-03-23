# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Descrambler
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import pmt
    
class fengyun2_descrambler(gr.sync_block):
    """
    FengYun-2 S-VISSR2.0 Descrambler
    """
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='FengYun-2 S-VISSR2.0 Descrambler',
            in_sig=[],
            out_sig=[])

        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.message_port_register_out(pmt.intern('out'))
        self.mask=self.PN_mask_generator(mask=0x01)
    
    def PN_mask_generator(self, mask):
        mask=bin(mask)[2:].zfill(15)
        out=[]
        for _ in range(354848):
            x2=mask[14:]
            x1=mask[13:14]
            xor1=int(x1)^int(x2)
            mask=str(xor1)+mask[:14]
            out.append(mask[14:])
        return bytearray(int(''.join(out), 2).to_bytes(44356,'big'))

    def handle_msg(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg = pmt.u8vector_elements(msg)
        if(len(msg)==44356):
            arr_in=bytearray(msg)
            out_arr=list(bytes(a ^ b for (a, b) in zip(arr_in, self.mask)))
            msg_out = pmt.init_u8vector(len(out_arr), out_arr)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
            return
        else:
            print("Input MSG Length > 44356 bytes!")
            return
