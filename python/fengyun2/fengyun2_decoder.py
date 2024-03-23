# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FengYun-2 S-VISSR2.0 Images Decoder
# GNU Radio version: 3.10.7.0

import time, os, cv2, gc, sys
from PIL import Image
from multiprocessing import Process
import numpy
from gnuradio import gr

class fengyun2_decoder(gr.sync_block):
    """FengYun-2 S-VISSR2.0 Images Decoder"""

    def __init__(self, path='/home/user/'):
        gr.sync_block.__init__(
            self,
            name='FengYun-2 S-VISSR2.0 Images Decoder',
            in_sig=[numpy.uint8],
            out_sig=None)
        self.frames_array=bytearray()
        self.path=path
        self.temp_array=bytearray()
        self.hash_tab=[]
    
    def get_size(self):
        size = len(self.frames_array)
        l = int(size)/int(44356)
        return l
    
    def ir_1_saver(self):
        print("Saving IR CH-1...")
        crop_img = self.grayImage[0:int(self.l), 2552:4846]
        cv2.imwrite(f'{self.path}IR-CH_1.png', crop_img)
        del crop_img
        gc.collect()
        return

    def ir_2_saver(self):
        print("Saving IR CH-2...")
        crop_img = self.grayImage[0:int(self.l), 5102:7396]
        cv2.imwrite(f'{self.path}IR-CH_2.png', crop_img)
        del crop_img
        gc.collect()
        return

    def ir_3_saver(self):
        print("Saving IR CH-3...")
        crop_img = self.grayImage[0:int(self.l), 7653:9947]
        cv2.imwrite(f'{self.path}IR-CH_3.png', crop_img)
        del crop_img
        gc.collect()
        return
    
    def vis_chunks_reader(self):
        print('Read VIS Chunks...')
        f1 = open('/tmp/chunks.vis', 'ab')
        f2 = open('/tmp/ir10.ch', 'ab')
        for i in range(0,len(self.frames_array),44356):
            frame = self.frames_array[i:i+44356]
            frame=''.join(format(x, '02x') for x in frame)
            f1.write(bytes.fromhex(frame[20408:34160]))
            f1.write(bytes.fromhex(frame[34673:48425]))
            f1.write(bytes.fromhex(frame[48938:62690]))
            f1.write(bytes.fromhex(frame[63203:76955]))
            f2.write(bytes.fromhex(frame[82466:88216]))
        f1.close()
        f2.close()
        return
    
    def vis_chunks_converter(self):
        with open('/tmp/chunks.vis', 'rb') as binary_file:
            data = binary_file.read()
            data = bytearray(data)

        with open('/tmp/chunks.visscaled', 'wb') as pixel_file:
            i = 0
            four_pixels = bytearray([0,0,0,0])
            for i in range(0, len(data), 3):
                four_bytes = data[i]*0x10000 + data[i+1]*0x100 + data[i+2]
                four_pixels[0] = ((four_bytes >> (18)) & 0x3f) << 2
                four_pixels[1] = ((four_bytes >> (12)) & 0x3f) << 2
                four_pixels[2] = ((four_bytes >> (6)) & 0x3f) << 2
                four_pixels[3] = ((four_bytes) & 0x3f) << 2
                pixel_file.write(four_pixels)
        return
    
    def ir10_saver(self):
        print("Saving IR CH-4 (10-bit)...")
        file5 = open('/tmp/ir10.ch', 'rb').read()
        b4=bin(int.from_bytes(file5, byteorder='big', signed=False))[2:].zfill(os.path.getsize('/tmp/ir10.ch')*8)
        chunks10 = [b4[i:i+10] for i in range(0, len(b4), 10)]
        del b4
        gc.collect()
        chunks10 = [str+'000000' for str in chunks10]
        len_c10=int((len(chunks10)*16)/8)
        with open('/tmp/ir10.bit', 'wb') as file:
            file.write(int(''.join(chunks10)[8:], 2).to_bytes(len_c10-1, byteorder='big',signed=False))
            file.write(b'\x00')
        del chunks10
        gc.collect()
        with open('/tmp/ir10.bit', mode='rb') as f:
            d = numpy.fromfile(f,dtype=numpy.uint16,count=2300*int(self.l)).reshape(int(self.l), int(2300))
        PILimage = Image.fromarray(d)
        PILimage.save(f'{self.path}IR-CH_4.png')
        return
    
    def vis_saver(self):
        with open('/tmp/chunks.visscaled', "rb") as image:
            f = image.read()
        bbyteArray = bytearray(f)
        grayImage = numpy.array(bbyteArray).reshape(int(self.l*4), int(9168))
        print("Saving VIS...")
        cv2.imwrite(f'{self.path}CH_VIS.png', grayImage)
        #src = cv2.imread('/tmp/CH_VIS.png', cv2.IMREAD_UNCHANGED)
        #cv2.imwrite(f'{self.path}CH_VIS.png', src)
        return
    
    def rmtmp(self):
        try:
            os.remove('/tmp/chunks.vis')
            os.remove('/tmp/chunks.visscaled')
            os.remove('/tmp/ir10.bit')
            os.remove('/tmp/ir10.ch')
            os.remove('/tmp/CH_VIS.png')
        except os.error:
            pass
        return

    def __del__(self):
        print("-----------------------------------")
        print("   FengYun-2 S-VISSR 2.0 decoder   ")
        print("           by Egor UB1QBJ          ")
        print("-----------------------------------")
        if(len(self.frames_array)==0):
            print("Done!")
            return
        self.l = self.get_size()
        self.grayImage = numpy.array(self.frames_array).reshape(int(self.l), int(44356))
        p1 = Process(target=self.ir_1_saver())
        p1.start()
        p2 = Process(target=self.ir_2_saver())
        p2.start()
        p3 = Process(target=self.ir_3_saver())
        p3.start()
        p4 = Process(target=self.vis_chunks_reader())
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        del self.grayImage
        gc.collect()
        print('Convert VIS Chunks to 8-bit pattern...')
        self.vis_chunks_converter()
        self.ir10_saver()
        ##
        self.vis_saver()
        print("Done!")
        self.rmtmp()
        return

    def work(self, input_items, output_items):
        msg=input_items[0][:]
        self.temp_array.extend(bytes(msg))
        if(len(self.temp_array)>44356):
            current_hash=hash(bytes(self.temp_array[:44356]))
            if current_hash not in self.hash_tab:
                self.frames_array.extend(self.temp_array[:44356])
                self.temp_array=self.temp_array[44356:]
                self.hash_tab.append(current_hash)
            else:
                self.temp_array=self.temp_array[44356:]
        if(len(self.temp_array)==44356):
            current_hash=hash(bytes(self.temp_array))
            if current_hash not in self.hash_tab:
                self.frames_array.extend(self.temp_array)
                self.temp_array.clear()
                self.hash_tab.append(current_hash)
            else:
                self.temp_array.clear()
        else:
            pass
        return len(input_items[0])