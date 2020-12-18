#!/usr/bin/env python

from __future__ import print_function
from mpi4py import MPI


comm = MPI.COMM_WORLD
if comm.rank==0:
    print("Saya Pertamax")
else:
    print("Saya anak ke %d dari %d bersaudara" % (comm.rank, comm.size))

comm.Barrier()

