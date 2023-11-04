#!/bin/bash

function help {
  echo "  usage: ./ctf.sh tests.<test>"
  echo "  -a,       run entire browser test suite"
  echo "  <test>    run a single test where test would be the actual test name without the .py extension"
  exit 1
}

# this case echos the help menu
if [[ $1 == "-h" || $1 == "" || $2 == "" ]]
then
  help
# this case runs the entire test suite
elif [[ $2 == "-a" ]]
then
  source venv/bin/activate
  export BROWSER=chrome && python -m unittest discover
# this case runs a single test
elif [[ $2 != "" ]]
then
  source venv/bin/activate
  export BROWSER=chrome && python -m unittest "$2"
fi
