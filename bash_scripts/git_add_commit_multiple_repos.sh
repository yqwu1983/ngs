#!/bin/bash
for DIR in `ls`;
do
    if [ -d $DIR/.git ];
    then
            echo "updating location: " $DIR;
            cd $DIR
            # your commands here...
             git add --all
            #git add -u
            #git add .
            git commit -m 'Latest'

            cd ..
    fi
done