use teloxide::{Bot, types::ChatMemberUpdated, requests::{ResponseResult, Requester}, utils::html};



/// Welcome Endpoint
pub async fn new_chat_member(bot: Bot, chat_member: ChatMemberUpdated) -> ResponseResult<()> {
    let user = chat_member.old_chat_member.user.clone();

    let telegram_group_name = chat_member.chat.title().unwrap_or("");

    // We get a "@username" mention via `mention()` method if the user has a
    // username, otherwise we create a textual mention with "Full Name" as the
    // text linking to the user
    let username = user
        .mention()
        .unwrap_or_else(|| html::user_mention(user.id.0 as i64, user.full_name().as_str()));

    bot.send_message(chat_member.chat.id, format!("Bienvenidx a {telegram_group_name}, un lugar horrible pero bueno, pasala bien {username}!"))
        .await?;

    Ok(())
}

