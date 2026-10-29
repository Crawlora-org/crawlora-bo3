import { BO3Client } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new BO3Client({ apiKey });

  const matchHistory = await client.matchHistory({  });
  console.log("matchHistory", matchHistory);
  const economyBaseline = await client.economyBaseline({  });
  console.log("economyBaseline", economyBaseline);
