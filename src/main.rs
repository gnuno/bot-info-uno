use bot::BotService;
use shuttle_secrets::SecretStore;
use teloxide::prelude::*;

pub mod bot;
pub mod command;

#[shuttle_runtime::main]
async fn shuttle_main(
    #[shuttle_secrets::Secrets] secrets: SecretStore,
) -> Result<BotService, shuttle_runtime::Error> {
    let telegram_token = secrets
        .get("TELEGRAM_TOKEN")
        .expect("TELEGRAM_TOKEN needs to be set.");

    Ok(BotService {
        bot: Bot::new(telegram_token),
    })
}
