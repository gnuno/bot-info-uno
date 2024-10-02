use bot::BotService;
use shuttle_runtime::SecretStore;
use teloxide::prelude::*;

pub mod bot;
pub mod command;

pub mod commands;
pub mod hooks;
pub mod models;

#[shuttle_runtime::main]
async fn shuttle_main(
    #[shuttle_runtime::Secrets] secrets: SecretStore,
) -> Result<BotService, shuttle_runtime::Error> {
    let telegram_token = secrets
        .get("TELEGRAM_TOKEN")
        .expect("TELEGRAM_TOKEN needs to be set.");

    Ok(BotService {
        bot: Bot::new(telegram_token),
    })
}
