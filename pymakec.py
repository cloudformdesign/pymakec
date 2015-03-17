
#!/usr/bin/python
import os
import glob
import subprocess
import itertools
pjoin = os.path.join


__version__ = '0.0.1'


# standard cflags
cflags = ['g', 'O2', 'Wall', 'Wextra', 'Isrc', 'rdynamic', 'DNDEBUG']

# standard compiler name
cc = 'cc'


def isiter(obj, exclude=(str, bytes, bytearray)):
    '''Returns True if object is an iterator.

    Arguments:
        exclude (tuple, optional): types to exclude from "iter" type
            In most applications you want to know whether something is a
            list, typle, generator, numpy array, etc... a string or bytes
            type is considered a constant, not an iterator.
    '''
    return (False if isinstance(obj, exclude)
            else True if hasattr(obj, '__iter__')
            else False)


def makeiter(obj):
    if not isiter(obj):
        obj = (obj,)
    return obj


def cfiles(path):
    '''Get all *.c files'''
    path = makeiter(path)
    return itertools.chain.from_iterable(
        glob.glob(pjoin(p, '*.c')) for p in path)


def cppfiles(path):
    '''Get all *.cpp files'''
    path = makeiter(path)
    return itertools.chain.from_iterable(
        glob.glob(pjoin(p, '*.cpp')) for p in path)


def hfiles(path):
    '''Get all *.h files'''
    path = makeiter(path)
    return itertools.chain.from_iterable(
        glob.glob(pjoin(p, '*.h')) for p in path)


def cleanfiles(path, extensions=('.o', '.gc', '.dSYM')):
    path = makeiter(path)
    return itertools.chain.from_iterable(
        glob.glob(pjoin(p, ext)) for p in path for ext in extensions)


def sourcefiles(path):
    '''Get all c, cpp and h files'''
    path = makeiter(path)
    return itertools.chain.from_iterable(files(p) for files in
                                         (cfiles, cppfiles, hfiles)
                                         for p in path)


def testfiles(sourcefiles, end='.c'):
    '''Convert all *.c files into program files

    Used to make a whole folder of tests'''
    return (o[:-2] for o in sourcefiles if o.endswith(end))


def clean(cleanfiles):
    '''remove given cleanfiles'''
    for c in cleanfiles:
        os.remove(c)


def compile(sourcefiles, testfiles=None, outputs=None, cleanfiles=None):
    '''Compile all files'''
    if not testfiles:
        testfiles = ()
    str_sources = ' '.join(itertools.chain(sourcefiles, testfiles))
    str_outputs = ' '.join(outputs)
    call = "{cc} {cflags} {sources} -o {outputs}".format(
        cc=cc, cflags=' '.join('-{}'.format(cf) for cf in cflags),
        sources=str_sources, outputs=str_outputs)
    if cleanfiles:
        clean(cleanfiles)
    subprocess.check_call(call, shell=True)


def runtests(path):
    '''run all tests'''
    makeiter(path)
    for p in path:
        files = glob.glob(pjoin(p, '*'))
        for f in files:
            if 'test' in f and '.' not in f and not os.path.isdir(f):
                print('\n#' * 50)
                print('### Running test: {}'.format(f))
                subprocess.check_call('sh {}'.format(f), shell=True)
