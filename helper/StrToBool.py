class Str2bool(str):
    def default(str):
        return str.lower() in ("True", "true","1")
