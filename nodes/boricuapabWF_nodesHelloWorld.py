
class PrintBoricuapabWFHelloWorld:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required":{
                    "text": ("STRING", {"multiline": False, "default": "BoricuapabWF Hello World"}),
                    }
                }
    
    RETURN_TYPES = ()
    FUNCTION = "print_BoricuapabWFHWText"
    OUTPUT_NODE = True
    CATEGORY = "BoricuapabWF Nodes"

    def print_BoricuapabWFHWText(self, text):
        print(f"BoricuapabWF HW Text : {text}")

        return{}
