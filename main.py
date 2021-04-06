import re


def cause_found():
    results = []
    caused_found = False
    war_found = False
    found = ""
    with open('server.log') as log_file:
        pattern = r'Caused by'
        for line in log_file.readlines():
            if re.search(r'}', line):
                if caused_found and war_found:
                    results.append(found)
                    war_found = False
                caused_found = False
            if caused_found and re.search(r'\.war\\', line):
                found += line
                war_found = True
            if re.search(pattern, line):
                found = line
                caused_found = True  
        return results


def main():
    found_lines = cause_found()
    for element in found_lines:
        print(element)
    print(len(found_lines))


if __name__ == '__main__':
    main()