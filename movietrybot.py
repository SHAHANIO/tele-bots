from telegram import Update, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, MessageHandler, CallbackContext, filters
from telegram.error import TimedOut

# Your movie data with keywords and image URLs
movies = {
    "marco malayalam 2024": {
        "name": "Marco Malayalam 2024",
        "link": "https://pay4fans.com/videoShare?surl=ZS8solcRA_YV9MkDc7T7jQ",
        "downloadlink": "https://1024terabox.com/s/1y2BZ_9T9Lf_uwTJazMhyvA",
        "image": "https://english.mathrubhumi.com/image/contentid/policy:1.9643492:1718529294/448350774_17966544149743589_6992687319211761609_n.jpg?$p=d121241&f=4x3&w=1080&q=0.8"  # Replace with a valid image URL
    },
    "lucifer malayalam 2019": {
        "name": "Lucifer Malayalam 2019",
        "link": "https://pay4fans.com/videoShare?surl=ZS8solcRA_YV9MkDc7T7jQ",
        "downloadlink": "https://1024terabox.com/s/1y2BZ_9T9Lf_uwTJazMhyvA",
        "image": "https://images.indianexpress.com/2018/12/lucifer-759.jpg"  # Replace with a valid image URL
    },
}

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
    TOKEN = "7529277779:AAELpV2jYZfCemCNEb4DLySjjK47r_qHhUg"

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
