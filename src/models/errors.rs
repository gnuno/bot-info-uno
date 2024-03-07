use thiserror::Error;


#[derive(Error, Debug)]
pub enum BotErrors {
    #[error(transparent)]
    TeloxideErrors(#[from] teloxide::RequestError),

    #[error("ocurrio un error haciendo ping")]
    FailureDoingPing
}