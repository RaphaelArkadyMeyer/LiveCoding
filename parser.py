
from sys import argv
from parse import parse



def make_student_view(input_file_name, output_file_name):
    stack = []
    with open(input_file_name) as input_file:
        with open(output_file_name) as output_file:
            for line in input_file:
                if line[0:1] == "@@":
                    parts = line[2:].split(' ')
                    if parts[0] == 'begin':
                        stack.append({type:parts[1]})
                    elif parts[0] == 'end':
                        if stack[-1]['value'] != parts[1]:
                            raise ValueError('Cant end what you didn\'t begin')
                        else:
                            stack.pop()
                    elif parts[0][-1] == ':'
                        stack[-1][parts[0][:-2]] = parts[1:]
                        # Forward this info to student
                        output_file.writelines(line)
                    else
                        print ('possible gibberish: ', line)
                        # Forward this info to student
                        output_file.writelines(line)
                else:
                    # No preprocessing
                    output_file.writelines(line)


def main():
    make_student_view(argv[1], argv[2])

if __name__ == '__main__':
    main()

