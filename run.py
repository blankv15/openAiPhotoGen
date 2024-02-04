import json

from createImage import createImage
from stockImageAssistant import generateDesc


def readStartPrompt():
    f = open('data.json')
    data = json.load(f)
    prompts = data[0]
    print("from file:", prompts)
    f.close()
    json_object = json.dumps(data[1:])

    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    return prompts


def generatePost():
    startPrompts = readStartPrompt()
    location = startPrompts['location']
    object = startPrompts['object']
    print("Location: ", location, "object: ", object)

    image_information = generateDesc(object, location)

    image_information = image_information[image_information.find("{"):image_information.rfind("}") + 1].replace("\n",
                                                                                                                " ")
    image_information = image_information.lower()
    #     image_information =  """
    #     {
    #   "image_title": "Wanderlust Companion: The Travel Backpack",
    #   "image_summary": "An image capturing the essence of a travel backpack ready for a new adventure, meticulously packed and placed at the beginning of a well-trodden dirt path in a dense, green forest. The backpack stands upright, implying the eager anticipation of the journey ahead, surrounded by nature's serenity and the promise of discovery.",
    #   "detailed_description": "The image showcases a robust and ergonomically designed travel backpack, standing upright on a slightly dusty, sun-speckled dirt path that slices through a verdant forest. The backpack, about 65 liters in capacity, boasts a sophisticated blend of deep forest green and steely gray hues. It's an embodiment of durability with rip-stop nylon material, thick foam padding on the back panel, featuring a mesh overlay for optimal air circulation and comfort.
    #
    # The backpack's structure is well-defined with contoured shoulder straps that are absent of hands or arms, but shaped as if waiting to be worn. The hip belt is substantial, padded, and articulated, designed to distribute weight efficiently, hugging the bag's lower contours. On the front, a series of adjustable straps with squeeze-style quick release buckles allow for external gear attachment, and a few carabiners dangle showcasing its function and utility.
    #
    # A small, detachable daypack is visibly clipped onto the main backpack, exhibiting a matching color scheme and material. It promises versatility with its own separate compartments, ideal for short explorations away from the main camp or hostel. Near the base of the backpack sits a zippered compartment, hinting at a tucked-away rain cover with a reflective logo that would shimmer slightly as it catches the occasional rays of sunlight filtering through the dense canopy above.
    #
    # It's evident the main compartment of the backpack is neatly packed, without bulges, indicating careful and experienced packing. The sizeable, U-shaped zipper reveals a glimpse of an organized interior with a variety of packing cubes and a dedicated laptop sleeve which is discreetly padded and suspended, ensuring device safety during travel.
    #
    # On one side of the backpack, an expandable mesh pocket holds a stainless steel water bottle with a moisture-beaded surface, reflecting the humidity of the surrounding forest. The opposite side features trekking pole attachments and a compact, rolled-up foam sleeping pad secured by two horizontal straps with a friction buckle.
    #
    # The forest setting emanates a tranquil ambiance, where towering trees with gnarled roots flank the narrow trail and a chorus of distant bird calls resonates through the air. Rays of sunlight pierce through the dense foliage, creating a dappled pattern across the scene. A light mist hangs in the air, wrapping the setting in a veil of mystery, enhancing the allure of hidden natural wonders that beckon to be explored.
    #
    # Overall, the image captures the nuanced interplay between the allure of adventure inherent in the travel backpack and the serene, unbridled beauty of the wilderness it's poised to explore."
    # }
    #
    #     """
    # imageInfomationDescription = image_infomation[image_infomation.find('detailed_description":'):].replace("\n"," ")
    # image_infomation = image_infomation[:image_infomation.find('detailed_description":')] +imageInfomationDescription
    print(image_information)
    imageInformationDict = json.loads(image_information)

    imageTitle = imageInformationDict["image_title"]
    image_summary = imageInformationDict["image_summary"]
    detailed_description = imageInformationDict["detailed_description"]

    print("imageTitle: ", imageTitle)
    print("image_summary: ", image_summary)
    print("detailed_description: ", detailed_description)

    createImage(detailed_description, imageTitle)


generatePost()
