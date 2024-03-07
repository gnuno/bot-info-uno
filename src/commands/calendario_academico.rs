use std::fs::read_to_string;

use teloxide::{payloads::SendMessageSetters, requests::{Requester, ResponseResult}, types::Message, Bot};
use teloxide::types::ParseMode::MarkdownV2;


pub async fn calendario_academico(msg: &Message, bot: &Bot) -> ResponseResult<()> {

    let content = read_to_string("assets/messages/calendario_academico.txt")?;

    bot.send_message(msg.chat.id, content).parse_mode(MarkdownV2).await?;
    
    Ok(())
}

