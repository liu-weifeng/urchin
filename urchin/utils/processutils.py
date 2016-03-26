try:
    from eventlet.green import subprocess
except:
    import subprocess

def execute(*cmd, **kwargs):

    try:
        _PIPE = subprocess.PIPE
        obj = subprocess.Popen(cmd,
                               stdin=_PIPE,
                               stdout=_PIPE,
                               stderr=_PIPE)    
    
        try:
            result = obj.communicate()
            obj.stdin.close()
            _returncode = obj.returncode
        except:
            pass

        return result
    except:
        pass

if __name__=="__main__":
    res = execute('ls','asd/')
    print res

