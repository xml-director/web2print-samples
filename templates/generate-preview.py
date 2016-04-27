import os
import glob
import commands

for name in glob.glob('*/*.html'):
    basename, ext = os.path.splitext(name)

    cmd = 'pdfreactor.py -i {} -o {}.pdf'.format(name, basename)
    print cmd
    os.system(cmd)

    cmd  = 'convert -density 300 {}.pdf -resize 400 {}.png'.format(basename, basename)
    print cmd
    os.system(cmd)


