

def hookDebugger(debugger='gdb'):
    """debugging helper, hooks debugger to running interpreter process
    """
    import os
    pid = os.spawnvp(os.P_NOWAIT,
                     debugger, [debugger, '-q', 'python', str(os.getpid())])
    
    # give debugger some time to attach to the python process
    import time
    time.sleep( 1 )
    
    # verify the process' existence (will raise OSError if failed)
    os.waitpid( pid, os.WNOHANG )
    os.kill( pid, 0 )
    return
