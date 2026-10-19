curl https://api.openai.com/v1/chat/completions ^
-H "Authorization: Bearer %OPENAI_API_KEY%" ^
-H "Content-Type: application/json"  ^
-d "{\"model\":\"gpt-4o-mini\",\"messages\":[{\"role\":\"user\",\"content\":\"안녕\"}],\"max_tokens\":10}"

----------------------


curl https://api.openai.com/v1/chat/completions ^
-H "Authorization: Bearer %OPENAI_API_KEY%" ^
-H "Content-Type: application/json" ^
-d "{\"model\":\"gpt-6-luna\",\"messages\":[{\"role\":\"user\",\"content\":\"안녕\"}],\"reasoning_effort\":\"none\",\"max_completion_tokens\":50}"
