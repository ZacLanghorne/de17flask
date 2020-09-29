if __name__ == '__main__':
    import sys
    # if someone is executing this directly.
    sys.exit()

class Child():
    pass

def whoami():
    return __name__
