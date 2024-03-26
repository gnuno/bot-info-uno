use teloxide::{requests::Requester, types::Message, Bot};

use crate::models::errors::BotErrors;


pub async fn roadmap(msg: &Message, bot: &Bot) -> Result<(), BotErrors> {
    bot.send_message(msg.chat.id, "https://i.ibb.co/yB15FSW/Programa.jpg").await?;
    println!("enviando link imagen");

    Ok(())
}