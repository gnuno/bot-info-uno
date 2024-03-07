use serde::{Deserialize, Serialize};

#[derive(Default, Debug, Clone, PartialEq, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Escuela {
    #[serde(rename = "escuela")]
    pub name: String,
    pub mails: Vec<Mail>,
}

#[derive(Default, Debug, Clone, PartialEq, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Mail {
    pub name: String,
    pub mail: String,
}
