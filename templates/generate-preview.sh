#!/bin/bash

for name in *html
    base=`basename $name html`
    print base
done
