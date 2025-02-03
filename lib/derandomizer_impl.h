/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FENGYUN2_DERANDOMIZER_IMPL_H
#define INCLUDED_FENGYUN2_DERANDOMIZER_IMPL_H

#include <gnuradio/Fengyun2/derandomizer.h>

namespace gr {
namespace Fengyun2 {

class derandomizer_impl : public derandomizer
{
private:
    uint8_t *derandTable = PNDerandomizer();
    std::vector<uint8_t> data;
    template <typename T>
    inline bool getBit(T data, int bit)
    {
        return (data >> bit) & 1;
    }

public:
    uint8_t * PNDerandomizer();
    derandomizer_impl();
    ~derandomizer_impl();

    // Where all the action really happens
    void forecast(int noutput_items, gr_vector_int& ninput_items_required);

    int general_work(int noutput_items,
                     gr_vector_int& ninput_items,
                     gr_vector_const_void_star& input_items,
                     gr_vector_void_star& output_items);
};

} // namespace Fengyun2
} // namespace gr

#endif /* INCLUDED_FENGYUN2_DERANDOMIZER_IMPL_H */
