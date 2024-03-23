# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Data Saver
# GNU Radio version: 3.10.7.0

from gnuradio import gr
from io import BytesIO
import pmt
    
class fengyun2_data_saver(gr.sync_block):
    """
    FengYun-2 S-VISSR2.0 Data Saver
    """
    def __init__(self,path='/home/user/bin.bin',log_state=True):
        gr.basic_block.__init__(
            self,
            name='FengYun-2 S-VISSR2.0 Data Saver',
            in_sig=[],
            out_sig=[]
            )
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg1)
        self.path=path
        print(f"Save to: {self.path}")
        self.log_state=log_state
        self.n=0
        self.out_file=open(self.path,'wb')

    def handle_msg1(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_o = pmt.u8vector_elements(msg)
        self.out_file.write(bytes(msg_o))
        self.n+=1
        if(self.log_state):
            print(f"Frame: {self.n}\r")