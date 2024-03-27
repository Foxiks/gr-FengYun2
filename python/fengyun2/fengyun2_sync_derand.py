# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Deframer and Derandomizer
# GNU Radio version: 3.10.7.0

from gnuradio import digital
from gnuradio import gr
from gnuradio import pdu
import fengyun2
import satellites
import satellites.grtypes







class fengyun2_sync_derand(gr.hier_block2):
    def __init__(self, threshold=7):
        gr.hier_block2.__init__(
            self, "FengYun-2 S-VISSR2.0 Deframer and Derandomizer",
                gr.io_signature(1, 1, gr.sizeof_char*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.threshold = threshold

        ##################################################
        # Blocks
        ##################################################

        self.satellites_fixedlen_to_pdu_0_0_1 = satellites.fixedlen_to_pdu(satellites.grtypes.byte_t, 'syncword', (354848+(192+128)), True)
        self.satellites_fixedlen_to_pdu_0_0_0_1 = satellites.fixedlen_to_pdu(satellites.grtypes.byte_t, 'syncword', (354848+(192+64)), True)
        self.satellites_fixedlen_to_pdu_0_0_0_0 = satellites.fixedlen_to_pdu(satellites.grtypes.byte_t, 'syncword', (354848+(64)), True)
        self.satellites_fixedlen_to_pdu_0_0_0 = satellites.fixedlen_to_pdu(satellites.grtypes.byte_t, 'syncword', (354848+(128)), True)
        self.satellites_fixedlen_to_pdu_0_0 = satellites.fixedlen_to_pdu(satellites.grtypes.byte_t, 'syncword', (354848+(192)), True)
        self.satellites_fixedlen_to_pdu_0 = satellites.fixedlen_to_pdu(satellites.grtypes.byte_t, 'syncword', 354848, True)
        self.pdu_pdu_to_stream_x_0 = pdu.pdu_to_stream_b(pdu.EARLY_BURST_APPEND, 64)
        self.messages_skip_head_0_2 = fengyun2.messages_skip_head((8*5))
        self.messages_skip_head_0_1 = fengyun2.messages_skip_head((8*3))
        self.messages_skip_head_0_0_0 = fengyun2.messages_skip_head((8*4))
        self.messages_skip_head_0_0 = fengyun2.messages_skip_head((8*2))
        self.messages_skip_head_0 = fengyun2.messages_skip_head(8)
        self.fengyun2_relevance_check_0 = fengyun2.fengyun2_relevance_check()
        self.fengyun2_frames_collector_0 = fengyun2.fengyun2_frames_collector()
        self.fengyun2_descrambler_0_3_1 = fengyun2.fengyun2_descrambler()
        self.fengyun2_descrambler_0_3_0 = fengyun2.fengyun2_descrambler()
        self.fengyun2_descrambler_0_3 = fengyun2.fengyun2_descrambler()
        self.fengyun2_descrambler_0_1 = fengyun2.fengyun2_descrambler()
        self.fengyun2_descrambler_0_0 = fengyun2.fengyun2_descrambler()
        self.fengyun2_descrambler_0 = fengyun2.fengyun2_descrambler()
        self.fengyun2_bytes_inverter_0_2 = fengyun2.fengyun2_bytes_inverter()
        self.fengyun2_bytes_inverter_0_1 = fengyun2.fengyun2_bytes_inverter()
        self.fengyun2_bytes_inverter_0_0_1 = fengyun2.fengyun2_bytes_inverter()
        self.fengyun2_bytes_inverter_0_0_0 = fengyun2.fengyun2_bytes_inverter()
        self.fengyun2_bytes_inverter_0_0 = fengyun2.fengyun2_bytes_inverter()
        self.fengyun2_bytes_inverter_0 = fengyun2.fengyun2_bytes_inverter()
        self.digital_correlate_access_code_tag_xx_0_0_1 = digital.correlate_access_code_tag_bb('1110010110010100010111010111100111001111000101001010001001111011', threshold, 'syncword')
        self.digital_correlate_access_code_tag_xx_0_0_0_1 = digital.correlate_access_code_tag_bb('1100110100011000101011100101001111100101111010000101110001110001', threshold, 'syncword')
        self.digital_correlate_access_code_tag_xx_0_0_0_0 = digital.correlate_access_code_tag_bb('1001001001101101011011010110111101101111011000110110001101001011', threshold, 'syncword')
        self.digital_correlate_access_code_tag_xx_0_0_0 = digital.correlate_access_code_tag_bb('1011011011111101101101100000110110110100001011011011100011101101', threshold, 'syncword')
        self.digital_correlate_access_code_tag_xx_0_0 = digital.correlate_access_code_tag_bb('1100100100100100101101101101101110110110110110011011011011010101', threshold, 'syncword')
        self.digital_correlate_access_code_tag_xx_0 = digital.correlate_access_code_tag_bb('0100101110111011101110011001100110010101010101010111111111111111', threshold, 'syncword')


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.fengyun2_bytes_inverter_0, 'out'), (self.fengyun2_frames_collector_0, 'in 5'))
        self.msg_connect((self.fengyun2_bytes_inverter_0_0, 'out'), (self.fengyun2_frames_collector_0, 'in 4'))
        self.msg_connect((self.fengyun2_bytes_inverter_0_0_0, 'out'), (self.fengyun2_frames_collector_0, 'in 2'))
        self.msg_connect((self.fengyun2_bytes_inverter_0_0_1, 'out'), (self.fengyun2_frames_collector_0, 'in 0'))
        self.msg_connect((self.fengyun2_bytes_inverter_0_1, 'out'), (self.fengyun2_frames_collector_0, 'in 3'))
        self.msg_connect((self.fengyun2_bytes_inverter_0_2, 'out'), (self.fengyun2_frames_collector_0, 'in 1'))
        self.msg_connect((self.fengyun2_descrambler_0, 'out'), (self.fengyun2_bytes_inverter_0, 'in'))
        self.msg_connect((self.fengyun2_descrambler_0_0, 'out'), (self.fengyun2_bytes_inverter_0_1, 'in'))
        self.msg_connect((self.fengyun2_descrambler_0_1, 'out'), (self.fengyun2_bytes_inverter_0_2, 'in'))
        self.msg_connect((self.fengyun2_descrambler_0_3, 'out'), (self.fengyun2_bytes_inverter_0_0, 'in'))
        self.msg_connect((self.fengyun2_descrambler_0_3_0, 'out'), (self.fengyun2_bytes_inverter_0_0_0, 'in'))
        self.msg_connect((self.fengyun2_descrambler_0_3_1, 'out'), (self.fengyun2_bytes_inverter_0_0_1, 'in'))
        self.msg_connect((self.fengyun2_frames_collector_0, 'out'), (self.fengyun2_relevance_check_0, 'in'))
        self.msg_connect((self.fengyun2_relevance_check_0, 'out'), (self.pdu_pdu_to_stream_x_0, 'pdus'))
        self.msg_connect((self.messages_skip_head_0, 'out'), (self.fengyun2_descrambler_0, 'in'))
        self.msg_connect((self.messages_skip_head_0_0, 'out'), (self.fengyun2_descrambler_0_3, 'in'))
        self.msg_connect((self.messages_skip_head_0_0_0, 'out'), (self.fengyun2_descrambler_0_3_0, 'in'))
        self.msg_connect((self.messages_skip_head_0_1, 'out'), (self.fengyun2_descrambler_0_0, 'in'))
        self.msg_connect((self.messages_skip_head_0_2, 'out'), (self.fengyun2_descrambler_0_1, 'in'))
        self.msg_connect((self.satellites_fixedlen_to_pdu_0, 'pdus'), (self.fengyun2_descrambler_0_3_1, 'in'))
        self.msg_connect((self.satellites_fixedlen_to_pdu_0_0, 'pdus'), (self.messages_skip_head_0_1, 'in'))
        self.msg_connect((self.satellites_fixedlen_to_pdu_0_0_0, 'pdus'), (self.messages_skip_head_0_0, 'in'))
        self.msg_connect((self.satellites_fixedlen_to_pdu_0_0_0_0, 'pdus'), (self.messages_skip_head_0, 'in'))
        self.msg_connect((self.satellites_fixedlen_to_pdu_0_0_0_1, 'pdus'), (self.messages_skip_head_0_0_0, 'in'))
        self.msg_connect((self.satellites_fixedlen_to_pdu_0_0_1, 'pdus'), (self.messages_skip_head_0_2, 'in'))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.satellites_fixedlen_to_pdu_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0, 0), (self.satellites_fixedlen_to_pdu_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_0, 0), (self.satellites_fixedlen_to_pdu_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_0_0, 0), (self.satellites_fixedlen_to_pdu_0_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_0_1, 0), (self.satellites_fixedlen_to_pdu_0_0_0_1, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_1, 0), (self.satellites_fixedlen_to_pdu_0_0_1, 0))
        self.connect((self, 0), (self.digital_correlate_access_code_tag_xx_0, 0))
        self.connect((self, 0), (self.digital_correlate_access_code_tag_xx_0_0, 0))
        self.connect((self, 0), (self.digital_correlate_access_code_tag_xx_0_0_0, 0))
        self.connect((self, 0), (self.digital_correlate_access_code_tag_xx_0_0_0_0, 0))
        self.connect((self, 0), (self.digital_correlate_access_code_tag_xx_0_0_0_1, 0))
        self.connect((self, 0), (self.digital_correlate_access_code_tag_xx_0_0_1, 0))
        self.connect((self.pdu_pdu_to_stream_x_0, 0), (self, 0))


    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.digital_correlate_access_code_tag_xx_0.set_threshold(self.threshold)
        self.digital_correlate_access_code_tag_xx_0_0.set_threshold(self.threshold)
        self.digital_correlate_access_code_tag_xx_0_0_0.set_threshold(self.threshold)
        self.digital_correlate_access_code_tag_xx_0_0_0_0.set_threshold(self.threshold)
        self.digital_correlate_access_code_tag_xx_0_0_0_1.set_threshold(self.threshold)
        self.digital_correlate_access_code_tag_xx_0_0_1.set_threshold(self.threshold)

