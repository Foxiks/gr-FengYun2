# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun2 S-VISSR2.0 Frames Collector
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import pmt
    
class fengyun2_frames_collector(gr.sync_block):
    """
    Frames add
    """
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='FengYun2 S-VISSR2.0 Frames Collector',
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern('in 0'))
        self.message_port_register_in(pmt.intern('in 1'))
        self.message_port_register_in(pmt.intern('in 2'))
        self.message_port_register_in(pmt.intern('in 3'))
        self.message_port_register_in(pmt.intern('in 4'))
        self.message_port_register_in(pmt.intern('in 5'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in 0'), self.handle_msg0)
        self.set_msg_handler(pmt.intern('in 1'), self.handle_msg1)
        self.set_msg_handler(pmt.intern('in 2'), self.handle_msg2)
        self.set_msg_handler(pmt.intern('in 3'), self.handle_msg3)
        self.set_msg_handler(pmt.intern('in 4'), self.handle_msg2)
        self.set_msg_handler(pmt.intern('in 5'), self.handle_msg3)
        self.hash_arr=[]

    def handle_msg0(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        if(hash(bytes(msg_out[:1024])) not in self.hash_arr):
            self.hash_arr.append(hash(bytes(msg_out[:1024])))
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass
    
    def handle_msg1(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        if(hash(bytes(msg_out[:1024])) not in self.hash_arr):
            self.hash_arr.append(hash(bytes(msg_out[:1024])))
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass
    
    def handle_msg2(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        if(hash(bytes(msg_out[:1024])) not in self.hash_arr):
            self.hash_arr.append(hash(bytes(msg_out[:1024])))
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass
    
    def handle_msg3(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        if(hash(bytes(msg_out[:1024])) not in self.hash_arr):
            self.hash_arr.append(hash(bytes(msg_out[:1024])))
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass
    
    def handle_msg4(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        if(hash(bytes(msg_out[:1024])) not in self.hash_arr):
            self.hash_arr.append(hash(bytes(msg_out[:1024])))
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass
    
    def handle_msg5(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        msg_out = pmt.u8vector_elements(msg)
        if(hash(bytes(msg_out[:1024])) not in self.hash_arr):
            self.hash_arr.append(hash(bytes(msg_out[:1024])))
            msg_out = pmt.init_u8vector(len(msg_out), msg_out)
            msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
            self.message_port_pub(pmt.intern('out'), msg_out)
        else:
            pass