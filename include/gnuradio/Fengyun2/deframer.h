/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FENGYUN2_DEFRAMER_H
#define INCLUDED_FENGYUN2_DEFRAMER_H

#include <gnuradio/Fengyun2/api.h>
#include <gnuradio/block.h>

namespace gr {
namespace Fengyun2 {

/*!
 * \brief <+description of block+>
 * \ingroup Fengyun2
 *
 */
class FENGYUN2_API deframer : virtual public gr::block
{
public:
    typedef std::shared_ptr<deframer> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of Fengyun2::deframer.
     *
     * To avoid accidental use of raw pointers, Fengyun2::deframer's
     * constructor is in a private implementation
     * class. Fengyun2::deframer::make is the public interface for
     * creating new instances.
     */
    static sptr make(std::string syncword,
                     int syncword_bit_length,
                     int frame_length_bits,
                     int thresold);
};

} // namespace Fengyun2
} // namespace gr

#endif /* INCLUDED_FENGYUN2_DEFRAMER_H */
