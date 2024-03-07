use std::fs::read_to_string;

use teloxide::{requests::Requester, types::Message, utils::html::escape, Bot};

use crate::models::{errors::BotErrors, mails_de_escuelas::Escuela};
use std::fmt::Write;

pub async fn get_mails_de_escuela(msg: &Message, bot: &Bot, school_name: String) -> Result<(), BotErrors> {
    let content = read_to_string("assets/mails_escuelas.json")?;
    let schools: Vec<Escuela> = serde_json::from_str(&content)?;
    let mut message = "Estos son los mails que tenemos:\n".to_string();

    if school_name.is_empty() {

        for school in schools {
            let escuela_title = escape(&school.name);
            writeln!(&mut message, "Escuela de {}", escuela_title)?;
            for mail in school.mails {
                let name = escape(&mail.name);
                let mail = escape(&mail.mail);
                writeln!(&mut message, "{name}: {mail}")?;
            }
        }
    } else{
        let Some(school) = schools.iter().find(|school_information| school_information.name.to_lowercase().contains(&school_name.to_lowercase())) else {
            bot.send_message(msg.chat.id, "No se encontró escuela que coincida con el nombre enviado").await?;
            return Err(BotErrors::SchoolNotFound(school_name))
        };
    
        let escuela_title = escape(&school.name);
        writeln!(&mut message, "Escuela de {}", &escuela_title)?;
        for mail in school.mails.iter() {
            let name = escape(&mail.name);
            let mail = escape(&mail.mail);
            writeln!(&mut message, "{name}: {mail}")?;
        }
    }
    
    bot.send_message(msg.chat.id, "Acá tenes los mails").await?;
    bot.send_message(msg.chat.id, message).await?;
    Ok(())
}