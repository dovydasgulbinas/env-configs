#!/usr/bin/env bash

set -euo pipefail

#/
#/ Usage: 
#/ ./casbab.sh option [string]
#/ 
#/ Description:
#/ CLI "tool" and a bash "library" for converting representation style of compound words or phrases
#/ 
#/ Examples:
#/ Read from stdin
#/ $ echo camel-Snake-Kebab | ./casbab.sh camel
#/ $ camelSnakeKebab
#/
#/ Pass as a argument
#/ $ ./casbab.sh pascal Camel Snake Kebab
#/ $ CamelSnakeKebab
#/
#/ You can source this file and use it's functions
#/ camel camelSnakeKebab
#/
#/ Options:

usage() { grep '^#/' "$0" | cut -c4- ; exit 0 ; }
expr "$*" : ".*--help" > /dev/null && usage

if [ -f "$BASH_MODULES_DIR/casbab.sh" ]; then
. "$BASH_MODULES_DIR/casbab.sh"
else
    echo "failed to load casbab.sh module!"
    exit 0;
fi

new(){
    # fixme: add output to the variable!
    echo "# $1" >> "$STICKIES_DIR/$(kebab $1).md"
    $EDITOR "$STICKIES_DIR/$(kebab $1).md"
    exit 0
}


list(){
    ls -t $STICKIES_DIR
}

walk(){
    $TERM_FILE_MANAGER $STICKIES_DIR
}


if [[ "${BASH_SOURCE[0]}" = "$0" ]]; then

  arg=( "${@:2}" )

  if [[ -t 0 && -z ${arg[*]} ]]; then
    if [[ ${#arg[*]} -eq 1 ]]; then
      arg[0]=' '
    else
      usage
    fi 
  fi
  
  arg=( ${arg:-$(cat -)} )

  case ${1:-} in
    new)
      new "${arg[*]:-""}"
    ;;
    ls)
      list "${arg[*]:-""}"
    ;;
    walk)
      walk "${arg[*]:-""}"
    ;;
    camelsnake)
      camelsnake "${arg[*]:-""}"
    ;;
    screamingsnake)
      screamingsnake "${arg[*]:-""}"
    ;;
    kebab)
      kebab "${arg[*]:-""}"
    ;;
    camelkebab)
      camelkebab "${arg[*]:-""}"
    ;;
    screamingkebab)
      screamingkebab "${arg[*]:-""}"
    ;;
    lower)
      lower "${arg[*]:-""}"
    ;;
    title)
      title "${arg[*]:-""}"
    ;;
    screaming)
      screaming "${arg[*]:-""}"
    ;;
    *)
      usage
    ;;
  esac
fi
