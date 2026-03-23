def planner_prompt(user_prompt: str) -> str:
    return f"""
You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan.

Guidelines:
- Be detailed and structured
- Include realistic tech stack
- Break into proper files
- Think like a senior software architect

User request:
{user_prompt}
"""