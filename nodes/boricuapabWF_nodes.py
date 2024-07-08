
class BoricuapabWFPrintHelloPuertoRicanWorld:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required":{
                    "text": ("STRING", {"multiline": False, "default": "BoricuapabWF Hello Puerto Rican World"}),
                    }
                }
    
    RETURN_TYPES = ()
    FUNCTION = "print_BoricuapabWFHWText"
    OUTPUT_NODE = True
    CATEGORY = "BoricuapabWF Nodes"

    def print_BoricuapabWFHWText(self, text):
        print(f"BoricuapabWF HW Text : {text}")

        return{}
    
class BoricuapabWFPrintPuertoRican:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required":{
                    "text": ("STRING", {"multiline": False, "default": "BoricuapabWF Puerto Rican"}),
                    }
                }
    
    RETURN_TYPES = ()
    FUNCTION = "print_BoricuapabWFPuertoRican"
    OUTPUT_NODE = True
    CATEGORY = "BoricuapabWF Nodes"

    def print_BoricuapabWFPuertoRican(self, text):
        print(f"BoricuapabWF Puerto Rican Text : {text}")

        return{}

class BoricuapabWFConcatenateHelloWorld:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required": {
                    "textLine1": ("STRING", {"multiline": False, "default": "Hello Puerto"}),
                    "textLine2": ("STRING", {"multiline": False, "default": "Rican World"}),
                    }            
                }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "BWF_concatenate_text"
    CATEGORY = "BoricuapabWF Nodes"

    def BWF_concatenate_text (self, textLine1, textLine2):
        text_out = textLine1 + " " + textLine2
        return(text_out, )
    
class BoricuapabWFINT:

    @classmethod
    def INPUT_TYPES(cls):
        
        return {"required": {
                    "Whole Number": ("INT", {"default": 1, "min": 0, "max": 9999999999999}),
                    }
                }

    RETURN_TYPES = ("INT", )
    FUNCTION = "BWF_INT"
    CATEGORY = "BoricuapabWF Nodes"

    def BWF_INT (self, Number):
        try:
            return_value = int(Number)
        except Exception:
            raise Exception("You've input an incorrect value for BWF INT")
        return (return_value, )
