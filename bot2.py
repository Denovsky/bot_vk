import vk_api
import random
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                       'attachment': ','.join(attachments)})


token = "d69e74476f027c67ccbfb8cb5f6309f5b61081cadbeb1c5b3f5762722a8367fd81ae8ebb5d2a5a4c4a27d"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
upload = VkUpload(authorize)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_message = event.text
        sender = event.user_id
        attachments = []
        if reseived_message == "пикча" or reseived_message == "Картинка" or reseived_message == "картинка" or reseived_message == "Пикча":
            random_int = random.randint(1, 2)
            image = "img/photo0" + str(random_int) + ".jpg"
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            write_message(sender, "нА, патеряйся")
            print(reseived_message)
        elif reseived_message == "гей":
            write_message(sender, "сам " + reseived_message)
        elif reseived_message == "жопа ты(":
            write_message(sender, "САМ(")
        else:
            write_message(sender, "0_0 такого нету ага")
