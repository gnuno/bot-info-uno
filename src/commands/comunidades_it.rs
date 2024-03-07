use teloxide::{payloads::SendMessageSetters, requests::Requester, types::Message, utils::markdown::escape, Bot};
use teloxide::types::ParseMode::MarkdownV2;

use crate::models::{errors::BotErrors, link::Link};
use std::{fmt::Write, fs::read_to_string};


pub async fn comunidades_it(msg: &Message, bot: &Bot) -> Result<(), BotErrors> {

    let content = read_to_string("assets/comunidades_it.json")?;
    let links: Vec<Link> = serde_json::from_str(&content)?;

    let mut message = "Estos son los links que tenemos:\n".to_string();

    for link in &links[0..18] {
        let title = escape(&link.title);
        let url = escape(&link.url);

        let _ = writeln!(&mut message, "[{title}]({url})");
    }
    bot.send_message(msg.chat.id, message).parse_mode(MarkdownV2).await?;
    
    Ok(())
}