/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "deframer_impl.h"
#include <gnuradio/io_signature.h>
#include <cstdint>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

namespace gr {
namespace Fengyun2 {

//#pragma message("set the following appropriately and remove this warning")
using input_type = unsigned char;
//#pragma message("set the following appropriately and remove this warning")
using output_type = unsigned char;
deframer::sptr deframer::make(std::string syncword,
                              int syncword_bit_length,
                              int frame_length_bits,
                              int thresold)
{
    return gnuradio::make_block_sptr<deframer_impl>(
        syncword, syncword_bit_length, frame_length_bits, thresold);
}

uint64_t deframer_impl::hexStringToUint64(const std::string& hexStr) {
    uint64_t result = 0;
    std::stringstream ss;
    ss << std::hex << hexStr;
    ss >> result;

    return result;
}

/*
 * The private constructor
 */
deframer_impl::deframer_impl(std::string syncword,
                             int syncword_bit_length,
                             int frame_length_bits,
                             int thresold)
    : gr::block("deframer",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type))),
                d_syncword(syncword),
                d_syncword_length(syncword_bit_length),
                d_frame_length(frame_length_bits),
                d_thresold(thresold)
{
    d_sync_mask = 0;
    for (int i = 0; i < (int)syncword_bit_length; i++){
        d_sync_mask = (d_sync_mask << 1) + 1;
    }
    d_work_syncword = hexStringToUint64(d_syncword);
    //printf("\nSyncword: %lu \nSyncword Length: %d \nFrame Length: %d \nThresold: %d \n", d_work_syncword, d_syncword_length, d_frame_length, d_thresold);
}

/*
 * Our virtual destructor.
 */
deframer_impl::~deframer_impl() {
}

void deframer_impl::forecast(int noutput_items, gr_vector_int& ninput_items_required)
{

}

int deframer_impl::general_work(int noutput_items,
                                gr_vector_int& ninput_items,
                                gr_vector_const_void_star& input_items,
                                gr_vector_void_star& output_items)
{
    auto in = static_cast<const input_type*>(input_items[0]);
    auto out = static_cast<output_type*>(output_items[0]);

    send_size = 0;
    offset = 0;
    for (int byten = 0; byten < ninput_items[0]; byten++)
    {
        for (int i = 7; i >= 0; i--)
        {
            bit = (in[byten] >> i) & 0b1;
            
            asm_shifter = (asm_shifter << 1 | bit) & d_sync_mask; //% d_sync_modulo;
            
            if (in_frame)
            {
                push_bit(bit);

                if ((int)current_frame.size() * 8 == d_frame_length)
                {
                    output_frames.push_back(current_frame);
                    in_frame = false;
                    if((int)output_frames.size() > 0){
                        for (const auto& vec : output_frames) {
                            std::memcpy(out + offset, vec.data(), vec.size());
                            offset += vec.size();
                        }
                        send_size = offset;
                        output_frames.clear();
                    }
                    current_frame.clear();
                }
                continue;
            } else {
                if(corr_64(d_work_syncword, asm_shifter, d_sync_mask) <= d_thresold)
                {
                    if (in_frame)
                    {
                        // Fill up what we're missing
                        while ((int)current_frame.size() * 8 < d_frame_length)
                            push_bit(0);
                        output_frames.push_back(current_frame);
                    }

                    in_frame = true;
                }
            }
        }
    }
    consume_each(ninput_items[0]);

    // Tell runtime system how many output items we produced.
    return send_size;
}

} /* namespace Fengyun2 */
} /* namespace gr */
