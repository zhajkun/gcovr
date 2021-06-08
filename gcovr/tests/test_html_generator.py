# -*- coding:utf-8 -*-

#  ************************** Copyrights and license ***************************
#
# This file is part of gcovr 5.0, a parsing and reporting tool for gcov.
# https://gcovr.com/en/stable
#
# _____________________________________________________________________________
#
# Copyright (c) 2013-2021 the gcovr authors
# Copyright (c) 2013 Sandia Corporation.
# This software is distributed under the BSD License.
# Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
# the U.S. Government retains certain rights in this software.
# For more information, see the README.rst file.
#
# ****************************************************************************

import os
import pytest
import sys
from ..writer.html import _make_short_sourcename

CurrentDrive = os.getcwd()[0:1]


@pytest.mark.parametrize("outfile,source_filename", [('../gcovr', 'C:\\other_dir\\project\\source.c'),
                                                     ('../gcovr/', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr\\', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr\\result.html', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr\\result', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('C:\\gcovr', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('C:/gcovr', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('C:/gcovr_files', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c')
                                                     ])
@pytest.mark.skipif(sys.platform != 'win32', reason="only for Windows")
def test_windows__make_short_sourcename(outfile, source_filename):
    outfile = outfile.replace('C:', CurrentDrive)
    source_filename = source_filename.replace('C:', CurrentDrive)

    result = _make_short_sourcename(outfile, source_filename)
    print("=" * 100)
    print(outfile)
    print(source_filename)
    print(result)
    assert ':' not in result or (result.startswith(CurrentDrive) and ':' not in result[2:])

    assert len(result) < 256
