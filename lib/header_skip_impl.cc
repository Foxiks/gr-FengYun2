/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "header_skip_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace Fengyun2 {

using input_type = unsigned char;
using output_type = unsigned char;
header_skip::sptr header_skip::make(int skip_bytes)
{
    return gnuradio::make_block_sptr<header_skip_impl>(skip_bytes);
}


/*
 * The private constructor
 */
header_skip_impl::header_skip_impl(int skip_bytes)
    : gr::block("header_skip",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type))),
                d_skip_bytes(skip_bytes)
{
}

/*
 * Our virtual destructor.
 */
header_skip_impl::~header_skip_impl() {}

void header_skip_impl::forecast(int noutput_items, gr_vector_int& ninput_items_required)
{
//#pragma message(
    //"implement a forecast that fills in how many items on each input you need to produce noutput_items and remove this warning")
    ninput_items_required[0] = 44356;
}

int header_skip_impl::general_work(int noutput_items,
                                   gr_vector_int& ninput_items,
                                   gr_vector_const_void_star& input_items,
                                   gr_vector_void_star& output_items)
{
    auto in = static_cast<const input_type*>(input_items[0]);
    auto out = static_cast<output_type*>(output_items[0]);


    // Do <+signal processing+>
    // Tell runtime system how many input items we consumed on
    // each input stream.
    std::memcpy(out, in + d_skip_bytes, ninput_items[0] - d_skip_bytes);
    consume_each(ninput_items[0]);

    // Tell runtime system how many output items we produced.
    return (int)(ninput_items[0] - d_skip_bytes);
}

} /* namespace Fengyun2 */
} /* namespace gr */
