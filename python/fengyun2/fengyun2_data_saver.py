# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Data Saver
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import numpy
    
class fengyun2_data_saver(gr.sync_block):
    """
    FengYun-2 S-VISSR2.0 Data Saver
    """
    def __init__(self, path='/home/user/bin.bin',log_state=True,corrector_state=False):
        gr.sync_block.__init__(
            self,
            name='FengYun-2 S-VISSR2.0 Data Saver',
            in_sig=[numpy.uint8],
            out_sig=None)
        self.frames_array=bytearray()
        self.temp_array=bytearray()
        self.path=path
        print(f"Save to: {self.path}")
        self.log_state=log_state
        self.n=0
        self.corrector_state=corrector_state
    
    def __del__(self):
        if(self.corrector_state):
            total=int(len(self.frames_array)/44356)
            n=0
            op=total/100
            last=total-int(op*11)
            first=int(op*3)
            t=first+2501
            syncword = "00000000000000"
            k=0
            ff=open(self.path,'wb')
            for i in range(0,len(self.frames_array),44356):
                n+=1
                x = self.frames_array[i:i+44356]
                if (n<first):
                    vcducounter="0000"
                    syncword="00000000000000"
                if (n>=first<=t):
                    k+=1
                    vcducounter=hex(int(k))[2:].zfill(4)
                    syncword = "00000033FFFF00"  
                if (n>t):
                    vcducounter ="0000"
                    syncword="000000CC000000"
                if (n>=last):
                    vcducounter="0000"
                    syncword="000000CC000000"
                block1=x[7:67]
                block2=x[69:]
                ff.write(int(syncword,16).to_bytes(7,'big'))
                ff.write(bytes(block1))
                ff.write(int(vcducounter,16).to_bytes(2,'big'))
                ff.write(bytes(block2))
            ff.close()
        else:
            with open(self.path,'wb') as ff:
                ff.write(bytes(self.frames_array))
            
    
    def work(self, input_items, output_items):
        msg=input_items[0][:]
        self.temp_array.extend(bytes(msg))
        if(len(self.temp_array)>44356):
            self.n+=1
            if(self.log_state):
                print(f"Frame: {self.n}\r")
            self.frames_array.extend(self.temp_array[:44356])
            self.temp_array=self.temp_array[44356:]
        elif(len(self.temp_array)==44356):
            self.n+=1
            if(self.log_state):
                print(f"Frame: {self.n}\r")
            self.frames_array.extend(self.temp_array)
            self.temp_array.clear()
        else:
            pass
        return len(input_items[0])