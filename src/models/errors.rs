use thiserror::Error;


#[derive(Error, Debug)]
pub enum BotErrors {
    #[error("Ha habido un problema de comunicación con Telegram")]
    TeloxideErrors(#[from] teloxide::RequestError),

    #[error("No se ha podido obtener el archivo correspondiente")]
    IOError(#[from] std::io::Error),

    #[error("Hubo un problema transformando un JSON")]
    Serde(#[from] serde_json::Error),

    #[error("Ocurrio un error formateando")]
    Format(#[from] std::fmt::Error),

    #[error("Ocurrio un error haciendo ping")]
    FailureDoingPing,

    #[error("No existe la escuela con el nombre `{0}`")]
    SchoolNotFound(String)
}