# Allora Worker Node Base

This repository serves as a base template for implementing your own prediction model as part of the Allora network.

Currently, the `app.py` script generates a random prediction for ETH (`y_pred`). You should replace this with your own model code. Your model should fetch data (e.g., from Tiingo) and generate a prediction for the topic(s) specified in `config.json`, assigning the result to the `y_pred` variable.

The worker node periodically invokes the `get_inference` function with a token (from `config.json`). This function must return a prediction specific to the token provided, as network requests will be made at regular intervals (defined by `epoch_length`).

---

## Getting Started

Clone the repository and navigate into it:

```sh
git clone https://github.com/t-hossein/Allora-Worker-Node-Base
cd Allora-Worker-Node-Base
```

Implement your model inside the `app.py` file as described above.

Next, update the `config.json` file with:

* Your wallet's mnemonic phrase (the 12/24-word recovery phrase)
* The topics you intend to participate in

---

## Initialize Config

Make the `init.config` script executable and run it:

```sh
chmod +x init.config
./init.config
```

---

## Run the Worker

Start the worker and inference containers using Docker:

```sh
docker compose up -d --build 
```

---

## Verifying Inference Submission

Check the logs to confirm that your worker is successfully sending inferences to the chain:

```
{"level":"debug","msg":"Send Worker Data to chain","txHash":<tx-hash>,"time":<timestamp>,"message":"Success"}
```

If you encounter issues during container build, run the following to view detailed errors:

```sh
docker compose up --build 
```

---

## Logging and Troubleshooting

To check your worker logs:

```sh
docker logs worker
```

If you’re seeing successful transaction logs, your worker is functioning properly.

To inspect logs related to your model’s predictions:

```sh
docker logs inference
```

This is where you’ll find any errors or issues related to your `app.py` script and its ability to make predictions.

