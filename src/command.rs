use std::{error::Error, sync::Arc};

use teloxide::{prelude::*, types::Me, utils::command::BotCommands};
use tracing::error;

use crate::{bot::InstanceState, commands::{calendario_academico::calendario_academico, comunidades_it::comunidades_it, get_siu_info::get_siu_info, hacer_algo::hacer_algo, links_utiles::links_utiles, mails_de_escuela::get_mails_de_escuela}, models::errors::BotErrors};

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
    #[command(description = "Hace algo")]
    HacerAlgo,
    #[command(description = "Devuelve una lista de links")]
    Links,
    #[command(description = "Lista las comunidades IT que tenemos")]
    ComunidadesIT,
    #[command(description = "Muestra el calendario académico")]
    CalendarioAcademico,
    #[command(description = "Obtener estado del SIU")]
    SIU,
    #[command(description = "Obtener mails de Escuela")]
    MailDeEscuela(String),
}

impl Command {
    /// Function used for handling various commands matched.
    pub async fn reply(
        _state: Arc<InstanceState>,
        bot: Bot,
        _sender: Me,
        msg: Message,
        cmd: Command,
    ) -> Result<(), BotErrors> {
        
        let response = match cmd {
            Command::Help => help(&msg, &bot).await,
            Command::HacerAlgo => hacer_algo(&msg, &bot).await,
            Command::Links => links_utiles(&msg, &bot).await,
            Command::CalendarioAcademico => calendario_academico(&msg, &bot).await,
            Command::SIU => get_siu_info(&msg, &bot).await,
            Command::ComunidadesIT => comunidades_it(&msg, &bot).await,
            Command::MailDeEscuela(escuela) => get_mails_de_escuela(&msg, &bot, escuela).await
        };

        if let Err(error) = response {
            error!("Ha ocurrido un error: {:?}", error.source());
            bot.send_message(msg.chat.id, error.to_string()).await?;
        }

        Ok(())
    }
}

async fn help(msg: &Message, bot: &Bot) -> Result<(), BotErrors> {
    bot.send_message(msg.chat.id, Command::descriptions().to_string()).await?;
    Ok(())
}