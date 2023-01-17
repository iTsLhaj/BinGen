#!/bin/bash -e

clear

types=( INFO DEBUG ERROR NOTSET )

echo -e "\n - You can leave it blank Level well be INFO by default or pick one ! "
echo -e " - Choose A Logging LEVEL[ERROR/INFO/DEBUG/NOTSET] \c"
read -r

save()
{
    echo "LoggingLevel: $1" > config.yaml
    echo "config file created successfully"

    pip install -r requirements.txt
    echo "pip pkgs installed !"
    clear
    exit
}

for i in "${types[@]}"
do
    if [ "$REPLY" == "$i" ]
    then
            echo "LEVEL: $i"
            save $i
    fi
done

echo "LEVEL: $types"
save $types

exit