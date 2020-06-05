import os

def try1() -> None:
    from foo.bar.importing_module import ImportingModule
    im: ImportingModule = ImportingModule()
    print("Import with 'from foo.bar.importing_module import ImportingModule'")
    print("IM.foo: " + str(im.foo))
    print("IM.bar: "+ (im.bar))

def try2() -> None:
    import importlib
    factory_dir = os.path.dirname(__file__)
    module = importlib.import_module("foo.bar.importing_module")
    ds_class = getattr(module, "ImportingModule")
    im: ImportingModule = ds_class()
    print("Strange import with importlib.import_module and getattr")
    print("IM.foo: " + str(im.foo))
    print("IM.bar: "+ (im.bar))

def try3() -> None:
    pass


if __name__ == '__main__':
    print('first try:')
    try1()
    print('second try:')
    try2()
