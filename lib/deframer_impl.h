/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FENGYUN2_DEFRAMER_IMPL_H
#define INCLUDED_FENGYUN2_DEFRAMER_IMPL_H

#include <gnuradio/Fengyun2/deframer.h>

namespace gr {
namespace Fengyun2 {

class deframer_impl : public deframer
{
private:
    std::string d_syncword;
    uint64_t d_work_syncword;
    const int d_syncword_length;
    uint64_t d_sync_mask;
    const int d_frame_length;
    const int d_thresold;
    int send_size = 0;

    bool in_frame = false;
    std::vector<uint8_t> current_frame;
    std::vector<std::vector<uint8_t>> output_frames;

    int corr_64(uint64_t v1, uint64_t v2, uint64_t mask)
    {
        int cor = 0;
        uint64_t diff = (v1 ^ v2) & mask;
        for(int j=63; j>=0; j--){
            if(diff >> j & 0b1){
                cor++;
            }
        }
        return cor;
    }

    uint8_t byte_shifter;
    int in_byte_buffer = 0;

    void push_bit(uint8_t bit)
    {
        byte_shifter = (byte_shifter << 1) | bit;
        in_byte_buffer++;
        if (in_byte_buffer == 8)
        {
            current_frame.push_back(byte_shifter);
            in_byte_buffer = 0;
        }
    }
    uint64_t hexStringToUint64(const std::string& hexStr);
    uint64_t asm_shifter = 0;
    size_t offset = 0;
    uint8_t bit;

public:
    deframer_impl(std::string syncword,
                  int syncword_bit_length,
                  int frame_length_bits,
                  int thresold);
    ~deframer_impl();

    // Where all the action really happens
    void forecast(int noutput_items, gr_vector_int& ninput_items_required);

    int general_work(int noutput_items,
                     gr_vector_int& ninput_items,
                     gr_vector_const_void_star& input_items,
                     gr_vector_void_star& output_items);
};

} // namespace Fengyun2
} // namespace gr

#endif /* INCLUDED_FENGYUN2_DEFRAMER_IMPL_H */
