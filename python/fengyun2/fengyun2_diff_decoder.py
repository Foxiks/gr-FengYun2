# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Differential Decoder
# GNU Radio version: 3.10.7.0

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr

class fengyun2_diff_decoder(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "FengYun-2 S-VISSR2.0 Differential Decoder",
                gr.io_signature(1, 1, gr.sizeof_char*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Blocks
        ##################################################

        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, 2)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 2, "", False, gr.GR_LSB_FIRST)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_repeat_0, 0))


