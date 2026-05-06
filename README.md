# AI Study Assistant — ITAI 2376 Final Project

## Project Title
Jai'AnniWhite_Solo_ITAI2376

## Description
This project is a Python-based AI Study Assistant that helps students learn computer science concepts using question answering, summarization, and quiz generation.

## Problem Being Solved
Students need a simple assistant that explains programming concepts clearly and provides practice questions.

## Target Users
Beginner computer science students.

## Architecture Overview
The system uses:
- Intent Classification to detect user request type
- Retrieval system (RAG-style) to find relevant knowledge
- Generator module to produce responses

### Architecture Flow
User Input → Intent Classifier → RAG Retrieval → Generator → Output

## Tools Used
- Python
- Rule-based NLP (no external APIs required)

## How to Run

```bash
## How to Run

If Python command works:
python agent.py

If not working (Windows fallback):
py agent.py