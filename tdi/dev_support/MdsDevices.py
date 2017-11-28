def MdsDevices():
    from MDSplus import Device,tdi,version
    from numpy import array
    def importDevices(name):
        bname = version.tobytes(name)
        try:
            module = __import__(name)
            ans = [[version.tobytes(k),bname] for k,v in module.__dict__.items() if isinstance(v,int.__class__) and issubclass(v,Device)]
        except ImportError: ans = []
        tdidev = tdi("if_error(%s(),*)"%name)
        if tdidev is None: return ans
        return tdidev.value.reshape((int(tdidev.value.size/2),2)).tolist()+ans
    ans = [[version.tobytes(d),b'pydevice'] for d in Device.findPyDevices()]
    for module in ["KbsiDevices","MitDevices","RfxDevices","W7xDevices"]:
        ans += importDevices(module)
    ans = array(list(dict(ans).items()))
    ans.view('%s,%s'%(ans.dtype,ans.dtype)).sort(order=['f0'], axis=0)
    return ans
