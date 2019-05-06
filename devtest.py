import calendar
from datetime import datetime, timedelta


class Solutions(object):

    def greater_than_avg(self, nums):
        return [n for n in nums if n > sum(nums) / len(nums)]

    def sort_fruit(self, fruit):
        return sorted(fruit, key=lambda i: i['count'])

    def reverse_dict(self, d):
        return dict([(value, key) for key, value in d.items()])

    def week_start_end(self, dt):
        start = dt - timedelta(days=dt.weekday())
        start = datetime(start.year, start.month, start.day)
        end = start + timedelta(days=6)
        end = datetime(end.year, end.month, end.day, 23, 59, 59, 999999)
        return (start, end)

    def month_last_day(self, dt):
        return calendar.monthrange(dt.year, dt.month)[1]

    def string_parse(self, text):
        lines = filter(bool, (line.strip() for line in text.splitlines()))
        answers = []
        current_like = ''
        current_dislike = ''
        for index, line in enumerate(lines[3:]):
            if line.startswith('|'):
                vals = [cur.strip() for cur in line.split('|')]
                current_like = '%s %s' % (current_like, vals[1])
                current_dislike = '%s %s' % (current_dislike, vals[2])
                if lines[index + 4].startswith('+'):
                    answers.append(
                        (current_like.strip(), current_dislike.strip()))
                    current_dislike = ''
                    current_like = ''
        return answers

    def palindrome_test_function(self):
        def return_func(test_string=None):
            forward_value = test_string.translate(None, ',.: ')
            return forward_value.lower() == forward_value[::-1].lower()

        return return_func

    def get_dynamic_classes(self, names):
        ret = []
        for name in names:
            current_type = type(name, (), {
                'is_the_one': lambda self: self.__class__.__name__ == 'Neo'
            })
            ret.append(current_type)
        return ret
