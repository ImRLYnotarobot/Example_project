from time import perf_counter as timer
from django.db import connection, reset_queries


class SimpleMiddleware:
    '''
    Adds response generating time and sql hits count before
    </body> tag
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response_init_time = timer()
        reset_queries()

        response = self.get_response(request)

        if response.status_code == 200:
            response_time = timer() - response_init_time
            p_response_time = self.pretty_time(response_time)
            hit_count = len(connection.queries)

            message = bytes(
                self.make_message(p_response_time, hit_count),
                encoding='utf-8'
            )

            buffer = response.content
            body_close_tag_pos = buffer.find(b'</body>')
            response.content = buffer[:body_close_tag_pos] + \
                message + \
                buffer[body_close_tag_pos:]
        return response

    @staticmethod
    def make_message(time_str, hit_count):
        tag = 'h3'

        message = '''<{0}>Execution time: {1}</{0}>
        <{0}>Database hits per request: {2}</{0}>'''.format(
            tag,
            time_str,
            hit_count
        )
        return message

    @staticmethod
    def pretty_time(secs):
        '''takes float (timedelta in seconds) and makes good looking string'''
        if secs < 1:
            nanos = secs * 1e9

            if nanos > 1e6:
                format_time = nanos / 1e6
                si_code = 'm'

            elif nanos > 1e3:
                format_time = nanos / 1e3
                si_code = '\u03BC'       # microseconds (greek small letter mu)

            else:
                format_time = nanos
                si_code = 'n'

        else:
            format_time = secs
            si_code = ''

        return '{:.3f} {}s'.format(format_time, si_code)
