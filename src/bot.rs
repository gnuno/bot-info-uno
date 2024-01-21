use std::sync::Arc;

use crate::command::Command;
use shuttle_runtime::Service;
use teloxide::{dispatching::UpdateFilterExt, prelude::*, utils::html, RequestError};
use tracing::log::debug;

pub struct BotService {
    pub bot: Bot,
}

pub struct InstanceState;

#[shuttle_runtime::async_trait]
impl Service for BotService {
    async fn bind(mut self, _addr: std::net::SocketAddr) -> Result<(), shuttle_runtime::Error> {
        self.start()
            .await
            .expect("An error occured while using the bot!");

        Ok(())
    }
}

async fn log_update(u: Update) {
    debug!("{:#?}", u);
}

async fn unhandled_update(upd: Arc<Update>) {
    debug!("unhandled update: {upd:?}");
}

async fn error_log(err: RequestError) {
    tracing::error!("dispatcher error: {err}")
}

impl BotService {
    async fn start(&self) -> Result<(), shuttle_runtime::CustomError> {
        let bot = self.bot.clone();

        let reply_commands = Update::filter_message().branch(
            dptree::entry()
                .filter_command::<Command>()
                .endpoint(Command::reply),
        );

        let member_updates = Update::filter_chat_member()
            .branch(
                dptree::filter(|m: ChatMemberUpdated| {
                    m.old_chat_member.is_left() && m.new_chat_member.is_present()
                })
                .endpoint(new_chat_member),
            )
            .branch(
                dptree::filter(|m: ChatMemberUpdated| {
                    m.old_chat_member.is_present() && m.new_chat_member.is_left()
                })
                .endpoint(left_chat_member),
            );

        let handler = dptree::entry()
            .inspect_async(log_update)
            .branch(reply_commands)
            .branch(member_updates);

        let dependencies = dptree::deps![Arc::new(InstanceState {})];

        Dispatcher::builder(bot, handler)
            .dependencies(dependencies)
            .default_handler(unhandled_update)
            .error_handler(Arc::new(error_log))
            .enable_ctrlc_handler()
            .build()
            .dispatch()
            .await;
        Ok(())
    }
}

/// Welcome Endpoint
async fn new_chat_member(bot: Bot, chat_member: ChatMemberUpdated) -> ResponseResult<()> {
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

async fn left_chat_member(bot: Bot, chat_member: ChatMemberUpdated) -> ResponseResult<()> {
    let user = chat_member.old_chat_member.user;

    let username = user
        .mention()
        .unwrap_or_else(|| html::user_mention(user.id.0 as i64, user.full_name().as_str()));

    bot.send_message(
        chat_member.chat.id,
        format!("Hasta la proximaaaa {username}!"),
    )
    .await?;

    Ok(())
}
