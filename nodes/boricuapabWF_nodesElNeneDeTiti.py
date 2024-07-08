
class PrintBoricuapabWFElNeneDeTiti:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required":{
                    "text": ("STRING", {"multiline": False, "default": "BoricuapabWF El Nene De Titi"}),
                    }
                }
    
    RETURN_TYPES = ()
    FUNCTION = "print_BoricuapabWFElNeneDeTitiText"
    OUTPUT_NODE = True
    CATEGORY = "BoricuapabWF Nodes"

    def print_BoricuapabWFElNeneDeTitiText(self, text):
        print(f"BoricuapabWF El Nene De Titi Text : {text}")

        return{}
