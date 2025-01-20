import json
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, MessageHandler, CallbackContext, filters
from telegram.error import TimedOut

# Load movie data from data.json
with open("data.json", "r") as file:
    movies = json.load(file)

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.strip().lower()
    
    # Find the movie in the database
    for movie_name, details in movies.items():
        if user_message in movie_name.lower():  # Check if user input is a substring of the movie name
            link = details["link"]
            downloadlink = details["downloadlink"]
            image = details["image"]

            # Create buttons for "Watch Now" and "Download"
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="🎥 Watch Now", url=link)],
                [InlineKeyboardButton(text="⬇️ Download", url=downloadlink)]
            ])
            
            # Create the caption with proper Markdown formatting
            caption = f"""
*{details['name']}* 

‹⟬ Join channel : [Click here](https://t.me/flemovies) ⟭›

--------------------------------------------------------
"""
            
            # Send the movie image with the buttons
            await update.message.reply_photo(
                photo=image,
                caption=caption,
                parse_mode="Markdown",
                reply_markup=buttons
            )
            return
    
    # If no match is found
    await update.message.reply_text(
        "Sorry, I couldn't find that movie. Please try another."
    )

# Main function to set up the bot
def main():
    # Replace with your API token
    # TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    # Create the Application
    application = Application.builder().token(TOKEN).build()

    try:
        # Add a message handler
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Start the bot with an increased timeout
        application.run_polling(timeout=60)  # Increase timeout to 60 seconds or as needed

    except TimedOut:
        print("The request timed out. Please try again.")

if __name__ == "__main__":
    main()
