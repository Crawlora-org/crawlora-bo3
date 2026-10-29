use crawlora_bo3::{serde_json, Bo3MatchHistoryParams, Client};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .bo3
        .match_history(Bo3MatchHistoryParams {
            ..Default::default()
        })
        .await?;
    let data: serde_json::Value = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
