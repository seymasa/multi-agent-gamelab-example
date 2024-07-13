class GameLabTasks():
    def code_task(self, agent, game):
        return {
            'name': 'Oyunu Kodla',
            'agent': agent,
            'description': f"{game} oyununun kodunu yaz",
            'verbose': True,
            'expected_output': 'Tamamlanmış oyun kodu'
        }

    def review_task(self, agent, game):
        return {
            'name': 'Oyunu Gözden Geçir',
            'agent': agent,
            'description': f"{game} oyununun kodunu gözden geçir ve hataları bul",
            'verbose': True,
            'expected_output': 'Hata raporu'
        }

    def evaluate_task(self, agent, game):
        return {
            'name': 'Oyunu Onayla',
            'agent': agent,
            'description': f"{game} oyununun kodunu değerlendir ve nihai onayı ver",
            'verbose': True,
            'expected_output': 'Onaylanmış oyun kodu'
        }
