from openai import OpenAI


def generateDesc(object, location):

    # Update with your API key
    client = OpenAI()

    instructions = """
    You create detailed descriptions for these tasks. The descriptions are used to generate an image with AI. So, every description needs a lot of detail. also, no hands are to be shown in the photos
    You will also return an image title, a two-sentence summary of the image and the detailed descriptions which is at least 425 words. You will return all this information in JSON format 
    """



    # Create and configure the assistant
    assistant = client.beta.assistants.create(
        name="Terrific Travels",
        instructions=instructions,
        model="gpt-4-1106-preview",
    )

    # Create a thread where the conversation will happen
    thread = client.beta.threads.create()

    # Create the user message and add it to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Object/Person: "+ object+ ", Location: "+ object+ "location",
    )

    # Create the Run, passing in the thread and the assistant
    run = client.beta.threads.runs.create(
      thread_id=thread.id,
      assistant_id=assistant.id
    )

    # Periodically retrieve the Run to check status and see if it has completed
    # Should print "in_progress" several times before completing
    while run.status != "completed":
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(f"Run status: {keep_retrieving_run.status}")

        if keep_retrieving_run.status == "completed":
            print("\n")
            break

    # Retrieve messages added by the Assistant to the thread
    all_messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    # Print the messages from the user and the assistant
   ##print(f"USER: {message.content[0].text.value}")
   # print(f"ASSISTANT: {all_messages.data[0].content[0].text.value}")
    return all_messages.data[0].content[0].text.value