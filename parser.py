
from sys import argv
from parse import parse



def make_student_view(input_file_name, output_file_name):
    stack = []
    def print_or_hide(line):
        if len(stack) == 0:
            output_file.write(line)
        else:
            if stack[-1]['type'] in ['hide', 'entry']:
                pass
            elif stack[-1]['type'] in ['question']:
                if line[0:2] == '@@':
                    output_file.write(line)
                else:
                    output_file.write('\n')
            else:
                output_file.write(line)
    with open(input_file_name) as input_file:
        with open(output_file_name,mode='w') as output_file:
            for line in input_file:
                if line[0:2] == "@@":
                    parts = line[2:-1].split(' ')
                    while parts[0] == '':
                        parts = parts[1:]
                    if parts[0] == 'begin':
                        stack.append({'type':parts[1]})
                        print_or_hide(line)
                    elif parts[0] == 'end':
                        print_or_hide(line)
                        if stack[-1]['type'] != parts[1]:
                            raise ValueError('Cant end what you didn\'t begin')
                        else:
                            stack.pop()
                    elif parts[0][-1] == ':':
                        stack[-1][parts[0][:-1]] = ' '.join(parts[1:])
                        # Forward this info to student
                        output_file.writelines(line)
                    else:
                        print ('possible gibberish: ', line)
                        # Forward this info to student
                        output_file.writelines(line)
                else:
                    print_or_hide(line)


def main():
    make_student_view(argv[1], argv[2])

if __name__ == '__main__':
    main()

