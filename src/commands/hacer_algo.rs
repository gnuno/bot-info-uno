use teloxide::{requests::{Requester, ResponseResult}, types::Message, Bot};


pub async fn hacer_algo(msg: &Message, bot: &Bot) -> ResponseResult<()> {
    bot.send_message(msg.chat.id, "Hola mundo").await?;
    println!("Hola mundo");

    Ok(())
}