use teloxide::payloads::SendMessageSetters;
use teloxide::{requests::Requester, types::Message, Bot};
use teloxide::types::ParseMode::MarkdownV2;

use crate::models::errors::BotErrors;

const MESSAGE: &'static str = r#"
*Sede Rectorado*
Tel: \(0220\) 483 4150
[Belgrano 369 \- San Antonio de Padua](https://maps.app.goo.gl/6Yz6BKtcaTdcnxaz7)
Lunes a viernes de 9 a 16 hs

*CAMPUS UNIVERSITARIO*
[Av\. Dr\. Ricardo Balbín 2048\-2098, Merlo](https://maps.app.goo.gl/XpKfohxjGXmSu8dP9)
Lunes a viernes de 9 a 20 hs

*Sede Centenario*
[Centenario 1399 y Lavallol de Acosta \- San Antonio de Padua](https://maps.app.goo.gl/qMegZX6vxGE4bubr9)
Tel: \(0220\) 483 5390
Lunes a viernes de 9 a 20 hs

*Sede Córdoba*
[Córdoba 1055 \- Merlo](https://maps.app.goo.gl/mFQ4Wo8pmbHb8RJr5)
Tel: \(0220\) 482 0799
Lunes a viernes de 8 a 18 hs

*Hospital Odontológico*
[Moreno y pte\. Perón \- Merlo](https://maps.app.goo.gl/mVqNtUY9H1uDJZbWA)
"#;


pub async fn sedes(msg: &Message, bot: &Bot) -> Result<(), BotErrors> {
    bot.send_message(msg.chat.id, MESSAGE).parse_mode(MarkdownV2).await?;

    Ok(())
}