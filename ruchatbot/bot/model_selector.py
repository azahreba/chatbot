# -*- coding: utf-8 -*-
"""
Аппликатор для модели классификатора, который определяет способ генерации
ответа чат-бота.
"""

from abc import abstractmethod

from ruchatbot.bot.model_applicator import ModelApplicator


class ModelSelector(ModelApplicator):
    def __init__(self):
        pass

    @abstractmethod
    def select_model(self, premise_str_list, question_str, text_utils):
        """
        Данный метод должен быть перегружен в производном классе, реализуя конкретный
        алгоритм классификации способа генерации ответа на пару предпосылка (premise_str)
        + вопрос (question_str)
        :param premise_str_list: unicode строки с предпосылками (0 предпосылок или больше)
        :param question_str: unicode строка с вопросом
        :param text_utils: экземпляр класса TextUtils
        :return: целое число 0...2, определяющее способ генерации ответа
        """
        raise NotImplementedError()
