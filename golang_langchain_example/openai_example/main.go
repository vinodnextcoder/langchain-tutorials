package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/openai"
)

func main() {

	// ✅ Load .env
	if err := godotenv.Load(); err != nil {
		log.Fatal("❌ Failed to load .env file:", err)
	}

	// ✅ Read OpenRouter key
	apiKey := os.Getenv("OPENROUTER_API_KEY")
	if apiKey == "" {
		log.Fatal("❌ OPENROUTER_API_KEY not found in .env")
	}

	ctx := context.Background()

	// ✅ Initialize OpenRouter (OpenAI-compatible)
	llm, err := openai.New(
		openai.WithToken(apiKey),
		openai.WithBaseURL("https://openrouter.ai/api/v1"),
		openai.WithModel("x-ai/grok-4.1-fast:free"),
	)
	if err != nil {
		log.Fatal("❌ Failed to initialize LLM:", err)
	}

	prompt := "What is artificial intelligence in simple terms?"

	// ✅ Generate response
	response, err := llms.GenerateFromSinglePrompt(ctx, llm, prompt)
	if err != nil {
		log.Fatal("❌ LLM Generation Error:", err)
	}

	fmt.Println("\n✅ AI Response:")
	fmt.Println(response)
}
