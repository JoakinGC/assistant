

def check_string(field,length=10):
        if field:
            return False
        if isinstance(field,str):
            if len(field) <= length or len(field) > 0:
                return True

        return False  