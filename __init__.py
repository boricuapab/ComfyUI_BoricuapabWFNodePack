
from .nodes.boricuapabWF_nodes import *
#from .nodes.boricuapabWF_nodesElNeneDeTiti import *

NODE_CLASS_MAPPINGS = {
    # Add mappings here
    "BoricuapabWF Print Hello Puerto Rican World": BoricuapabWFPrintHelloPuertoRicanWorld,
    "BoricuapabWF Print Puerto Rican": BoricuapabWFPrintPuertoRican,
    "BoricuapabWF Concatenate Hello World": BoricuapabWFConcatenateHelloWorld,
}

print("\033[34mComfyUI_BoricuapabWFNodePack Nodes: \033[92mLoaded\033[0m")
