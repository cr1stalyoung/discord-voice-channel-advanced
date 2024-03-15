import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from datetime import datetime, timezone


class Application(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="New name of the room:",
                placeholder="",
                custom_id="name_channel",
                style=TextInputStyle.short,
                max_length=25,
            ),
        ]
        super().__init__(
            title="Lucky Squad",
            custom_id="create_tag_name_channel",
            components=components,
            timeout=120,
        )

    async def callback(self, interaction: disnake.ModalInteraction):
        for key, value in interaction.text_values.items():
            await interaction.author.voice.channel.edit(name=value)
        await interaction.response.defer()
        await interaction.delete_original_message()


class SelectCreateVoice(disnake.ui.StringSelect):
    def __init__(self, bot, button_press, mode, name_channel, category_channel):
        self.bot = bot
        self.button_press = button_press
        self.ButtonVoiceCog = ButtonVoiceCog(bot)
        self.mode = mode
        self.name_channel = name_channel
        self.category_channel = category_channel

        options = [
            disnake.SelectOption(label="Limit to 2", value="2"),
            disnake.SelectOption(label="Limit to 3", value="3"),
            disnake.SelectOption(label="Limit to 4", value="4"),
            disnake.SelectOption(label="Limit to 5", value="5"),
            disnake.SelectOption(label="Limit to 6", value="6"),
        ]
        super().__init__(
            placeholder="Select a limit of participants",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            target_channel_id = 1215688833857888267
            current_voice_channel = interaction.user.voice.channel if interaction.user.voice else None
            if current_voice_channel and current_voice_channel.id == target_channel_id:
                if self.values[0] == "2":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel}", self.category_channel, 2)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "3":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel}", self.category_channel, 3)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "4":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel}", self.category_channel, 4)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "5":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel}", self.category_channel, 5)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "6":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel}", self.category_channel, 6)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
            else:
                embed = disnake.Embed(
                    title="",
                    description="⚠️ First, go to this channel <#1162538136648290475> and try again!",
                    color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            print(f"An error occurred: {e}")


class SelectView(disnake.ui.View):
    def __init__(self, bot, button_press, mode, name_channel, category_channel):
        super().__init__()
        self.add_item(SelectCreateVoice(bot, button_press, mode, name_channel, category_channel))


class SelectCreateVoiceRanked(disnake.ui.StringSelect):
    def __init__(self, bot, button_press, mode, name_channel, category_channel, user_limit):
        self.bot = bot
        self.button_press = button_press
        self.ButtonVoiceCog = ButtonVoiceCog(bot)
        self.mode = mode
        self.name_channel = name_channel
        self.category_channel = category_channel
        self.user_limit = user_limit
        options = [
            disnake.SelectOption(label="Unlimited", value="1", emoji="<:norank:1196192777432727603>"),
            disnake.SelectOption(label="Bronze", value="2", emoji="<:bronze:1196189033668296774>"),
            disnake.SelectOption(label="Silver", value="3", emoji="<:silver:1196189047173959732>"),
            disnake.SelectOption(label="Gold", value="4", emoji="<:gold:1196189076928331898>"),
            disnake.SelectOption(label="Platinum", value="5", emoji="<:plat:1196189089234419752>"),
            disnake.SelectOption(label="Diamond", value="6", emoji="<:diamond:1196189116900061285>"),
            disnake.SelectOption(label="Crimson", value="7", emoji="<:cri:1196189144867668078>"),
            disnake.SelectOption(label="Iridescent", value="8", emoji="<:iridescent:1196189169559556146>"),
        ]
        super().__init__(
            placeholder="Select SR limitation",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            target_channel_id = 1215688833857888267
            current_voice_channel = interaction.user.voice.channel if interaction.user.voice else None
            if current_voice_channel and current_voice_channel.id == target_channel_id:
                if self.values[0] == "1":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Unlimited", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "2":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Bronze", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "3":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Silver", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "4":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Gold", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "5":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Platinum", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "6":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Diamond", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "7":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Crimson", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
                elif self.values[0] == "8":
                    self.button_press[interaction.user.id] = self.mode
                    await self.ButtonVoiceCog.create_room(interaction, f"{self.mode}", f"{self.name_channel} | Iridescent", self.category_channel, self.user_limit)
                    await interaction.response.defer()
                    await interaction.delete_original_message()
            else:
                embed = disnake.Embed(
                    title="",
                    description="⚠️ First, go to this channel <#1162538136648290475> and try again!",
                    color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            print(f"An error occurred: {e}")


class SelectViewRanked(disnake.ui.View):
    def __init__(self, bot, button_press, mode, name_channel, category_channel, user_limit):
        super().__init__()
        self.add_item(SelectCreateVoiceRanked(bot, button_press, mode, name_channel, category_channel, user_limit))


class SelectVoice(disnake.ui.StringSelect):
    def __init__(self, bot, test_collector, channel_data, data_room):
        self.ButtonVoiceCog = ButtonVoiceCog(bot)
        self.test_collector = test_collector
        self.channel_data = channel_data
        self.data_room = data_room
        options = [
            disnake.SelectOption(label="Limit to 2", value="2"),
            disnake.SelectOption(label="Limit to 3", value="3"),
            disnake.SelectOption(label="Limit to 4", value="4"),
            disnake.SelectOption(label="Limit to 5", value="5"),
            disnake.SelectOption(label="Limit to 6", value="6"),
        ]
        super().__init__(
            placeholder="Select a restriction",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            if self.values[0] == "2":
                await interaction.author.voice.channel.edit(user_limit=2)
                await self.ButtonVoiceCog.update_log_message(self.test_collector[interaction.author.voice.channel.id]['member'], self.test_collector[interaction.author.voice.channel.id]['after'], self.channel_data, self.data_room)
                await interaction.response.defer()
                await interaction.delete_original_message()
            elif self.values[0] == "3":
                await interaction.author.voice.channel.edit(user_limit=3)
                await self.ButtonVoiceCog.update_log_message(self.test_collector[interaction.author.voice.channel.id]['member'], self.test_collector[interaction.author.voice.channel.id]['after'], self.channel_data, self.data_room)
                await interaction.response.defer()
                await interaction.delete_original_message()
            elif self.values[0] == "4":
                await interaction.author.voice.channel.edit(user_limit=4)
                await self.ButtonVoiceCog.update_log_message(self.test_collector[interaction.author.voice.channel.id]['member'], self.test_collector[interaction.author.voice.channel.id]['after'], self.channel_data, self.data_room)
                await interaction.response.defer()
                await interaction.delete_original_message()
            elif self.values[0] == "5":
                await interaction.author.voice.channel.edit(user_limit=5)
                await self.ButtonVoiceCog.update_log_message(self.test_collector[interaction.author.voice.channel.id]['member'], self.test_collector[interaction.author.voice.channel.id]['after'], self.channel_data, self.data_room)
                await interaction.response.defer()
                await interaction.delete_original_message()
            elif self.values[0] == "6":
                await interaction.author.voice.channel.edit(user_limit=6)
                await self.ButtonVoiceCog.update_log_message(self.test_collector[interaction.author.voice.channel.id]['member'], self.test_collector[interaction.author.voice.channel.id]['after'], self.channel_data, self.data_room)
                await interaction.response.defer()
                await interaction.delete_original_message()
        except Exception as e:
            print(f"An error occurred: {e}")


class DropDownView(disnake.ui.View):
    def __init__(self, bot, test_collector,channel_data,data_room):
        super().__init__()
        self.add_item(SelectVoice(bot, test_collector, channel_data, data_room))


class KickMember(disnake.ui.StringSelect):
    def __init__(self, author, voice_channel):
        self.author = author
        self.voice_channel = voice_channel
        options = self.generate_options()
        super().__init__(
            placeholder="Kick a player out of the channel",
            min_values=1,
            max_values=1,
            options=options,
        )

    def generate_options(self):
        options = []
        for member in self.voice_channel.members:
            options.append(disnake.SelectOption(label=member.display_name, value=str(member.id), description="Kick", emoji="❌"))
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
                color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
            await interaction.response.send_message(embed=embed, ephemeral=True)


class KickMemberSelect(disnake.ui.View):
    def __init__(self, author, voice_channel):
        super().__init__()
        self.add_item(KickMember(author, voice_channel))


class ButtonVoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.button_presses = {}
        self.channel_data = {}
        self.test_collector = {}
        self.data_room = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print("LFG BOT STARTED")
        id_channel = self.bot.get_channel(1215688804837363833)
        ## Create an embed
        embed = disnake.Embed(
            description="In order to create a room, you initially need to be in this channel <#1215688804837363833>, then click on the appropriate button below to select the mode and room size 👇\n",
            color=disnake.Color(int("0b5e54", 16))
        )

        # Add buttons
        buttons = [
            disnake.ui.Button(style=disnake.ButtonStyle.secondary, label="⠀Create Room⠀", custom_id="warzone_new"),
        ]

        ## Create action rows with specific button arrangement
        action_rows = [
            disnake.ui.ActionRow(buttons[0]),
            *[
                disnake.ui.ActionRow(buttons[i], buttons[i + 1], buttons[i + 2])
                for i in range(8, len(buttons), 3)
            ]
        ]

        # Send the embed with buttons
        #await id_channel.send(embed=embed, components=action_rows)

    @commands.Cog.listener()
    async def on_button_click(self, interaction: disnake.Interaction):
        try:
            if interaction.component.custom_id == "ranked_wz":
                view = SelectViewRanked(self.bot, self.button_presses, "ranked_wz", "WZ", 1173937662592294913, 3)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "ranked_mw":
                view = SelectViewRanked(self.bot, self.button_presses, "ranked_mw", "MW", 1173937699590250646, 4)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "ranked_res":
                view = SelectViewRanked(self.bot, self.button_presses, "ranked_res", "WR", 1202919577047269386, 3)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "warzone_new":
                view = SelectView(self.bot, self.button_presses, "warzone_new", "Room", 1215688756947066940)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "mw3":
                view = SelectView(self.bot, self.button_presses, "mw3", "MW", 1173937755563233361)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "mwz":
                view = SelectView(self.bot, self.button_presses, "mwz", "MWZ", 1173937788408827994)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "resurgence":
                view = SelectView(self.bot, self.button_presses, "resurgence", "Resurgence", 1173937725020323960)
                await interaction.response.send_message(view=view, ephemeral=True)
            elif interaction.component.custom_id == "plunder":
                view = SelectView(self.bot, self.button_presses, "plunder", "Plunder", 1173937817748000809)
                await interaction.response.send_message(view=view, ephemeral=True)
        except:
            pass

        try:
            if interaction.component.custom_id.startswith("kick:"):
                split_limit_voice = int(interaction.component.custom_id.split(":")[2])
                current_voice_channel = interaction.user.voice.channel if interaction.user.voice else None
                if current_voice_channel and current_voice_channel.id == split_limit_voice:
                    split_limit = interaction.component.custom_id.split(":")[1]
                    if int(split_limit) == interaction.user.id:
                        kick_menu = KickMemberSelect(interaction.user, interaction.user.voice.channel)
                        await interaction.response.send_message(view=kick_menu, ephemeral=True)
                    else:
                        embed = disnake.Embed(
                            title="",
                            description="⚠️ Only the creator of the room can change the room's settings!",
                            color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    embed = disnake.Embed(
                        title="",
                        description="⚠️ You can only change room settings in your created channel!",
                        color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            elif interaction.component.custom_id.startswith("limit:"):
                split_limit_voice = int(interaction.component.custom_id.split(":")[2])
                current_voice_channel = interaction.user.voice.channel if interaction.user.voice else None
                if current_voice_channel and current_voice_channel.id == split_limit_voice:
                    split_limit = interaction.component.custom_id.split(":")[1]
                    if int(split_limit) == interaction.user.id:
                        view = DropDownView(self.bot, self.test_collector, self.channel_data, self.data_room)
                        await interaction.response.send_message(view=view, ephemeral=True)
                    else:
                        embed = disnake.Embed(
                            title="",
                            description="⚠️ Only the creator of the room can change the room's settings!",
                            color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    embed = disnake.Embed(
                        title="",
                        description="⚠️ You can only change room settings in your created channel!",
                        color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            elif interaction.component.custom_id.startswith("edit:"):
                split_limit_voice = int(interaction.component.custom_id.split(":")[2])
                current_voice_channel = interaction.user.voice.channel if interaction.user.voice else None
                if current_voice_channel and current_voice_channel.id == split_limit_voice:
                    split_limit = interaction.component.custom_id.split(":")[1]
                    if int(split_limit) == interaction.user.id:
                        await interaction.response.send_modal(modal=Application())
                    else:
                        embed = disnake.Embed(
                            title="",
                            description="⚠️ Only the creator of the room can change the room's settings!",
                            color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    embed = disnake.Embed(
                        title="",
                        description="⚠️ You can only change room settings in your created channel!",
                        color=disnake.Color(int("ff3737", 16)), timestamp=datetime.now(timezone.utc))
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        listCategoryDelete = [
            1215688756947066940,
        ]
        try:
            if before.channel.id == 1215688833857888267:
                mode_list = ["ranked_wz", "ranked_mw", "ranked_res", "warzone_new", "mw3", "mwz", "resurgence", "plunder"]
                if member.id in self.button_presses and self.button_presses[member.id] in mode_list:
                    selected_mode = self.button_presses[member.id]
                    await self.create_message_lfg_voice_voice(member, after.channel, selected_mode)
        except:
            pass

        try:
            if before.channel is not None and after.channel is not None:
                if after.channel.category_id in listCategoryDelete:
                    if member.id in self.button_presses and self.button_presses[member.id] is not None:
                        if member.id in self.button_presses and self.button_presses[member.id] == "ranked_wz":
                            self.button_presses.pop(member.id, "ranked_wz")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "ranked_mw":
                            self.button_presses.pop(member.id, "ranked_mw")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "ranked_res":
                            self.button_presses.pop(member.id, "ranked_res")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "warzone_new":
                            self.button_presses.pop(member.id, "warzone_new")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "mw3":
                            self.button_presses.pop(member.id, "mw3")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "mwz":
                            self.button_presses.pop(member.id, "mwz")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "resurgence":
                            self.button_presses.pop(member.id, "resurgence")
                        elif member.id in self.button_presses and self.button_presses[member.id] == "plunder":
                            self.button_presses.pop(member.id, "plunder")
                    else:
                        await self.update_log_message(member, after.channel, self.channel_data, self.data_room)

            if before.channel is None and after.channel is not None:
                if after.channel.category_id in listCategoryDelete:
                    await self.update_log_message(member, after.channel, self.channel_data, self.data_room)

            if before.channel is not None and after.channel is None:
                await self.delete_log_message(before.channel)

            if before.channel != after.channel and after.channel is not None:
                await self.delete_log_message(before.channel)
        except:
            pass

        try:
            if before.channel.members == [] and before.channel.id != 1215688833857888267:
                if before.channel.category_id in listCategoryDelete:
                    await before.channel.delete()
        except:
            pass

    async def check_rank_wz(self, user_id):
        rank_id_role = {
            1142188376359981056: "<:bronze:1196189033668296774>",
            1142188344550375444: "<:silver:1196189047173959732>",
            1142188319728488608: "<:gold:1196189076928331898>",
            1142188272555130890: "<:plat:1196189089234419752>",
            1142188207409213491: "<:diamond:1196189116900061285>",
            1142188098755768451: "<:cri:1196189144867668078>",
            1142188149334884452: "<:iridescent:1196189169559556146>",
            1184451720508625039: "<:top250:1196202026212806726>"
        }
        guild = self.bot.get_guild(1060006588510896168)
        member = guild.get_member(user_id)
        user_roles = [role.id for role in member.roles]
        for role_id in user_roles:
            if role_id in rank_id_role:
                return rank_id_role[role_id]
        return "<:norank:1196192777432727603>"

    async def check_rank_mw(self, user_id):
        rank_id_role = {
            1196188101421301881: "<:bronze:1196189033668296774>",
            1196187987994738698: "<:silver:1196189047173959732>",
            1196187923440222249: "<:gold:1196189076928331898>",
            1196187853412106321: "<:plat:1196189089234419752>",
            1196187485819109426: "<:diamond:1196189116900061285>",
            1196187431892955216: "<:cri:1196189144867668078>",
            1196187346803101766: "<:iridescent:1196189169559556146>",
            1196187248379559956: "<:top250:1196202026212806726>"
        }
        guild = self.bot.get_guild(1060006588510896168)
        member = guild.get_member(user_id)
        user_roles = [role.id for role in member.roles]
        for role_id in user_roles:
            if role_id in rank_id_role:
                return rank_id_role[role_id]
        return "<:norank:1196192777432727603>"

    # create room with help buttons
    async def create_room(self, interaction, name_button, name_channel, category_id, user_limit):
        self.button_presses[interaction.user.id] = name_button
        CategoryCreateNewChannel = disnake.utils.get(interaction.guild.categories, id=category_id)
        existing_channel_names = [channel.name for channel in CategoryCreateNewChannel.voice_channels]
        count = 1
        voice_channel_name = f"{name_channel} #{count}"
        while voice_channel_name in existing_channel_names:
            count += 1
            voice_channel_name = f"{name_channel} #{count}"
        voice = await interaction.guild.create_voice_channel(name=voice_channel_name, category=CategoryCreateNewChannel, user_limit=user_limit)
        await voice.set_permissions(interaction.user, connect=True, mute_members=True, move_members=True, manage_channels=True)
        await interaction.user.move_to(voice)

    # create message lfg voice channel
    async def create_message_lfg_voice_voice(self, member, after, selected_mode):
        output = []
        self.test_collector[after.id] = {"member": member, "after": after}
        self.data_room[after.id] = {"id_owner": member.id, "mode_list": selected_mode}
        log_channel = self.bot.get_channel(1216694791799308288)
        participants = [member.id for member in after.members]
        embed = disnake.Embed(
            title=f"Searching for +{after.user_limit - 1} | {member.voice.channel.name}",
            description="",
            color=disnake.Color(int("37ff6c", 16)))
        for i in range(after.user_limit):
            if i < len(after.members):
                #rank_wz = await self.check_rank_wz(participants[i])
                #rank_mw = await self.check_rank_mw(participants[i])
                output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}><:crown:1216712042199912458>")
            else:
                output.append("<a:green:1212720539311808522> Free place.")
        formatted_output = "\n".join(output)
        embed.add_field(
            name="",
            value=formatted_output,
            inline=False
        )
        file_path = f'room.png'
        file_path_gif = '2.gif'
        file = disnake.File(file_path, filename=f'room.png')
        file_gif = disnake.File(file_path_gif, filename='2.gif')
        embed.set_thumbnail(url=f'attachment://room.png')
        embed.set_image(url=f'attachment://2.gif')
        invite = await after.create_invite()
        join = disnake.ui.Button(style=disnake.ButtonStyle.gray, label=f"Join", url=invite.url)
        kick_member = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Kick", custom_id=f"kick:{member.id}:{member.voice.channel.id}")
        user_limit = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="", custom_id=f"limit:{member.id}:{member.voice.channel.id}", emoji="<:limit:1186380908719263805>")
        edit_name_channel = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="", custom_id=f"edit:{member.id}:{member.voice.channel.id}", emoji="<:edit_channel:1186380951845081149>")
        message = await log_channel.send(files=[file, file_gif], embed=embed, components=[join, kick_member, user_limit, edit_name_channel])
        self.channel_data[after.id] = message.id

    # update lfg message
    async def update_log_message(self, member, after, channel_data, data_room):
        output = []
        log_channel = self.bot.get_channel(1216694791799308288)
        if log_channel and after.id in channel_data:
            message_id = channel_data[after.id]
            message = await log_channel.fetch_message(message_id)
            count = after.user_limit - len(after.members)
            participants = [member.id for member in after.members]
            name_img = data_room[after.id]['mode_list']
            if len(after.members) < int(after.user_limit):
                embed = disnake.Embed(
                    title=f"Searching for +{after.user_limit - 1} | {member.voice.channel.name}",
                    description="",
                    color=disnake.Color(int("37ff6c", 16)))
                for i in range(after.user_limit):
                    if i < len(after.members):
                        if participants[i] == data_room[after.id]['id_owner']:
                            print(participants[i])
                            output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}><:crown:1216712042199912458>")
                        else:
                            print(participants[i])
                            output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}>")
                    else:
                        output.append("<a:green:1212720539311808522> Free place")
                formatted_output = "\n".join(output)
                embed.add_field(
                    name="",
                    value=formatted_output,
                    inline=False
                )
                file_path = f'room.png'
                file_path_gif = '2.gif'
                file = disnake.File(file_path, filename=f'room.png')
                file_gif = disnake.File(file_path_gif, filename='2.gif')
                embed.set_thumbnail(url=f'attachment://room.png')
                embed.set_image(url=f'attachment://2.gif')
                await message.edit(files=[file, file_gif], embed=embed)
            else:
                embed = disnake.Embed(
                    title=f"Busy | {member.voice.channel.name}",
                    description="",
                    color=disnake.Color(int("ff3737", 16)))
                for i in range(after.user_limit):
                    if participants[i] == data_room[after.id]['id_owner']:
                        print(participants[i])
                        output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}><:crown:1216712042199912458>")
                    else:
                        print(participants[i])
                        output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}>")
                formatted_output = "\n".join(output)
                embed.add_field(
                    name="",
                    value=formatted_output,
                    inline=False
                )
                file_path = f'room.png'
                file_path_gif = '4.gif'
                file = disnake.File(file_path, filename=f'room.png')
                file_gif = disnake.File(file_path_gif, filename='4.gif')
                embed.set_thumbnail(url=f'attachment://room.png')
                embed.set_image(url=f'attachment://4.gif')
                await message.edit(files=[file, file_gif], embed=embed)

    # delete message lfg voice channel
    async def delete_log_message(self, before):
        output = []
        log_channel = self.bot.get_channel(1216694791799308288)
        if log_channel and before.id in self.channel_data:
            message_id = self.channel_data[before.id]
            try:
                message = await log_channel.fetch_message(message_id)
            except disnake.NotFound:
                return
            count = before.user_limit - len(before.members)
            participants = [member.id for member in before.members]
            if len(before.members) > 0:
                name_img = self.data_room[before.id]['mode_list']
                embed = disnake.Embed(title=f"Searching for +{count} | {before.name}", description="", color=disnake.Color(int("37ff6c", 16)))
                for i in range(before.user_limit):
                    if i < len(before.members):
                        rank_wz = await self.check_rank_wz(participants[i])
                        rank_mw = await self.check_rank_mw(participants[i])
                        if participants[i] == self.data_room[before.id]['id_owner']:
                            output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}>")
                        else:
                            output.append("<a:red:1212720526909505606> " + f"<@{participants[i]}>")
                    else:
                        output.append("<a:green:1212720539311808522> Free Place")
                formatted_output = "\n".join(output)
                embed.add_field(
                    name="",
                    value=formatted_output,
                    inline=False
                )
                file_path = f'{name_img}.png'
                file_path_gif = '2.gif'
                file = disnake.File(file_path, filename=f'{name_img}.png')
                file_gif = disnake.File(file_path_gif, filename='2.gif')
                embed.set_thumbnail(url=f'attachment://{name_img}.png')
                embed.set_image(url=f'attachment://2.gif')
                await message.edit(files=[file, file_gif], embed=embed)
            else:
                await message.delete()
                self.channel_data.pop(before.id, message.id)


def setup(bot):
    bot.add_cog(ButtonVoiceCog(bot))
