from agent import make_agent


TodoAgent = make_agent()
messages = []

while True:
    query = input('You: ')
    messages.append(
        ("user", query)
    )

    response = TodoAgent.invoke(
        {
            "messages": messages
        }
    )

    messages = response["messages"]

    print(
        "AI:",
        response["messages"][-1].content
    )