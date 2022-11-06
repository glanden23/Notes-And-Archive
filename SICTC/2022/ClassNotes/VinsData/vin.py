class VIN:
    def __init__(self,v):
        """__init__
        
        Arguments: VIN
        
        Will return 1 if VIN is invalid.
        """
        if (len(v) == 17):
            for c in v:
                if c in "IOQ":
                    print(f"Vin contained IOQ which means it is invalid: {v}")
                    return v
        else:
            print(f"Vin wasn't 17 in length: {v} ({len(v)})")
            return v
        self.wmi = v[0:3]
        self.vds = v[3:9]
        self.ser = v[9:]
    
    def __str__(self):
        return [self.wmi,self.vds,self.ser]