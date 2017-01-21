
from sys import argv
from parse import parse


class FileView:
    def __init__(self, text_file=None):
        self.lines = [] # [{text:"code", hidden:false, question=None/"name"}]
        if text_file:
            self.read(text_file)
    def read(self, text_file):
        stack = []
        state = 'root'
        for line in text_file:
            line_data = {
                'text':   line,
            }
            line = line[:-1]
            for stack_frame in stack[::-1]:
                if stack_frame['type'] in ['hide', 'entry']:
                    line_data['mode'] = 'hide'
                    break
                elif stack_frame['type'] in ['question']:
                    line_data['mode'] = 'blank'
                    break
            for stack_frame in stack[::-1]:
                if 'question' in stack_frame:
                    line_data['question'] = stack_frame['question']
                    break
            if line[0:2] == "@@":
                parts = line[2:].split(' ')
                parts = filter(None, parts)

                if parts[0] in ['begin', 'end'] and parts[1] in ['hide', 'entry']:
                    line_data['mode'] = 'hide'

                if parts[0] == 'begin':
                    stack_frame = { 'type':   parts[1] }
                    if parts[1] == 'question':
                        stack_frame['question'] = parts[2]
                    stack.append(stack_frame)
                elif parts[0] == 'end':
                    if stack[-1]['type'] != parts[1]:
                        raise ValueError('Could not find matching begin '+str(parts[1]))
                    else:
                        stack.pop()
                elif parts[0][-1] == ':':
                    stack[-1][parts[0][:-1]] = ' '.join(parts[1:])
                else:
                    print ('might be gibberish: ', line)
            print(stack)
            if 'mode' not in line_data:
                line_data['mode'] = 'normal'
            self.lines.append(line_data)

    def get_student_view(self):
        for line in self.lines:
            if line['mode'] == 'print':
                yield line['text']
            elif line['mode'] == 'blank':
                yield '\n'



def make_student_view(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        with open(output_file_name, mode='w') as output_file:
            fv = FileView(input_file)
            print(fv.lines)
            for line in fv.get_student_view():
                output_file.write(line)

# def make_student_view(input_file_name, output_file_name):
#    stack = []
#    def print_or_hide(line):
#        if len(stack) == 0:
#            output_file.write(line)
#        else:
#            if stack[-1]['type'] in ['hide', 'entry']:
#                pass
#            elif stack[-1]['type'] in ['question']:
#                if line[0:2] == '@@':
#                    output_file.write(line)
#                else:
#                    output_file.write('\n')
#            else:
#                output_file.write(line)
#    with open(input_file_name) as input_file:
#        with open(output_file_name,mode='w') as output_file:
#            for line in input_file:
#                if line[0:2] == "@@":
#                    parts = line[2:-1].split(' ')
#                    while parts[0] == '':
#                        parts = parts[1:]
#                    if parts[0] == 'begin':
#                        stack.append({'type':parts[1]})
#                        print_or_hide(line)
#                    elif parts[0] == 'end':
#                        print_or_hide(line)
#                        if stack[-1]['type'] != parts[1]:
#                            raise ValueError('Cant end what you didn\'t begin')
#                        else:
#                            stack.pop()
#                    elif parts[0][-1] == ':':
#                        stack[-1][parts[0][:-1]] = ' '.join(parts[1:])
#                        # Forward this info to student
#                        output_file.writelines(line)
#                    else:
#                        print ('possible gibberish: ', line)
#                        # Forward this info to student
#                        output_file.writelines(line)
#                else:
#                    print_or_hide(line)


def main():
    make_student_view(argv[1], argv[2])

if __name__ == '__main__':
    main()

