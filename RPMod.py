from .. import loader, utils


@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""

    strings = {"name": "RPMod"}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit(
            "<b>• чмок\n• чпок\n• кусь\n• обнять\n• поцеловать\n• шлеп\n• убить\n• выебать\n• связать\n• ударить\n• уебать\n• отсосать\n• отлизать\n• отпиздить\n• задушить\n• украсть"
            "\n• погладить\n• притянуть\n• изнасиловать\n• отпороть</b>"
        )

    async def watcher(self, message):
        status = self.db.get("RPMod", "status")
        reply = await message.get_reply_message()
        try:
            user = await message.client.get_entity(reply.sender_id)
            me = await message.client.get_me()
            if status is not False and message.sender_id == me.id:
                if message.text.lower() == "чмок":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "чпок":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> чпокнул <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "кусь":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнул <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "обнять":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> обнял <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "шлёп":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> шлёпнул <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "убить":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> убил <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "выебать":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> выебал <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "связать":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "ударить":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> ударил <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "уебать":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "отсосать":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал у <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "отлизать":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> отлизал у <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "задушить":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> задушил <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "украсть":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> украл <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "погладить":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "притянуть":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> притянул <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "отпиздить":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> отпиздил <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "изнасиловать":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> изнасиловал <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )
                if message.text.lower() == "отпороть":
                    await message.edit(
                        f"<a href=tg://user?id={me.id}>{me.first_name}</a> отпорол <a href=tg://user?id={user.id}>{user.first_name}</a>"
                    )

        except:
            pass
