use teloxide::{payloads::SendMessageSetters, requests::{Requester, ResponseResult}, types::Message, utils::markdown::escape, Bot, RequestError};
use teloxide::types::ParseMode::MarkdownV2;

use crate::models::link::Link;
use std::{fmt::Write, fs::read_to_string};


pub async fn links_utiles(msg: &Message, bot: &Bot) -> ResponseResult<()> {

    let content = read_to_string("assets/links.json")?;
    let links: Vec<Link> = serde_json::from_str(&content).map_err(|e|RequestError::InvalidJson { source: e, raw: content.into_boxed_str() })?;

    let mut message = "Estos son los links que tenemos:\n".to_string();

    for link in &links[0..18] {
        let title = escape(&link.title);
        let url = escape(&link.url);

        let _ = writeln!(&mut message, "[{title}]({url})");
    }
    bot.send_message(msg.chat.id, message).parse_mode(MarkdownV2).await?;
    
    Ok(())
}