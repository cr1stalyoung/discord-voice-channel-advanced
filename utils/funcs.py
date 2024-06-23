import disnake


class Channel:

    @staticmethod
    async def create_room(interaction, name_channel, category_id, user_limit, button_presses, mode):
        channel_settings = {
            "cod": {
                "game": "Call of Duty",
                "ping": "ID_ROLE_FOR_PING",
                "mode": "cod"
            },
            "arena": {
                "game": "Arena Breakout",
                "ping": "ID_ROLE_FOR_PING",
                "mode": "arena"
            }
        }
        settings = channel_settings[mode]
        category = disnake.utils.get(interaction.guild.categories, id=category_id)
        existing_channel_names = {channel.name for channel in category.channels}
        count = 1
        while True:
            voice_channel_name = f"{name_channel} #{count}"
            if voice_channel_name not in existing_channel_names:
                break
            count += 1

        voice_channel = await interaction.guild.create_voice_channel(
            name=voice_channel_name,
            category=category,
            user_limit=user_limit
        )
        button_presses[voice_channel.id] = {
            "owner": interaction.user.id,
            "id_message": None,
            "game_name": settings['game'],
            "ping": settings['ping'],
            "mode": settings['mode'],
            "value": 0
        }
        await voice_channel.set_permissions(interaction.user, connect=True, mute_members=True, move_members=True, manage_channels=True)
        await interaction.user.move_to(voice_channel)


class Message:

    @staticmethod
    async def create_message(member, after, button_presses, log_channel):
        output = []
        participants = [member.id for member in after.members]
        embed = disnake.Embed(
            title=f"Looking for +{after.user_limit - 1} | {button_presses[after.id]['game_name']}",
            description=f"We're going to play a game, so come join us <@&{button_presses[after.id]['ping']}>",
            color=disnake.Color(int("3fbe54", 16)))
        for i in range(after.user_limit):
            if i < len(after.members):
                output.append("<a:busyslot:1142143554836250664> " + f"<@{participants[i]}><:emoji_109:1142156603710255144>")
            else:
                output.append("<a:freeslot:1142143566634811495> Free slot")
        formatted_output = "\n".join(output)
        embed.add_field(
            name="",
            value=formatted_output,
            inline=False
        )
        mode = button_presses[after.id]['mode']
        file = disnake.File(f'resources/{mode}.png', filename=f'{mode}.png')
        embed.set_image(url=f'attachment://{mode}.png')
        invite = await after.create_invite()
        join = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Join", url=invite.url)
        kick_member = disnake.ui.Button(style=disnake.ButtonStyle.red, custom_id=f"kick:{member.id}:{member.voice.channel.id}", emoji="YOUR_EMJ_OR_ADD_LABEL")
        user_limit = disnake.ui.Button(style=disnake.ButtonStyle.blurple, custom_id=f"limit:{member.id}:{member.voice.channel.id}", emoji="YOUR_EMJ_OR_ADD_LABEL")
        close = disnake.ui.Button(style=disnake.ButtonStyle.gray, custom_id=f"close:{member.id}:{member.voice.channel.id}", emoji="YOUR_EMJ_OR_ADD_LABEL")
        message = await log_channel.send(file=file, embed=embed, components=[join, kick_member, user_limit, close])
        button_presses[after.id]['id_message'] = message.id
        button_presses[after.id]['value'] = 1

    @staticmethod
    async def update_message(after, button_presses, message, value=None):
        output = []
        count = after.user_limit - len(after.members)
        participants = [member.id for member in after.members]
        if value == 1:
            title = f"Room is closed | {button_presses[after.id]['game_name']}"
            description = ""
            color = "ff3737"
        elif len(after.members) < int(after.user_limit):
            title = f"Looking for +{count} | {button_presses[after.id]['game_name']}"
            description = f"We're going to play a game, so come join us <@&{button_presses[after.id]['ping']}>"
            color = "3fbe54"
        else:
            title = f"Playing | {button_presses[after.id]['game_name']}"
            description = ""
            color = "ff3737"
        embed = disnake.Embed(
            title=title,
            description=description,
            color=disnake.Color(int(color, 16)))
        for i in range(after.user_limit):
            if i < len(after.members):
                if participants[i] == button_presses[after.id]['owner']:
                    output.append("<a:busyslot:1142143554836250664> " + f"<@{participants[i]}><:emoji_109:1142156603710255144>")
                else:
                    output.append("<a:busyslot:1142143554836250664> " + f"<@{participants[i]}>")
            else:
                output.append("<a:freeslot:1142143566634811495> Free slot")
        formatted_output = "\n".join(output)
        embed.add_field(
            name="",
            value=formatted_output,
            inline=False
        )
        mode = button_presses[after.id]['mode']
        file = disnake.File(f'resources/{mode}.png', filename=f'{mode}.png')
        embed.set_image(url=f'attachment://{mode}.png')
        await message.edit(file=file, embed=embed)

    @staticmethod
    async def delete_message(before, button_presses, message):
        output = []
        count = before.user_limit - len(before.members)
        participants = [member.id for member in before.members]
        if len(before.members) > 0:
            embed = disnake.Embed(
                title=f"Looking for +{count} | {button_presses[before.id]['game_name']}",
                description=f"We're going to play a game, so come join us <@&{button_presses[before.id]['ping']}>",
                color=disnake.Color(int("3fbe54", 16)))
            for i in range(before.user_limit):
                if i < len(before.members):
                    if participants[i] == button_presses[before.id]['owner']:
                        output.append("<a:busyslot:1142143554836250664> " + f"<@{participants[i]}><:emoji_109:1142156603710255144>")
                    else:
                        output.append("<a:busyslot:1142143554836250664> " + f"<@{participants[i]}>")
                else:
                    output.append("<a:freeslot:1142143566634811495> Free slot")
            formatted_output = "\n".join(output)
            embed.add_field(
                name="",
                value=formatted_output,
                inline=False
            )
            mode = button_presses[before.id]['mode']
            file = disnake.File(f'resources/{mode}.png', filename=f'{mode}.png')
            embed.set_image(url=f'attachment://{mode}.png')
            await message.edit(file=file, embed=embed)
        else:
            button_presses.pop(before.id)
            await message.delete()
