import re

LOGFILE = "../../examples/rsvp-agent-processing.log"

pattern = re.compile("(\d\d/\d\d \d\d:\d\d:\d\d) ([A-Z]+)[ ]*:(\.*)(\w+): (.+)")
# pattern = re.compile("^(.+)$")

def main():
    with open(LOGFILE) as f:
        count = 0
        for line in f:
            matched = pattern.match(line)
            if matched:
                count += 1
                # print(matched.groupdict())
                print(matched.groups())
        print(count)

if __name__ == "__main__":
    main()