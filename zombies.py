from asyncio import sleep
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from . import *

"""
✘ Commands Available
• `{i}zombies`
    Gives the Number of Deleted Accounts.
    
• `{i}zombies clean`
    Remove the deleted accounts if the user is admin.
"""

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================


@ultroid_cmd('zombies ?(.*)')
async def rm_deletedacc(show):
    """ For .zombies command, list all the ghost/deleted/zombie accounts in a chat. """
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No deleted accounts found, Group is clean`"
    if con != "clean":
        eh = await eor(show, "`Searching for ghost/deleted/zombie accounts...`")
        async for user in ultroid_bot.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`Found` {del_u} `ghost/deleted/zombie account(s) in this group,\
            \nClean them by using` `zombies clean`"
        await eh.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # Well
    if not admin and not creator:
        await eor(show, "`I am not an admin here!`")
        return
    ehh = await eor(show, "`Deleting deleted accounts...`")
    del_u = 0from asyncio import sleep
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================


@ultroid_cmd('zombies ?(.*)')
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No deleted accounts found, Group is clean`"
    if con != "clean":
        eh = await eor(show, "`Searching for ghost/deleted/zombie accounts...`")
        async for user in ultroid_bot.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`Found` {del_u} `ghost/deleted/zombie account(s) in this group,\
            \nClean them by using` `zombies clean`"
        await eh.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # Well
    if not admin and not creator:
        await eor(show, "`I am not an admin here!`")
        return
    ehh = await eor(show, "`Deleting deleted accounts...`")
    del_u = 0
    del_a = 0
    async for user in ultroid_bot.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await ultroid_bot(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await eh.edit("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
    del_a = 0
    async for user in ultroid_bot.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await ultroid_bot(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await eh.edit("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await ultroid_bot(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"
    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"
    await ehh.edit(del_status)
    await sleep(2)
    await show.delete()
    
HELP.update({f"{__name__.split('.')[2]}": f"{__doc__.format(i=Var.HNDLR)}"})
