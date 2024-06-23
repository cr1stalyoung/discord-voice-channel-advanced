from utils import funcs
import disnake


# ---------------------------------------------------------------------------------------------------------------------------
# Call of Duty
class SelectCOD(disnake.ui.StringSelect):
    def __init__(self, category_channel, channel_jump, button_presses):
        self.category_channel = category_channel
        self.channel_jump = channel_jump
        self.button_presses = button_presses
        self.func = funcs

        options = [
            disnake.SelectOption(label="Limit to 2", value="0"),
            disnake.SelectOption(label="Limit to 3", value="1"),
            disnake.SelectOption(label="Limit to 4", value="2"),
            disnake.SelectOption(label="Limit to 5", value="3"),
            disnake.SelectOption(label="Limit to 6", value="4")
        ]
        super().__init__(
            placeholder="Select a limit of members",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            if interaction.user.voice.channel.id == self.channel_jump:
                if self.values[0] == "0":
                    await self.func.Channel.create_room(interaction, "Duo", self.category_channel, 2, self.button_presses, "cod")
                elif self.values[0] == "1":
                    await self.func.Channel.create_room(interaction, "Trios", self.category_channel, 3, self.button_presses, "cod")
                elif self.values[0] == "2":
                    await self.func.Channel.create_room(interaction, "Squad", self.category_channel, 4, self.button_presses, "cod")
                elif self.values[0] == "3":
                    await self.func.Channel.create_room(interaction, "Multiplayer", self.category_channel, 5, self.button_presses, "cod")
                elif self.values[0] == "4":
                    await self.func.Channel.create_room(interaction, "Multiplayer", self.category_channel, 6, self.button_presses, "cod")
                await interaction.response.defer()
                await interaction.delete_original_message()
            else:
                embed = disnake.Embed(description=f"⚠️ First go to this channel <#{self.channel_jump}> and try again!", color=disnake.Color(int("ff3737", 16)))
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            print(f"An error occurred: {e}")


class ViewCallOfDuty(disnake.ui.View):
    def __init__(self, category_channel, channel_jump, button_presses):
        super().__init__(timeout=60)
        self.add_item(SelectCOD(category_channel, channel_jump, button_presses))
# ---------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------
# Arena Breakout
class SelectArenaBreakOut(disnake.ui.StringSelect):
    def __init__(self, category_channel, channel_jump, button_presses):
        self.category_channel = category_channel
        self.channel_jump = channel_jump
        self.button_presses = button_presses
        self.func = funcs

        options = [
            disnake.SelectOption(label="Limit to 2", value="0"),
            disnake.SelectOption(label="Limit to 3", value="1"),
            disnake.SelectOption(label="Limit to 4", value="2")
        ]
        super().__init__(
            placeholder="Select a limit of members",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            if interaction.user.voice.channel.id == self.channel_jump:
                if self.values[0] == "0":
                    await self.func.Channel.create_room(interaction, "Duo", self.category_channel, 2, self.button_presses, "arena")
                elif self.values[0] == "1":
                    await self.func.Channel.create_room(interaction, "Trios", self.category_channel, 3, self.button_presses, "arena")
                elif self.values[0] == "2":
                    await self.func.Channel.create_room(interaction, "Squad", self.category_channel, 4, self.button_presses, "arena")
                await interaction.response.defer()
                await interaction.delete_original_message()
            else:
                embed = disnake.Embed(description=f"⚠️ First go to this channel <#{self.channel_jump}> and try again!", color=disnake.Color(int("ff3737", 16)))
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            print(f"An error occurred: {e}")


class ViewArenaBreakOut(disnake.ui.View):
    def __init__(self, category_channel, channel_jump, button_presses):
        super().__init__(timeout=60)
        self.add_item(SelectArenaBreakOut(category_channel, channel_jump, button_presses))
# ---------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------
# Kick of player
class KickMember(disnake.ui.StringSelect):
    def __init__(self, author, voice_channel):
        self.author = author
        self.voice_channel = voice_channel
        options = self.generate_options()
        super().__init__(
            placeholder="Kick member out",
            min_values=1,
            max_values=1,
            options=options,
        )

    def generate_options(self):
        options = []
        for member in self.voice_channel.members:
            options.append(disnake.SelectOption(label=member.display_name, value=str(member.id), description="Kick member out of room", emoji="ADD_EMJ_IF_NEED"))
        return options

    async def callback(self, interaction: disnake.MessageInteraction):
        selected_member_id = int(self.values[0])
        selected_member = self.voice_channel.guild.get_member(selected_member_id)
        if selected_member:
            await selected_member.move_to(None)
            await interaction.response.defer()
            await interaction.delete_original_message()
        else:
            embed = disnake.Embed(
                title="",
                description="⚠️ Selected member not found!",
                color=disnake.Color(int("ff3737", 16)))
            await interaction.response.send_message(embed=embed, ephemeral=True)


class ViewKickMember(disnake.ui.View):
    def __init__(self, author, voice_channel):
        super().__init__(timeout=60)
        self.add_item(KickMember(author, voice_channel))
# ---------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------
# Change Limit
class ChangeLimit(disnake.ui.StringSelect):
    def __init__(self, channel, button_presses, log_channel):
        self.channel = channel
        self.button_presses = button_presses
        self.log_channel = log_channel
        self.func = funcs
        options = [
            disnake.SelectOption(label="Limit to 2", value="0"),
            disnake.SelectOption(label="Limit to 3", value="1"),
            disnake.SelectOption(label="Limit to 4", value="2"),
            disnake.SelectOption(label="Limit to 5", value="3"),
            disnake.SelectOption(label="Limit to 6", value="4"),
            disnake.SelectOption(label="Limit to 10", value="5")
        ]
        super().__init__(
            placeholder="Select a limit of members",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            if self.values[0] == "9":
                await interaction.author.voice.channel.edit(user_limit=2)
            elif self.values[0] == "1":
                await interaction.author.voice.channel.edit(user_limit=3)
            elif self.values[0] == "2":
                await interaction.author.voice.channel.edit(user_limit=4)
            elif self.values[0] == "3":
                await interaction.author.voice.channel.edit(user_limit=5)
            elif self.values[0] == "4":
                await interaction.author.voice.channel.edit(user_limit=6)
            elif self.values[0] == "5":
                await interaction.author.voice.channel.edit(user_limit=10)
            await self.func.Message.update_message(self.channel, self.button_presses, self.log_channel)
            await interaction.response.defer()
            await interaction.delete_original_message()
        except Exception as e:
            print(f"An error occurred: {e}")


class ViewChangeLimit(disnake.ui.View):
    def __init__(self, channel, button_presses, log_channel):
        super().__init__(timeout=60)
        self.add_item(ChangeLimit(channel, button_presses, log_channel))

