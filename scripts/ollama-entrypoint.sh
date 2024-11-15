#!/bin/bash

/bin/ollama serve &
pid=$!
sleep 5
ollama pull llama3.2:1b
wait $pid