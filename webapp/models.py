from django.db import models

#Организация
class Organization(models.Model):
	name = models.CharField("Название",max_length=50, unique=True)
	about = models.TextField("Описание",blank=True)
	photo = models.CharField("Фото",max_length=100, blank=True)
	phone = models.CharField("Телефон",max_length = 20, blank=True)
	email = models.CharField("Почта",max_length=30, blank=True)

	def __str__(self):
		return self.name

#Пользователи
#class User(models.Model):
#	first_name = models.CharField("Имя",max_length=50)
#	last_name = models.CharField("Фамилия",max_length=50)
#	org = models.ForeignKey(Organization, verbose_name="Организация")
#	login = models.CharField("Логин",max_length=30)
#	passwd = models.CharField("Пароль",	max_length=30)
#	email = models.CharField("Почта",max_length=30)
#	image = models.CharField("Картинка", max_length=100, blank=True)	
#
#	def __str__(self):
#		return '%s %s' % (self.first_name, self.last_name)

#Отделы
#class Depart(models.Model):
#	name = models.CharField("Название",max_length=100,unique=True)
#	depart = models.CharField("Состоит в",max_length=30)
#
#	def __str__(self):
#		return self.name
#
#		#Тип покупки
#class Category(models.Model):
#	name = models.CharField("Тип покупки", max_length = 30)
#
#	def __str__(self):
#		return self.name
#
#Покупки
#class Purchase(models.Model):
#	name = models.CharField("Название",max_length=50)
#	user = models.ForeignKey(User, verbose_name="Пользователь")
#	depart = models.ForeignKey(Depart,verbose_name = "Отдел")
#	date = models.DateTimeField("Дата совершения",auto_now=True, blank=True)
#	cost = models.FloatField("Сумма",default = 0)
#	state = models.FloatField("Состояние")#оплачена или нет
#	about = models.TextField(blank=True)
#	category = models.ForeignKey(Category)

#	def __str__(self):
#		return self.name

#ПОП - Покупатель - Отдел - Покупка
#class POP(models.Model):
#	user = models.ForeignKey(User, verbose_name="Пользователь")
#	depart = models.ForeignKey(Depart, verbose_name = "Отдел")
#	purchase = models.ForeignKey(Purchase, verbose_name = "Покупка")
#
#	def __str__(self):
#		return self.us_id

#ПО - Покупатель - Отдел
#class PO(models.Model):
#	user = models.ForeignKey(User, verbose_name = "Пользователь")
#	depart = models.ForeignKey(Depart, verbose_name = "Отдел")
#
#	def __str__(self):
#		return self.us_id