import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import database
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
from dotenv import load_dotenv

# --- Setup ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the /start command is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I'm your personal time tracker.",
    )
    await update.message.reply_text(
        "To use me, send:\n"
        "/begin <activity_name> - to start a new activity\n"
        "/stop - to stop the current activity"
    )

async def begin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Starts tracking a new activity."""
    user_id = update.effective_user.id
    activity_name = " ".join(context.args)

    if not activity_name:
        await update.message.reply_text("Please provide an activity name. Usage: /begin <activity name>")
        return 


    if context.user_data.get('current_activity_id'):
        await stop(update, context)

    activity_id = database.start_activity(user_id, activity_name)

    context.user_data["current_activity_id"] = activity_id

    context.user_data["current_activity_name"] = activity_name

    await update.message.reply_text(f"Starting activity: {activity_name}")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Stops the current activity."""
    activity_id = context.user_data.get('current_activity_id')

    if not activity_id:
        await update.message.reply_text("No activity is currently running.")
        return


    duration_minutes = database.stop_activity(activity_id)
    activity_name = context.user_data.get('current_activity_name')


    await update.message.reply_text(
        f"Stopped activity: {activity_name}. Duration: {duration_minutes} minutes."
    )

    context.user_data.clear()




async def report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generates and sends a report of activities."""
    user_id = update.effective_user.id
    period = 'today' # Default period
    if context.args:
        period = context.args[0].lower()

    if period not in ['today', 'week']:
        await update.message.reply_text("Invalid period. Please use 'today' or 'week'.")
        return

    df = database.get_activities(user_id, period)

    if df.empty:
        await update.message.reply_text(f"No completed activities found for {period}.")
        return

    # --- Generate Text Summary ---
    summary = df.groupby('activity_name')['duration_minutes'].sum().reset_index()
    summary_text = f"Time spent ({period}):\n\n"
    for _, row in summary.iterrows():
        summary_text += f"- *{row['activity_name']}*: {row['duration_minutes']} minutes\n"

    await update.message.reply_text(summary_text, parse_mode='Markdown')

    # --- Generate and Send Pie Chart ---
    plt.style.use('ggplot')
    plt.figure(figsize=(8, 8))
    plt.pie(summary['duration_minutes'], labels=summary['activity_name'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Activity Distribution for {period.capitalize()}')
    plt.axis('equal')  

    # Save the plot to an in-memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='PNG')
    buf.seek(0)

    await update.message.reply_photo(photo=buf)
    plt.close() # Close the plot to free up memory










# --- Main Bot Logic ---
def main() -> None:
    """Sets up and runs the bot."""
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TOKEN:
        raise ValueError("No TELEGRAM_TOKEN found in environment variables")




    database.init_db()


    application = Application.builder().token(TOKEN).build()


    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("begin", begin))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("report", report))

    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()