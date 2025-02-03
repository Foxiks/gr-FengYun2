/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "derandomizer_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace Fengyun2 {

//#pragma message("set the following appropriately and remove this warning")
using input_type = unsigned char;
//#pragma message("set the following appropriately and remove this warning")
using output_type = unsigned char;
derandomizer::sptr derandomizer::make()
{
    return gnuradio::make_block_sptr<derandomizer_impl>();
}

uint8_t * derandomizer_impl::PNDerandomizer()
{
    derandTable = new uint8_t[354848];

    // Generate derandomization table
    int oo = 0;
    uint8_t currentByteShifter = 0;
    int inCurrentByteShiter = 0;

    uint16_t shifter = 0b011001110011111;

    for (int i = 0; i < 10000 + 354848; i++)
    {
        bool xor1 = getBit<uint16_t>(shifter, 14);
        bool xor2 = getBit<uint16_t>(shifter, 13);
        bool outBit = xor1 ^ xor2;

        shifter = shifter << 1 | outBit;

        if (i >= 10000)
        {
            currentByteShifter = currentByteShifter << 1 | outBit;
            inCurrentByteShiter++;

            if (inCurrentByteShiter == 8)
            {
                derandTable[oo++] = currentByteShifter;
                inCurrentByteShiter = 0;
            }
        }
    }
    return derandTable;
}


/*
 * The private constructor
 */
derandomizer_impl::derandomizer_impl()
    : gr::block("derandomizer",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type)))
{
}

/*
 * Our virtual destructor.
 */
derandomizer_impl::~derandomizer_impl() {
    delete[] derandTable;
}

void derandomizer_impl::forecast(int noutput_items, gr_vector_int& ninput_items_required)
{
//#pragma message(
    //"implement a forecast that fills in how many items on each input you need to produce noutput_items and remove this warning")
    ninput_items_required[0] = 44356;
}

int derandomizer_impl::general_work(int noutput_items,
                                    gr_vector_int& ninput_items,
                                    gr_vector_const_void_star& input_items,
                                    gr_vector_void_star& output_items)
{
    auto in = static_cast<const input_type*>(input_items[0]);
    auto out = static_cast<output_type*>(output_items[0]);
    data.clear();

//#pragma message("Implement the signal processing in your block and remove this warning")
    // Do <+signal processing+>
    // Tell runtime system how many input items we consumed on
    // each input stream.
    for (int byten = 0; byten < 44356; byten++)
    {
        if (byten % 2 == 1)
            data.push_back((uint8_t)(0xFF - (derandTable[byten] ^ in[byten])));
        else
            data.push_back((uint8_t)(derandTable[byten] ^ in[byten]));
    }
    consume_each(44356);
    std::memcpy(out, data.data(), data.size());

    // Tell runtime system how many output items we produced.
    return 44356;
}

} /* namespace Fengyun2 */
} /* namespace gr */
