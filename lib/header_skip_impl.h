/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FENGYUN2_HEADER_SKIP_IMPL_H
#define INCLUDED_FENGYUN2_HEADER_SKIP_IMPL_H

#include <gnuradio/Fengyun2/header_skip.h>

namespace gr {
namespace Fengyun2 {

class header_skip_impl : public header_skip
{
private:
    int d_skip_bytes;

public:
    header_skip_impl(int skip_bytes);
    ~header_skip_impl();

    // Where all the action really happens
    void forecast(int noutput_items, gr_vector_int& ninput_items_required);

    int general_work(int noutput_items,
                     gr_vector_int& ninput_items,
                     gr_vector_const_void_star& input_items,
                     gr_vector_void_star& output_items);
};

} // namespace Fengyun2
} // namespace gr

#endif /* INCLUDED_FENGYUN2_HEADER_SKIP_IMPL_H */
