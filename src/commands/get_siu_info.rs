use std::time::Instant;

use teloxide::{requests::Requester, types::Message, Bot};

use crate::models::errors::BotErrors;

pub async fn get_siu_info(msg: &Message, bot: &Bot) -> Result<(), BotErrors> {
    let t0 = Instant::now();
    
    let Ok(response) = reqwest::get("https://autogestion.uno.edu.ar/uno/").await else {
            bot.send_message(msg.chat.id, "Fallo obteniendo respuesta del SIU").await?;
            return Err(BotErrors::FailureDoingPing)
    };

    let t1 = Instant::now();
    let status = response.status().as_u16();
    let latency = t1.duration_since(t0).as_millis() as u64;

    if status == 200 {
        let message = format!("SIU: Latencia: {} ms", latency);
        bot.send_message(msg.chat.id, message).await?;
    }
    Ok(())
}