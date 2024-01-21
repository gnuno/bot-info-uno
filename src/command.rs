use std::sync::Arc;

use teloxide::{prelude::*, types::Me, utils::command::BotCommands};

use crate::bot::InstanceState;

/// Enumeration of commands accepted by the bot.
#[derive(BotCommands, Clone)]
#[command(
    rename_rule = "lowercase",
    description = "Bienvenidos al bot de Telegram de la UNO! Gracias por usarme.
Para reportar bugs, escribelos aquí: https://github.com/gnuno/bot-info-uno/issues.

Estos son los siguientes comandos:"
)]
pub enum Command {
    #[command(description = "Muestra este texto. Uso: /help")]
    Help,
}

impl Command {
    /// Function used for handling various commands matched.
    pub async fn reply(
        _state: Arc<InstanceState>,
        bot: Bot,
        _sender: Me,
        msg: Message,
        cmd: Command,
    ) -> ResponseResult<()> {
        match cmd {
            Command::Help => {
                bot.send_message(msg.chat.id, Command::descriptions().to_string())
                    .await?;
            }
        }

        Ok(())
    }
}
