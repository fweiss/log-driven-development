import re

LOGFILE = "../../examples/rsvp-agent-processing.log"

# using multi line string concatenation to aid readability
# using (?P<>...) to name match groups
pattern = re.compile((
    "(?P<timestamp>\d\d/\d\d \d\d:\d\d:\d\d)"
    " "
    "(?P<level>[A-Z]+)"
    "[ ]*:"
    "(?P<depth>\.*)"
    "(?P<tag>\w+)"
    ": "
    "(?P<message>.+)"))

# interesting tags:
# rsvp_flow_stateMachine
def filter(tag):
    return tag == "reg_process"

def main():
    with open(LOGFILE) as f:
        count = 0
        tags = set()
        for line in f:
            matched = pattern.match(line)
            if matched:
                count += 1
                tags.add(matched.groupdict()["tag"])

                if (filter(matched.groupdict()["tag"])):
                    # print(matched.groupdict())
                    print(matched.groups())
        print(count)
        print(tags)

if __name__ == "__main__":
    main()