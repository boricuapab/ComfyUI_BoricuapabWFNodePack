
from .nodes.boricuapabWF_nodesHelloWorld import *
from .nodes.boricuapabWF_nodesElNeneDeTiti import *

NODE_CLASS_MAPPINGS = {
    # Add mappings here
    "Print BoricuapabWF Hello World": PrintBoricuapabWFHelloWorld,
    "Print BoricuapabWF El Nene De Titi": PrintBoricuapabWFElNeneDeTiti,
}

print("\033[34mComfyUI_BoricuapabWFNodePack Nodes: \033[92mLoaded\033[0m")
