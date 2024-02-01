import requests

from ImageGen import Image
import urllib.request

imagePrompt = ("""
Set within the quiet reverence of an old library in a historic mansion, the scene is carefully constructed to capture a moment frozen in time. An antique typewriter, the centerpiece of this tableau, rests on a robust mahogany desk with an intricate design. Particular attention is given to its black cast iron body, showcasing the patina of age on its curved edges and the Victorian elegance in its design. The round keys of the typewriter are made of ivory, each bearing a letter in a classic typeface, weathered but still proud. The keys are arranged in orderly rows, and the space bar exhibits signs of extensive use, hinting at the countless stories once brought to life here.

Directly in front of the typewriter, a piece of yellowed paper is securely held by the machine's platinum roller, with faint, blue horizontal lines and a half-typed letter visible, bearing a salutation and the beginning of a timeless introspection, the ink slightly smudged from the ribbon, black and purple, which loops through the intricate metal typebars. The nostalgic air is palpable as the roller waits in silent anticipation for the return of its author. 

In the background, book-lined walls rise to a high vaulted ceiling, with the books ranging in size and color, their spines lined with gold-lettered titles and intricate patterns. Ladders with brass fittings are connected to rails, allowing access to the highest shelves. The faint light filtering through the mullioned windows dusts the room with a golden hue, highlighting the floating motes of history carried in the air. No modern technology is present to interrupt the historic ambiance.

The vintage desk on which the typewriter sits is adorned with additional artifacts of the literary past. To the left of the typewriter, there is a glass inkwell with a silver cap, its quill absent but imagined hovering just out of sight, dipped in ebony ink. To the right, a leather-bound ledger sits closed, its strap firmly wrapped around it, suggesting a ledger of records or a private journal. Every object is positioned to convey usage without the presence of hands or human interaction, allowing the viewer to believe they have stumbled upon this setting just moments after the room's occupant has stepped away.

Above the desk, a stained glass lamp casts a warm, subdued light over the area, its pattern reminiscent of Art Nouveau, with swirls and floral motifs. The light enhances the somber, contemplative mood, inviting the onlooker to consider the history and creative endeavors that have transpired in this silent chamber. The image is composed in such a manner to create an enchanting and immersive experience, transporting one back to a bygone era of literary magnificence.


""")

newImage = Image(imagePrompt)
imgURL = newImage.createImage()
# newImage.getImageUrl()

urllib.request.urlretrieve(imgURL, "Timeless Words in the Storied Halls.jpg")
urllib.request.urlretrieve()

