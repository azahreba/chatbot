# -*- coding: utf-8 -*-

from abc import abstractmethod

from ruchatbot.bot.model_applicator import ModelApplicator


class YesNoModel(ModelApplicator):
    def __init__(self):
        pass

    @abstractmethod
    def calc_yes_no(self, premise_str_list, question_str, text_utils):
        raise NotImplementedError()
