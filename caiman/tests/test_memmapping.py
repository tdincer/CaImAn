from caiman import mmapping

def test_load_raises_wrong_ext():
    fname = "a.mmapp"
    try:
        mmapping.load_memmap(fname)
    except ValueError:
        assert True
    else:
        assert False

def test_load_raises_multiple_ext():
    fname = "a.mmap.mma"
    try:
        mmapping.load_memmap(fname)
    except ValueError:
        assert True
    else:
        assert False
