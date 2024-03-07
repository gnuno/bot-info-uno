use std::fs::read_to_string;

use teloxide::{requests::Requester, types::Message, utils::html::escape, Bot};

use crate::models::{errors::BotErrors, mails_de_escuelas::Escuela};
use std::fmt::Write;

pub async fn get_mails_de_escuela(msg: &Message, bot: &Bot, nombre_de_escuela: String) -> Result<(), BotErrors> {
    bot.send_message(msg.chat.id, "Acá tenes los mails").await?;
    let content = read_to_string("assets/mails_escuelas.json")?;
    let escuelas: Vec<Escuela> = serde_json::from_str(&content)?;

    if nombre_de_escuela.is_empty() {
        let mut message = "Estos son los mails que tenemos:\n".to_string();
        for escuela in escuelas {
            let escuela_title = escape(&escuela.escuela);
            let _ = writeln!(&mut message, "Escuela de {}", escuela_title);
            for mail in escuela.mails {
                let name = escape(&mail.name);
                let mail = escape(&mail.mail);
                let _ = writeln!(&mut message, "{name}: {mail}");
            }
        
        }
        bot.send_message(msg.chat.id, message).await?;
    } else{
        let Some(escuela) = escuelas.iter().find(|escuela| escuela.escuela.to_lowercase().contains(&nombre_de_escuela.to_lowercase())) else {
            bot.send_message(msg.chat.id, "No se encontró escuela que coincida con el nombre enviado").await?;
            return Ok(())
        };
        let mut message = "Estos son los mails que tenemos:\n".to_string();
    
        let escuela_title = escape(&escuela.escuela);
        let _ = writeln!(&mut message, "Escuela de {}", &escuela_title);
        for mail in escuela.mails.iter() {
            let name = escape(&mail.name);
            let mail = escape(&mail.mail);
            let _ = writeln!(&mut message, "{name}: {mail}");
        }
        bot.send_message(msg.chat.id, message).await?;
    }

    Ok(())
}