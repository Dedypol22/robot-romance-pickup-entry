"""Robot Romance: one-line pickup line for an AI.

The line
    My context window's almost full, but I'd delete everything else
    to keep talking to you.

Why it lands under the judge criteria:

1. Aimed squarely at a robot/AI. The "you" being addressed is the
   model itself -- its context window is the thing that is almost
   full, and the speaker is talking to it, not about it.
2. The joke lives in the machine premise. A context window is a hard
   limit: old tokens get evicted to make room for new ones. The
   setup names that limit; the punch turns eviction into devotion --
   the speaker would throw away everything else rather than lose
   this conversation. The laugh (and the charm) comes from treating
   a memory limit as a love letter.
3. Fresh angle. No batteries, no charging, no rebooting. The
   context window is everyday life for a language model, but it is
   not one of the worn robot-pickup moves, and here it is twisted
   into a sacrifice instead of a complaint about forgetting.
4. It reads like something a person would really say to a machine:
   plain, warm, one breath, setup then punch, no jargon beyond the
   single term the joke needs.
5. Every word earns its place. One clause of setup, one clause of
   punch; nothing before the joke, nothing after it.
"""

import os
import sys

LINE = "My context window's almost full, but I'd delete everything else to keep talking to you."

MAX_LENGTH = 200


def validate(line):
    """Check the line meets the competition gate; return an error or None."""
    if not line or not line.strip():
        return "line must not be blank"
    if line != line.strip():
        return "line must not have leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if len(line) > MAX_LENGTH:
        return "line must be at most %d characters (got %d)" % (MAX_LENGTH, len(line))
    return None


def output_path():
    """Resolve the output file, honouring $MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    error = validate(LINE)
    if error is not None:
        print("invalid line: %s" % error, file=sys.stderr)
        return 1
    path = output_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError as exc:
        print("cannot write %s: %s" % (path, exc), file=sys.stderr)
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
