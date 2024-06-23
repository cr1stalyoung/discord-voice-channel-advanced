from utils import views
from utils import funcs
import settings
import disnake
from disnake.ext import commands


class Channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.view = views
        self.func = funcs
        self.button_presses = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print("The create_room.py file has started working")
        # ## Create an embed
        # embed = disnake.Embed(
        #     description="To create a room first go to this channel <#YOUR_ID_VOICE_CHANNEL> then click the corresponding button below to choose the mode and room size 👇",
        #     color=disnake.Color(int("0b5e54", 16))
        # )
        #
        # # Add buttons
        # buttons = [
        #     disnake.ui.Button(style=disnake.ButtonStyle.danger, label="Call of Duty", custom_id="cod", emoji="YOUR_EMJ_IF_NEED"),
        #     disnake.ui.Button(style=disnake.ButtonStyle.secondary, label="Arena Breakout", custom_id="arena", emoji="YOUR_EMJ_IF_NEED"),
        # ]
        #
        # # Send the embed with buttons
        # await self.bot.get_channel(YOUR_ID_TEXT_CHANNEL).send(embed=embed, components=buttons)

    @commands.Cog.listener()
    async def on_button_click(self, interaction: disnake.MessageInteraction):
        if interaction.component.custom_id == "cod":
            view = self.view.ViewCallOfDuty(settings.CATEGORY_COD, settings.CHANNEL_JUMP, self.button_presses)
            await interaction.response.send_message(view=view, ephemeral=True)
        elif interaction.component.custom_id == "arena":
            view = self.view.ViewArenaBreakOut(settings.CATEGORY_ARENA, settings.CHANNEL_JUMP, self.button_presses)
            await interaction.response.send_message(view=view, ephemeral=True)
        elif interaction.component.custom_id.startswith("kick:"):
            if interaction.user.voice is not None and interaction.user.voice.channel.id == int(interaction.component.custom_id.split(":")[2]):
                if int(interaction.component.custom_id.split(":")[1]) == interaction.user.id:
                    await interaction.response.send_message(view=self.view.ViewKickMember(interaction.user, interaction.user.voice.channel), ephemeral=True)
                else:
                    embed = disnake.Embed(description="⚠️ Only the creator of the room can change the room's settings!", color=disnake.Color(int("ff3737", 16)))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = disnake.Embed(description="⚠️ You can only change room settings in your created channel!", color=disnake.Color(int("ff3737", 16)))
                await interaction.response.send_message(embed=embed, ephemeral=True)
        elif interaction.component.custom_id.startswith("limit:"):
            if interaction.user.voice is not None and interaction.user.voice.channel.id == int(interaction.component.custom_id.split(":")[2]):
                if int(interaction.component.custom_id.split(":")[1]) == interaction.user.id:
                    message = await self.bot.get_channel(settings.CHANNEL_ACTIVE).fetch_message(self.button_presses[interaction.user.voice.channel.id]['id_message'])
                    if message:
                        await interaction.response.send_message(view=self.view.ViewChangeLimit(interaction.user.voice.channel, self.button_presses, message), ephemeral=True)
                else:
                    embed = disnake.Embed(description="⚠️ Only the creator of the room can change the room's settings!", color=disnake.Color(int("ff3737", 16)))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = disnake.Embed(description="⚠️ You can only change room settings in your created channel!", color=disnake.Color(int("ff3737", 16)))
                await interaction.response.send_message(embed=embed, ephemeral=True)
        elif interaction.component.custom_id.startswith("close:"):
            if interaction.user.voice is not None and interaction.user.voice.channel.id == int(interaction.component.custom_id.split(":")[2]):
                if int(interaction.component.custom_id.split(":")[1]) == interaction.user.id:
                    channel = interaction.author.voice.channel
                    everyone_role = interaction.guild.default_role
                    if channel.overwrites_for(everyone_role).connect is None or channel.overwrites_for(everyone_role).connect:
                        new_permission = False
                        embed = f'Channel {channel.name} is closed to new connections.'
                        value = 1
                    else:
                        new_permission = True
                        embed = f'Channel {channel.name} is open for new connections.'
                        value = None
                    await channel.set_permissions(everyone_role, overwrite=disnake.PermissionOverwrite(connect=new_permission))
                    embed = disnake.Embed(description=embed, color=disnake.Color(int("ff3737", 16)))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    message = await self.bot.get_channel(settings.CHANNEL_ACTIVE).fetch_message(self.button_presses[interaction.user.voice.channel.id]['id_message'])
                    if message:
                        await self.func.Message.update_message(interaction.user.voice.channel, self.button_presses, message, value)
                else:
                    embed = disnake.Embed(description="⚠️ Only the creator of the room can change the room's settings!", color=disnake.Color(int("ff3737", 16)))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = disnake.Embed(description="⚠️ You can only change room settings in your created channel!", color=disnake.Color(int("ff3737", 16)))
                await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        category = [YOUR_ID_CATEGORIES]
        log_channel = self.bot.get_channel(settings.CHANNEL_ACTIVE)

        if after.channel and after.channel.id in self.button_presses:
            if self.button_presses[after.channel.id]['value'] == 0:
                await self.func.Message.create_message(member, after.channel, self.button_presses, log_channel)
            else:
                message = await log_channel.fetch_message(self.button_presses[after.channel.id]['id_message'])
                if message:
                    await self.func.Message.update_message(after.channel, self.button_presses, message)

        if before.channel and before.channel.category_id in category:
            if before.channel.id in self.button_presses:
                message = await log_channel.fetch_message(self.button_presses[before.channel.id]['id_message'])
                if message:
                    await self.func.Message.delete_message(before.channel, self.button_presses, message)
                    if before.channel.members == [] and before.channel.id != settings.CHANNEL_JUMP:
                        await before.channel.delete()
            else:
                if before.channel.members == [] and before.channel.id != settings.CHANNEL_JUMP:
                    await before.channel.delete()


def setup(bot):
    bot.add_cog(Channel(bot))

