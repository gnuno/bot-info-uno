use teloxide::{Bot, types::ChatMemberUpdated, requests::Requester, utils::html};

use crate::models::errors::BotErrors;


pub async fn left_chat_member(bot: Bot, chat_member: ChatMemberUpdated) -> Result<(), BotErrors> {
    let user = chat_member.old_chat_member.user;

    let username = user
        .mention()
        .unwrap_or_else(|| html::user_mention(user.id.0 as i64, user.full_name().as_str()));

    bot.send_message(
        chat_member.chat.id,
        format!("Hasta la proximaaaa {username}!"),
    )
    .await?;

    Ok(())
}