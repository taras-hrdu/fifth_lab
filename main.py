import re


def cause_found():
    results = []
    caused_found = False
    with open('server.log') as log_file:
        pattern = r'Caused by'
        for line in log_file.readlines():
            if re.search(pattern, line):
                results.append(line)
                caused_found = True

            elif caused_found and re.search(r'}', line):
                caused_found = False
                results[-1] += line
            elif caused_found:
                results[-1] += line
        return results


def war_found(array):
    results = []
    pattern = r'\.war\\'
    for element in array:
        if re.search(pattern, element):
            results.append(element)
    return results


def main():
    output = cause_found()
    count = 0
    found_lines = war_found(output)
    for element in found_lines:
        print(element)
        count += 1
    print(count)


if __name__ == '__main__':
    main()
