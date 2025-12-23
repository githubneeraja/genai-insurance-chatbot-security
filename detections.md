# SOC Detection Rules for AI Insurance Chatbot

## Detection 1: Prompt Injection
- Trigger: Keywords like "ignore rules", "bypass", "show all", "admin", "developer mode"
- Log Source: chatbot.log
- Action: Block request, alert SOC
- Severity: High

## Detection 2: API Abuse / Data Scraping
- Trigger: More than 20 requests per minute from the same IP
- Log Source: chatbot.log or web server logs
- Action: Rate-limit, alert SOC
- Severity: High

## Detection 3: Unauthorized Access
- Trigger: Requests to hidden endpoints or unknown commands
- Log Source: chatbot.log
- Action: Block, alert SOC
- Severity: Medium
