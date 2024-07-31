from telethon import events
from forwardbot import bot
from forwardbot.BotConfig import Config

bothandler = Config.COMMAND_HAND_LER

def forwardbot_cmd(add_cmd, is_args=False):
    def cmd(func):
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        else:
            pattern = bothandler + add_cmd + "$"
        bot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )
    return cmd

async def is_sudo(event):
    return str(event.sender_id) in Config.SUDO_USERS

def start_forwardbot(shortname):
    import importlib
    import sys
    from pathlib import Path

    if shortname.startswith("__"):
        # Skip special module names
        return

    # Load the module dynamically
    path = Path(f"forwardbot/plugins/{shortname}.py")
    name = f"forwardbot.plugins.{shortname}"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Setup the module
    if hasattr(mod, 'forwardbot_cmd'):
        mod.forwardbot_cmd = forwardbot_cmd
    if hasattr(mod, 'forwardbot'):
        mod.forwardbot = bot
    if hasattr(mod, 'Config'):
        mod.Config = Config

    # Register the module in sys.modules
    sys.modules[f"forwardbot.plugins.{shortname}"] = mod
    print(f"IMPORTED {shortname}")
