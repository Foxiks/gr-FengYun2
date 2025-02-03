/* -*- c++ -*- */
/*
 * Copyright 2025 Egor UB1QBJ.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FENGYUN2_HEADER_SKIP_H
#define INCLUDED_FENGYUN2_HEADER_SKIP_H

#include <gnuradio/Fengyun2/api.h>
#include <gnuradio/block.h>

namespace gr {
namespace Fengyun2 {

/*!
 * \brief <+description of block+>
 * \ingroup Fengyun2
 *
 */
class FENGYUN2_API header_skip : virtual public gr::block
{
public:
    typedef std::shared_ptr<header_skip> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of Fengyun2::header_skip.
     *
     * To avoid accidental use of raw pointers, Fengyun2::header_skip's
     * constructor is in a private implementation
     * class. Fengyun2::header_skip::make is the public interface for
     * creating new instances.
     */
    static sptr make(int skip_bytes = 0);
};

} // namespace Fengyun2
} // namespace gr

#endif /* INCLUDED_FENGYUN2_HEADER_SKIP_H */
