class NullStrToNull(str):
    def default(str):
        if(str.lower() in ("null")):
            return None
        
        return str
