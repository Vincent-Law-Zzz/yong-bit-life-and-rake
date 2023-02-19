import json
import random

import httpx
from typing import List, Dict
from models import *


def build_template_elements(
	data: List[Place]
) -> List[Dict]:
	res = []
	for el in data:
		element = {
			"title": f"{el.title}",
			"description": f"{el.description}",
			"photo_id": f"{el.photo_id}",
			"action": {
				"type": "open_photo"
			},
			"buttons": [
				{
				"action": {
					"type": "text",
					"label": f"{el.label}",
					}
				}
			]
		}
		res.append(element)
	return res


def build_carousel_template(data: List[Place]) -> str:
	elements = build_template_elements(data=data)
	template = {"type": "carousel", "elements": elements}
	print(template)
	print('-----')
	return json.dumps(template)


def send_hello(user_id):
	keyboard = {
		"inline": True,
		"buttons": [
			[
				{
					"action": {
						"type": "text",
						"label": "Продолжить",
					},
				},
			]
		]
	}
	data = {
		"access_token": "vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ",
		"user_id": user_id,
		"random_id": random.randint(0, 999999999999999),
		"attachment": 'photo-218914976_457239126',
		"keyboard": json.dumps(keyboard),
		"message": f"""Привет!👋👋\n
		Добро пожаловать в Студтуризм!\n
		С помощью этого бота ты сможешь найти для себя подходящее путешествие и сразу же забронировать, для тебя мы сделали удобные фильтры для поиска🔥\n
		Когда я узнаю про новые маршруты, я сразу сообщу, чтобы ты успел выгодно забронировать поездку\n
		Чем я еще могу быть полезен:\n
		❗️Напомню про выбранную поездку
		⏰ Укажи любую удобную дату — буду уведомлять о появлении свободных мест в этот период с подробной информацией\n
		❤️Ты можешь добавить понравившиеся города и места проживания в избранное\n
		Можно создать несколько подписок на разные направления и даты, проверю все варианты 👌
		""",
		"v": 5.81
	}
	resp = httpx.post('https://api.vk.com/method/messages.send', data=data)
	print(resp.text)


def get_city(user_id):
	keyboard = {
		"inline": True,
		"buttons": [
			[
				{
					"action": {
						"type": "text",
						"label": "Москва",
					},
				},
			],
			[
				{
					"action": {
						"type": "text",
						"label": "Новосибирск",
					},
				},
			],
			[
				{
					"action": {
						"type": "text",
						"label": "Владивосток",
					},
				},
			]
		]
	}
	data = {
		"access_token": "vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ",
		"user_id": user_id,
		"random_id": random.randint(0, 999999999999999),
		"keyboard": json.dumps(keyboard),
		"message": "Выберите пожалуйста город из списка.",
		"v": 5.81
	}
	resp = httpx.post('https://api.vk.com/method/messages.send', data=data)
	print(resp.text)


def send_carousel(user_id: int, template: str):
	data = {
		"access_token": "vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ",
		"user_id": user_id,
		"random_id": random.randint(0, 999999999999999),
		"template": template,
		"message": "Вот что удалось найти :",
		"v": 5.81
	}
	resp = httpx.post('https://api.vk.com/method/messages.send', data=data)
	print(resp.text)


def send_description(user_id: int, data: Room):
	keyboard = {
		"inline": True,
		"buttons": [
			[
				{
					"action": {
						"type": "text",
						"label": "Забронировать",
					},
				},
			],
			[
				{
				"action": {
					"type": "vkpay",
					"hash": f"action=transfer-to-group&group_id=218914976&aid={data.price}",
					},
				},
			]
		]
	}
	data = {
		"access_token": "vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ",
		"user_id": user_id,
		"random_id": random.randint(0, 999999999999999),
		"attachment": data.photo_id,
		"keyboard": json.dumps(keyboard),
		"message": f"{data.description}",
		"v": 5.81
	}
	resp = httpx.post('https://api.vk.com/method/messages.send', data=data)
	print(resp.text)


def send_award(user_id):
	keyboard = {
		"inline": True,
		"buttons": [
			[
				{
					"action": {
						"type": "text",
						"label": "Продолжить",
					},
				},
			]
		]
	}
	data = {
		"access_token": "vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ",
		"user_id": user_id,
		"random_id": random.randint(0, 999999999999999),
		"attachment": 'photo-218914976_457239127',
		"keyboard": json.dumps(keyboard),
		"message": f"""
			Поздравляю! 🥳🥳
			Ты получаешь достижение!🤩
			“Так рождаются легенды” - За бронирование своей первой поездки 🚉
			Пусть она получится незабываемой 🌻
			А пока держи стикер и скорее собирать чемодан!🧳
			""",
		"v": 5.81
	}
	resp = httpx.post('https://api.vk.com/method/messages.send', data=data)
	print(resp.text)


def list_awards(user_id):
	keyboard = {
		"inline": True,
		"buttons": [
			[
				{
					"action": {
						"type": "text",
						"label": "Продолжить",
					},
				},
			]
		]
	}
	data = {
		"access_token": "vk1.a.Pp0qiMfKJ26jQ8IqKdQKiLXxRjazh0jFE_YZYYuGonqfY8jg5QpDzGrmzYsLq2cI5zk1KKycibnR8PLaNvcPaQEHW8D5EFwuNpILjU-eF9WwGP6fzart4cl6qfnvy6ZXmvhvUGNdFfCdiWyf1etFh2ua3zdcGoGsha02I6nAg_08VM5S4ZPPU6VaJX_W5Ec-CFnbMZKhjbuwuqFB1x4FtQ",
		"user_id": user_id,
		"random_id": random.randint(0, 999999999999999),
		"attachment": 'photo-218914976_457239128',
		"keyboard": json.dumps(keyboard),
		"message": f"""
			Вот список всех возможных достижений🤩
			Скорее собери их все💯
			""",
		"v": 5.81
	}
	resp = httpx.post('https://api.vk.com/method/messages.send', data=data)
	print(resp.text)
