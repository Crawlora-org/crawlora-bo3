import { BO3Client } from "../src/index.js";

const client = new BO3Client({ apiKey: "test-key" });
void client.match({"slug": "sample"});
void client.request("bo3-match", {"slug": "sample"});
const streamResponse: Promise<Response> = client.request("bo3-match", {"slug": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("bo3-match", {"slug": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.match({"slug": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("bo3-match", {"slug": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("bo3-match", {"slug": "sample"}, { responseType: "text" });
void rawText;


void client.economyBaseline();
void client.request("bo3-economy-baseline");
// @ts-expect-error The selected operation requires its documented params.
void client.match();
