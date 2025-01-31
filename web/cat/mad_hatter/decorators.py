# We use the @tool decorator directly from langchain, 'as is'.
# The plugin system imports it from here (cat.decorators module), as it will be possible to extend it later on

from langchain.agents import tool

from cat.utils import log


log(tool)


def hook(func):
    def cat_hook_wrapper(*args, **kwargs):
        # log(func)
        return func(*args, **kwargs)

    return cat_hook_wrapper
