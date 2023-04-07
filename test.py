from pyrogram import Client, filters

bot = Client(
    "forward_bot",
    api_id="2933218",
    api_hash="d407e766a395ca20b20bd0cff4aeb825")

# Define the channel IDs
SOURCE_CHANNEL_ID = -1001798429761
DESTINATION_CHANNEL_ID = -1001412620548

# Define the message counter and threshold
message_counter = 0
message_threshold = 4


# Define a function to forward a message to the destination channel
def forward_message(message):
    try:
        bot.send_message(DESTINATION_CHANNEL_ID, message)

    except Exception:
        pass


# Define a message handler function that filters messages from the source channel
@bot.on_message(filters.chat(SOURCE_CHANNEL_ID))
def handle_message(client, message):
    try:
        global message_counter

        # Increment the message counter
        message_counter += 1

        # If the message threshold is reached, forward the last message to the destination channel
        if message_counter == message_threshold:
            # Forward the last message to the destination channel
            forward_message(message.text)

            # Reset the message counter
            message_counter = 0

    except Exception:
        pass

# Start the Pyrogram client
print("I'm Alive")
bot.run()
