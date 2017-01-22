class FileView:
    def __init__(self, text_file=None):
        # [{text:"code", hidden:false, question=None/"name"}]
        self.line_datas = []
        self.question_datas = []
        if text_file:
            self.read(text_file)

    def read(self, text_file):
        state = 'copy'
        question_data = {}

        for line_number, line in enumerate(text_file):
            line_data = {
                'text': line,
            }

            # Drop the last character from the line
            line = line[:-1]

            if state == 'hide':
                line_data['mode'] = 'hide'
            elif state == 'question':
                line_data['mode'] = 'blank'
            else:
                line_data['mode'] = 'copy'

            # Now parsing the line itself
            if line[0:2] == '@@':
                # Filters is for any empty strings after the split
                parts = list(filter(None, line[2:].split(' ')))
                line_data['macro'] = True
                if parts[0] == 'begin':
                    if state != 'copy':
                        raise ValueError('Embeded macro found at line {}.'
                                         .format(line_number + 1))
                    elif parts[1] in ['hide', 'entry']:
                        state = 'hide'
                        line_data['mode'] = 'hide'
                    elif parts[1] == 'question':
                        state = 'question'
                        line_data['question'] = True
                        question_data['name'] = ' '.join(parts[2:])
                        question_data['line'] = line_number
                    else:
                        raise ValueError('Unknown macro on line ' +
                                         str(line_number + 1) + ' file '+text_file.name)

                elif parts[0] == 'end':
                    if state == 'copy':
                        raise ValueError('Macro end without start at line {}.'
                                         .format(line_number + 1))
                    elif parts[1] in ['hide', 'entry']:
                        state = 'copy'
                    elif parts[1] == 'question':
                        state = 'copy'
                        line_data['mode'] = 'copy'
                        self.question_datas.append(question_data)
                        question_data = {}
                    else:
                        raise ValueError('Unknown macro on line ' +
                                         str(line_number + 1))
                elif parts[0][-1] == ':':
                    if state != 'question':
                        raise ValueError('Property macro without question' +
                                         ' on line ' + str(line_number + 1))
                    line_data['mode'] = 'copy'
                    if parts[0][:-1] == "description":
                        question_data['description'] = ' '.join(parts[1:])
                    if parts[0][:-1] == "points":
                        question_data['points'] = ' '.join(parts[1:])
                    if parts[0][:-1] == "time":
                        question_data['time'] = ' '.join(parts[1:])
                else:
                    raise ValueError("Invalid macro found at line {}: {}"
                                     .format(line_number + 1, line))

            self.line_datas.append(line_data)

    def get_student_view(self):
        for line_data in self.line_datas:

            if line_data['mode'] == 'copy':
                yield line_data['text']
            elif line_data['mode'] == 'blank':
                yield '\n'


def get_student_view_json(input_file_name):
    student_str = ""
    with open(input_file_name) as input_file:
        fv = FileView(input_file)
        for line in fv.get_student_view():
            student_str += line
    return student_str
