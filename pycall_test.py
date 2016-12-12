#!/usr/bin/env python

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# !in this way docs source moudule, not the installed one
sys.path.insert(0, os.path.abspath('../'))



from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from pycallgraph import Config

graphviz = GraphvizOutput()
graphviz.output_file = 'basic.png'

config = Config(max_depth=1)

with PyCallGraph(output=graphviz,config=config):
    from SL_clustering_tools import detection
      