import asyncio


def view_debug(time=100, before='', after=''):
    print('-' * 15)
    for variable, value in locals().items():
        print(variable, '=', value)


async def view_debug_async(time=100, before: str = '',
                           after: str = '', message: list = None, event: list = None):
    print('-' * 15)
    for variable, value in locals().items():
        print(variable, '=', value)
    for attribute, value in event.__dict__.items():
        print(attribute, '=', value)
    print('-' * 25)

    for attribute, value in message.__dict__.items():
        print(attribute, '=', value)
    await asyncio.sleep(time)


# await view_debug()

view_debug(before='list')
