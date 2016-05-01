import os
import glob
import commands

for name in glob.glob('*/*.html'):
    basename, ext = os.path.splitext(name)
    print basename

    cmd = 'pdfreactor.py -i {} -o {}.pdf'.format(name, basename)
    cmd = 'prince {} {}.pdf'.format(name, basename)
    os.system(cmd)

    cmd  = 'convert -density 300 {}.pdf[0] -resize 400 {}.png'.format(basename, basename)
    os.system(cmd)

    cmd  = 'git add {}.png'.format(basename)
    os.system(cmd)
