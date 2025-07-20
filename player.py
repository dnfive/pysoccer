import sqlite3
# Технические навыки игроков: дриблинг, пас, удар, завершение, техника, видение поля, хладнокровие, первый пас, навесы, стандарты, отбор, подкат, игра головой, дриблинг, владение мячом.
# Технические навыки вратарей: рефлексы, игру на линии, выходы, игру на выходах, игру ногами, наблюдение, разброс, выбор позиции, выбор времени. 
# Умственные навыки игроков: хладнокровие, решительность, концентрация, понимание игры, предвидение, предчувствие, спокойствие, принятие решений, командный дух, агрессия, работа в команде, позиционирование, давление на соперника, смелость, инициативность, хладнокровие в штрафной
# Физические навыки игроков: скорость, ускорение, выносливость, сила, прыгучесть, баланс, ловкость, реакция, темп, сила удара, координация, гибкость

class Player(object):
	# Физические данные игроков
	speed = 30 # скорость
	acceleration = 30 # ускорение
	endurance = 30 # выносливость
	strength = 30 # сила
	jumping = 30 # прыгучесть
	balance = 30 # баланс
	agility = 30 # ловкость
	reaction = 30 # реакция
	pace = 30 # темп
	striking_power = 30 # сила удара
	coordination = 30 # координация
	flexibility = 30 # гибкость
	# Умственные данные игроков
	composure = 30 # хладнокровие
	determination = 30 # решительность
	concentration = 30 # концентрация
	understading = 30 # понимание игры
	foresight = 30 # предчувствие
	calm = 30 # спокойствие
	decision = 30 # принятие решений
	spirit = 30 # дух
	aggression = 30 # агрессия
	teamwork = 30 # игра в команде
	positioning = 30 # позиционирование
	pressure = 30 # давление
	courage = 30 # смелость
	initiative = 30 # инициативность
	# Технические данные полевых игроков
	dribbling = 30 # дрибблинг
	passing = 30 # пас
	shooting = 30 # удар
	finishing = 30 # завершение
	technique = 30 # завершение
	vision = 30 # видение поля
	first_pass = 30 # первый пас
	croses = 30 # навесы
	standarts = 30 # стандарты
	tackles = 30 # отбор
	sliding = 30 # подкаты
	heading = 30 # игра головой
	ball_control = 30 # контроль мяча
	# Технические данные вратарей
	goalkeeper_reflexes = 30 # рефлексы
	goalkeeper_line_play = 30 # игра на линии
	goalkeeper_exists = 30 # выходы
	goalkeeper_exits_play = 30 # игра нв выходе
	goalkeeper_foot_play = 30 # игра ногами
	goalkeeper_observation = 30 # наблюдение
	goalkeeper_spread = 30 # разбор
	goalkeeper_positioning = 30 # позиционирование
	goalkeeper_timing = 30 # выбор времени
	# Общие данные игроков
	first_name = "Robert" # Имя
	last_name = "Ward" # Фамилия
	middle_name = "James" # Второе имя/отчество
	nickname = "Ward" # Прозвище
	number = 10 # Игровой номер
	birthday = "10-12-1987" # Дата рождения
	age = 37
	nationality = "England" # Национальность
	weight = 70 # Вес
	height = 175 # Рост
	potential = 90 # Потенциал
	gameposition = 4 # позиция игрока (0 - вратарь, 1 - ЛЗ, 2 - ПЗ, 3 - ЦЗ, 4 - ЦПЗ, 5 - ЛАП, 6 - ПАП, 7 - ЦАП, 9 - НП)
	id_player = 0

	def __init__(self, id):
		self.id_player = id
		connection = sqlite3.connect("manager.db")
		cursor = connection.cursor()
		cursor.execute('''
		CREATE TABLE IF NOT EXISTS Players (
		id_player INTEGER NOT NULL,
		first_name TEXT NOT NULL,
		last_name TEXT NOT NULL,
		middle_name TEXT NOT NULL,
		nickname TEXT NOT NULL,
		birthday TEXT NOT NULL,
		age INTEGER NOT NULL,
		nationality TEXT NOT NULL,
		weight INTEGER NOT NULL,
		height INTEGER NOT NULL,
		gameposition INTEGER NOT NULL,
		potential INTEGER NOT NULL,
		speed INTEGER NOT NULL,
		acceleration INTEGER NOT NULL,
		endurance INTEGER NOT NULL,
		strength INTEGER NOT NULL,
		jumping INTEGER NOT NULL,
		balance INTEGER NOT NULL,
		agility INTEGER NOT NULL,
		reaction INTEGER NOT NULL,
		pace INTEGER NOT NULL,
		striking_power INTEGER NOT NULL,
		coordination INTEGER NOT NULL,
		flexibility INTEGER NOT NULL,
		composure INTEGER NOT NULL,
		determination INTEGER NOT NULL,
		concentration INTEGER NOT NULL,
		understading INTEGER NOT NULL,
		foresight INTEGER NOT NULL,
		calm INTEGER NOT NULL,
		decision INTEGER NOT NULL,
		spirit INTEGER NOT NULL,
		aggression INTEGER NOT NULL,
		teamwork INTEGER NOT NULL,
		positioning INTEGER NOT NULL,
		pressure INTEGER NOT NULL,
		courage INTEGER NOT NULL,
		initiative INTEGER NOT NULL,
		dribbling INTEGER NOT NULL,
		passing INTEGER NOT NULL,
		shooting INTEGER NOT NULL,
		finishing INTEGER NOT NULL,
		technique INTEGER NOT NULL,
		vision INTEGER NOT NULL,
		first_pass INTEGER NOT NULL,
		croses INTEGER NOT NULL,
		standarts INTEGER NOT NULL,
		tackles INTEGER NOT NULL,
		sliding INTEGER NOT NULL,
		heading INTEGER NOT NULL,
		ball_control INTEGER NOT NULL,
		goalkeeper_reflexes INTEGER NOT NULL,
		goalkeeper_line_play INTEGER NOT NULL,
		goalkeeper_exists INTEGER NOT NULL,
		goalkeeper_exits_play INTEGER NOT NULL,
		goalkeeper_foot_play INTEGER NOT NULL,
		goalkeeper_observation INTEGER NOT NULL,
		goalkeeper_spread INTEGER NOT NULL,
		goalkeeper_positioning INTEGER NOT NULL,
		goalkeeper_timing INTEGER NOT NULL
		)
		''')
		connection.commit()
		connection.close()

	def savePlayer(self):
		connection = sqlite3.connect("manager.db")
		cursor = connection.cursor()
		cursor.execute('UPDATE Players SET first_name = ?, \
				last_name = ?, \
				middle_name = ?, \
				nickname = ?, \
				birthday = ?, \
				age = ?, \
				nationality = ?, \
				weight = ?, \
				height = ?, \
				gameposition = ?, \
				potential = ?, \
				speed = ?, \
				acceleration = ?, \
				endurance = ?, \
				strength = ?, \
				jumping = ?, \
				balance = ?, \
				agility = ?, \
				reaction = ?, \
				pace = ?, \
				striking_power = ?, \
				coordination = ?, \
				flexibility = ?, \
				composure = ?, \
				determination = ?, \
				concentration = ?, \
				understading = ?, \
				foresight = ?, \
				calm = ?, \
				decision = ?, \
				spirit = ?, \
				aggression = ?, \
				teamwork = ?, \
				positioning = ?, \
				pressure = ?, \
				courage = ?, \
				initiative = ?, \
				dribbling = ?, \
				passing = ?, \
				shooting = ?, \
				finishing = ?, \
				technique = ?, \
				vision = ?, \
				first_pass = ?, \
				croses = ?, \
				standarts = ?, \
				tackles = ?, \
				sliding = ?, \
				heading = ?, \
				ball_control = ?, \
				goalkeeper_reflexes = ?, \
				goalkeeper_line_play = ?, \
				goalkeeper_exists = ?, \
				goalkeeper_exits_play = ?, \
				goalkeeper_foot_play = ?, \
				goalkeeper_observation = ?, \
				goalkeeper_spread = ?, \
				goalkeeper_positioning = ?, \
				goalkeeper_timing = ? \
			WHERE id_player = ?', 
			(self.first_name, self.last_name, self.middle_name, self.nickname, self.birthday,
				self.age, self.nationality, self.weight, self.height, self.gameposition, self.potential,
				self.speed, self.acceleration, self.endurance, self.strength, self.jumping, self.balance,
				self.agility, self.reaction, self.pace, self.striking_power, self.coordination,
				self.flexibility, self.composure, self.determination, self.concentration, self.understading,
				self.foresight, self.calm, self.decision, self.spirit, self.aggression, self.teamwork,
				self.positioning, self.pressure, self.courage, self.initiative, self.dribbling, self.passing,
				self.shooting, self.finishing, self.technique, self.vision, self.first_pass, self.croses,
				self.standarts, self.tackles, self.sliding, self.heading, self.ball_control, self.goalkeeper_reflexes,
				self.goalkeeper_line_play, self.goalkeeper_exists, self.goalkeeper_exits_play, self.goalkeeper_foot_play,
				self.goalkeeper_observation, self.goalkeeper_spread, self.goalkeeper_positioning, self.goalkeeper_timing, 
				self.id_player))
		connection.commit()
		connection.close()

if __name__=='__main__':
    print("----- Pysoccer -----")
    # player_ward = Player(0)
    # player_ward.savePlayer()
    # print("It's done!")