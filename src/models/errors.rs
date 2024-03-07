use thiserror::Error;


#[derive(Error, Debug)]
pub enum BotErrors {
    #[error(transparent)]
    TeloxideErrors(#[from] teloxide::RequestError),

    #[error(transparent)]
    IOError(#[from] std::io::Error),

    #[error(transparent)]
    Serde(#[from] serde_json::Error),

    #[error("ocurrio un error haciendo ping")]
    FailureDoingPing
}