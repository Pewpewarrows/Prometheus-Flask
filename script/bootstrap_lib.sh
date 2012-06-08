#!/usr/bin/env sh

# Avoid double includsion
if [[ "${BashInclude__imported+defined}" == "defined" ]]; then
    return 0
fi
BashInclude__imported=1

Bootstrap__os=Linux
case `uname` in
    Darwin)
        Bootstrap__os=Darwin
        ;;
esac

# For a good example of why you should never upgrade a system-default
# interpreter for a dynamic language:
#
#   find /usr -name '*.rb'
#   find /usr -name '*.py'
#
# Those are program files that depend on the version of ruby/python that comes
# with your OS. Upgrading the system-default interpreter will introduce
# backwards-incompatibilities that can and will bring those programs to a halt.
# Instead, use tools like rvm, rbenv, or pythonbrew to manage user / project
# installations of those languages.

function Bootstrap__silent_cmd {
    local command_line="$1"

    `${command_line} >/dev/null 2>&1`
}

function Bootstrap__is_available {
    local command_name="$1"

    Bootstrap__silent_cmd "command -v ${command_name}"
}

function Bootstrap__check_for_progs {
    local missing=() prog

    for prog; do
        if ! Bootstrap__is_available "$prog"; then
            missing+=("$prog")
        fi
    done

    if (( ${#missing[@]} )); then
        echo >&2 "$0: the following required commands were not found:"
        printf >&2 "\t%s\n" "${missing[@]}"
        return 1
    fi

    return 0
}

function Bootstrap__python_available {
    # TODO: version argument
    Bootstrap__is_available "python"
}

function Bootstrap__ruby_available {
    # TODO: version argument
    Bootstrap__is_available "ruby"
}

function Bootstrap__pythonbrew_available {
    # TODO: version argument

    if ! Bootstrap__is_available "pythonbrew"; then
        echo "Instructions"
        return 1
    fi

    return 0
}

# Pip
# PyBrew Python Version
# PyBrew Virtualenv
# Virtualenv Requirements
# Gem bundle
# Rbenv
# Node.js
# NPM stuff

# Sqlite
# Postgres
# Mysql

# Git/Hg hooks
# Tmux/tmuxinator stuff?
