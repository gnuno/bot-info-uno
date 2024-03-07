use thiserror::Error;


#[derive(Error, Debug)]
pub enum BotErrors {
    #[error(transparent)]
    TeloxideErrors(#[from] teloxide::RequestError),

    #[error(transparent)]
    IOError(#[from] std::io::Error),

    #[error(transparent)]
    Serde(#[from] serde_json::Error),

    #[error(transparent)]
    Format(#[from] std::fmt::Error),

    #[error("ocurrio un error haciendo ping")]
    FailureDoingPing,

    #[error("No existe la escuela con el nombre `{0}`")]
    SchoolNotFound(String)
}