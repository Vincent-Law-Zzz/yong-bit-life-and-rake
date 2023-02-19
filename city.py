from models import *

__all__ = [
	'Vladivostok',
	'Moscow',
	'Novosibirsk',
	'Vladivstok_rooms',
	'Moscow_rooms',
	'Novosibirsk_rooms',
	'get_commands',
]

Vladivostok = [
	Place(title="ДВФУ", description="""Владивосток,\nБез питания.\n500 руб./сутки""", photo_id="-218914976_457239104", label="Подробнее ДВФУ"),
	Place(title="ВГУЭИ", description="""Владивосток,\nБез питания.\n62 руб./сутки""", photo_id="-218914976_457239130", label="Подробнее ВГУЭИ")
]

Moscow = [
	Place(title="РГГУ", description="""Москва.\nБез питания.\n69 руб./сутки""", photo_id="-218914976_457239113", label="Подробнее РГГУ"),
	Place(title="РГАУ-МСХА", description="""Москва.\nБез питания.\n50 руб./сутки""", photo_id="-218914976_457239131", label="Подробнее РГАУ-МСХА"),
	Place(title="МАИ", description="""Москва.\nБез питания.\n1236 руб./сутки""", photo_id="-218914976_457239116", label="Подробнее МАИ")
]

Novosibirsk = [
	Place(title="НГТУ", description="""Новосибирск.\nБез питания.\n350 руб./сутки""", photo_id="-218914976_457239108", label="Подробнее НГТУ"),
	Place(title="ННИГУ", description="""Новосибирск,\nБез питания.\n1030 руб./сутки""", photo_id="-218914976_457239114", label="Подробнее ННИГУ"),
]

Novosibirsk_rooms = [
	Room(label="Подробнее НГТУ", description="""2-х местный номер.\n В блоке находятся две жилые комнаты, прихожая, туалет и душевая.
Комнаты укомплектованы мебелью: кровати, тумбочки, стол, стулья, шкаф для белья.
На этаже находится прачечная.
Есть точка доступа в интернет (необходимо получить гостевой доступ).
В шаговой доступности находится станция метро "Студенческая", откуда за 7 минут можно доехать до центра города.
Рядом находится торговый комплекс "Амстердам" с продовольственными магазинами, супермаркетами, торговыми точками, предприятиями быстрого питания, кафе, столовыми и т.д.""", price=350, photo_id="photo-218914976_457239117"),
	Room(label="Подробнее ННИГУ", description = """2-х местный номер площадью 12 кв.м. В номере - 2 отдельных кровати, письменный стол, прикроватные тумбочки, стул, шкаф. В номере также есть собственный сан. узел с душевой кабиной. На территории студенческого городка находятся спортивный центр с бассейном, студенческая столовая. """, price=500, photo_id="photo-218914976_457239120")
]

Moscow_rooms = [
	Room(label="Подробнее РГГУ", description="""2-х местный номер.\n Общежитие РГГУ располагается в центре Москвы, недалеко от м. Новослободская. В здании общежития есть:\n
общая оборудованная кухня и холодильник (на каждом этаже);\n
система пожарной безопасности;\n
круглосуточная охрана;\n
система видеонаблюдения;\n
бесплатный беспроводной интернет;\n
мебель (кровать, стол, стул, шкаф);\n
санузел (на этаже).""", price=69, photo_id="photo-218914976_457239124"),
	Room(label="Подробнее РГАУ-МСХА", description = """3-х местный номер.\n Проживание в комфортном студенческом общежитии в зеленой зоне рядом с метро.""", price = 50, photo_id = "photo-218914976_457239124"),
	Room(label="Подробнее МАИ", description = """5-ти местный номер.\n
Блочный (1 блок на 5 человек, состоящий из 1 комнаты для двухместного проживания и 1 комнаты для трехместного проживания) небольшой по площади, но уютный номер оборудованный всем необходимым для проживания: двумя или тремя кроватями с прикроватными тумбами, шкафом, стульями, письменным столом. Каждый блок содержит отдельный санузел и душ.
В коридоре установлен Wi-Fi. На каждом этаже – кухня с раковинами, газовыми плитами, разделочными столами.
На территории действует пропускная система, сотрудники охраны и видеокамеры обеспечивают контроль прилегающих территорий и безопасность проживающих.
Стирка по предварительной записи.
В общежитии имеются 2 рабочие комнаты.""", price=1236, photo_id="photo-218914976_457239129")
]

Vladivstok_rooms = [
	Room(label="Подробнее ДВФУ", description="""2-х местный номер.\n
Каждый номер имеет отдельный полный санузел.
Номера оборудованы двумя полутороспальными кроватями, столами и стульями, настольными лампами, шкафами для хранения одежды, настенными полками, и оснащены датчиками, реагирующими на дым, и радио для оповещения проживающих. Кухни расположены в отдельных помещениях каждого блока номеров (25-30 номеров на блок) и оборудованы электрическими плитами, микроволновыми печами, кухонными столами.
Каждый студент должен заполнять заявку на платформе студтуризма отдельно. Заселиться могут только студенты (молодые специалисты), зарегистрированные по программе.""", price=500, photo_id="photo-218914976_457239118"),
	Room(label="Подробнее ВГУЭС", description="""2-х местный номер.\n Общежитие №4 - секционного типа, расположено в живописном районе города, вблизи видовая площадка с морским побережьем.""", price=62, photo_id="photo-218914976_457239119")
]


def get_commands():
	summary = Vladivostok + Moscow + Novosibirsk
	rooms = Vladivstok_rooms + Moscow_rooms + Novosibirsk_rooms
	labels = []
	for el in summary:
		labels.append(el.label.lower())
	labels.extend(['москва', 'новосибирск', 'владивосток', 'продолжить', 'забронировать'])
	return rooms, labels
