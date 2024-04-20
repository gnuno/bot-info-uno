use teloxide::{requests::Requester, types::{ChatId, Message}, Bot};
use tracing::info;

use crate::models::errors::BotErrors;

pub async fn me(msg: &Message, action: String, bot: &Bot) -> Result<(), BotErrors> {
    if action.is_empty() {
        return Err(BotErrors::MeCommandBadUsed);
    }
    
    if let Some(user) = msg.from() {
        if (user.id.0 as i64).eq(&msg.chat.id.0) {
            let username = if let Some(username) = user.username.clone() {
                username
            } else {
                user.full_name()
            };
            
            // our telegram chat id
            bot.send_message(ChatId(-1001217390053), format!("{username} {action}", )).await?;
        }
    }

    info!(" {}", msg.chat.id);

    Ok(())
}