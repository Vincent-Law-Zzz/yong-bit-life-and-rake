import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from city import Moscow, Moscow_rooms, Vladivostok, Vladivstok_rooms, Novosibirsk, Novosibirsk_rooms, get_commands
from tools import *

vk_session = vk_api.VkApi(token="vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

rooms, commands = get_commands()

cities = {
	'москва': Moscow,
	'новосибирск': Novosibirsk,
	'владивосток': Vladivostok
}


def find_room(event):
	for r in rooms:
		if r.label.lower() == event.text.lower():
			send_description(event.user_id, r)


def process_event(event):
	if event.text.lower() in ['москва', 'новосибирск', 'владивосток']:
		print(cities.get(event.text.lower(), None))
		send_carousel(
			user_id=event.user_id,
			template=build_carousel_template(
				cities.get(event.text.lower(), None)
			)
		)
	elif event.text.lower() != 'продолжить' and event.text.lower() != 'забронировать':
		find_room(event)
	elif event.text.lower() == 'продолжить':
		get_city(event.user_id)
	elif event.text.lower() == 'забронировать':
		send_award(event.user_id)
		list_awards(event.user_id)


def run():
	for event in longpool.listen():
		print(event.type)
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				msg = event.text.lower()
				id = event.user_id
				if event.text.lower() in commands:
					process_event(event)
				else:
					send_hello(event.user_id)


if __name__ == '__main__':
	run()