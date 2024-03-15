## CREATE VOICE CHANNEL | DISCORD BOT

Description:
A new version of creating voice channels with a button. This version implements sending a message to the channel to manage the channel, namely change the limit of participants, kick out, change the name of the room.

For creating, editing and deleting the message is responsible for the function:
1) create_message_lfg_voice_voice.
2) update_log_message
3) delete_log_message

The data is stored locally and can be changed as needed.
Function to create a room **create_room**, where 4 variables are accepted, namely name_button, name_channel, category_id, user_limit. The logic of creating a room message itself: first, the on_voice_state_update function checks if the id of the participant is in the collection, and then it checks if the name of the buttons is included in the mode_list, if so, then the create_message_lfg_voice_voice function is called.
