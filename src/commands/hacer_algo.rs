use teloxide::{requests::Requester, types::Message, Bot};

use crate::models::errors::BotErrors;


pub async fn hacer_algo(msg: &Message, bot: &Bot) -> Result<(), BotErrors> {
    bot.send_message(msg.chat.id, "Hola mundo").await?;
    println!("Hola mundo");

    Ok(())
}