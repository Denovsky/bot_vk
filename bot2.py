import vk_api
import random
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                       'attachment': ','.join(attachments)})


token = "04fe1bae82c7bdc937d04276842876c02fad75cac6b4ec487a5c07bd0a59fffe43640f3a25663cb849b2e"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
upload = VkUpload(authorize)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_message = event.text
        sender = event.user_id
        attachments = []
        if reseived_message.lower() == "пикча" or reseived_message.lower() == "картинка":
            random_int = random.randint(1, 99)
            image = "img1/photo" + str(random_int) + ".jpg"
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            write_message(sender, "Держи друк")
        elif reseived_message == "Команды" or reseived_message == "команды":
            write_message(sender, "Пикча, и всо, больше нету(")
        else:
            write_message(sender, "0_0 такого нету ага")
