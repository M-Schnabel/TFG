import gc
import os

def df():
    s = os.statvfs('//')
    print('Free file space')
    print('{0} MB'.format((s[0]*s[3])/1048576))

def free(full=False):
    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F+A
    P = '{0:.2f}%'.format(F/T*100)
    print('Available RAM')
    if not full:
        print(P)
    else :
        print('Total:{0} Free:{1} ({2})'.format(T,F,P))

if __name__ == '__main__':
    df()
    free()