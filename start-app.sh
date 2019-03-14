#!/usr/bin/env bash

na="[start-PyTkCad]: "


do_help () {
    if [ ! "$1" = "" ]; then 
        echo
        echo "$(cat ,/$1)"
        echo
        return
    fi
    printf "start "$0" with one of the following ways \n\n"
    for i in ,/*; do 
        printf "$0 $i\n"
        echo "$(cat $i)"
        echo
    done
}

do_complete () {
    if [ "$2" = 0 ]; then 
        echo $na$1 complete
        echo $na complete
    else 
        echo $na$1 error
        echo $na error
    fi
    exit $2 
}
do_check () {
    if [ "$2" = 0 ]; then 
        echo $na$1 complete
        return $2
    else 
        echo $na$1 error
        if [ ! "$3" = "easy" ]; then exit $2; else return $2; fi
    fi
}


if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then 
    me="help" 
	printf "$na$me\n\n"
    do_help
    do_complete "$me" $?
fi


if [ "$1" = ",/anckor" ]; then
    me="anckor" 
	echo $na$me
    do_help "$me" 
	echo $na$me "fixing .desktop files..."
	# Fix up .desktop Icon.
    sed -i -e "s,^Icon=.*,Icon=$PWD/media/PyTkCad_icon_main.png,g" start-PyTkCad.desktop
    sed -i -e "s,^Exec=.*,Exec=python $PWD/PyTkCad.pyw,g" start-PyTkCad.desktop
    sed -i -e "s,^Path=.*,Path=$PWD,g" start-PyTkCad.desktop
    do_complete "$me" $?
fi

if [ "$1" = ",/anckor-remove" ]; then
    me="anckor-remove" 
	echo $na$me
    do_help "$me"  
	echo $na$me "fixing .desktop files..."
	# Fix up .desktop Icon.
    sed -i -e "s,^Icon=.*,Icon=dialog-warning,g" start-PyTkCad.desktop
    sed -i -e "s,^Exec=.*,Exec=./start-app.sh,g" start-PyTkCad.desktop
    sed -i -e "s,^Path=.*,Path=,g" start-PyTkCad.desktop
    do_complete "$me" $?
fi


echo "starting PyTkCad"
python PyTkCad.pyw


