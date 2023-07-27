import sys
from functools import partial
from typing import Literal, NoReturn, NewType, Any

COLOR = NewType('COLOR', Literal['white', 'black', 'red', 'green', 'yellow', 'blue', 'purple', 'magenta'])
DECORATOR = NewType('DECORATOR', Literal['none', 'bright', 'underline', 'reverse'])


class CPrint:
    def __init__(self):
        self.cstring = CString()

    def __call__(self, *args,
                 color: COLOR = 'white',
                 decorator: DECORATOR = 'none',
                 sep=' ',
                 end='\n',
                 ) -> NoReturn:
        sys.stdout.write(self.cstring(*args, color=color, decorator=decorator, sep=sep) + end)
        sys.stdout.flush()

    def white(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='white', decorator=decorator, sep=sep)

    def red(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='red', decorator=decorator, sep=sep)

    def black(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='black', decorator=decorator, sep=sep)

    def green(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='green', decorator=decorator, sep=sep)

    def yellow(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='yellow', decorator=decorator, sep=sep)

    def blue(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='blue', decorator=decorator, sep=sep)

    def purple(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='purple', decorator=decorator, sep=sep)

    def magenta(self, *args, decorator: DECORATOR = 'none', sep: str = ' ') -> str:
        return self.__call__(*args, color='magenta', decorator=decorator, sep=sep)


class CString:
    CMAP = {
        'white': '1',
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'purple': '35',
        'magenta': '36',
    }

    DMAP = {
        'none': '0',
        'bright': '1',
        'underline': '4',
        'reverse': '7',
    }

    def __call__(self, *args,
                 color: COLOR = 'white',
                 decorator: DECORATOR = 'none',
                 sep: str = ' ',
                 ) -> str:
        text = sep.join([str(x) for x in args])
        c = self.__class__.CMAP[color]
        d = self.__class__.DMAP[decorator]
        return '\x1b[{d};{c}m{text}\x1b[0m'.format(d=d, c=c, text=text)

    def __getattribute__(self, name: str) -> Any:
        if name in super().__getattribute__('CMAP'):
            return partial(self.__call__, color=name)
        return super().__getattribute__(name)


cprint = CPrint()
cstring = CString()
