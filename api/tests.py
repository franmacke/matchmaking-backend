from django.test import TestCase
from api.models import Player, Match, Positions, PlayerMatchDetails

from datetime import datetime
import random

# Create your tests here.



class PlayerTestCase(TestCase):
    def setUp(self):
        Player.objects.create(name="Javier", gender=1)
        Player.objects.create(name="Maria", gender=2, skill=4.5)
    
    def test_create_match(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
        })

        self.assertEqual(response.status_code, 201, "Response status code should be 201")
        self.assertEqual(response.data['field_size'], field_size, "Field size should be equal")
        self.assertEqual(response.data['date'], date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'), "Date should be equal")
        self.assertEqual(response.data['team_one_goals'], None, "Team one goals should be None")
        self.assertEqual(response.data['team_two_goals'], None, "Team two goals should be None")
        self.assertEqual(response.data['goal_difference'], None, "Goal difference should be None")
        self.assertEqual(response.data['winner'], None, "Winner should be None")

    
    def test_update_field_size(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        created_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
        }, content_type='application/json')

        updated_match_response = self.client.patch(f'/api/match/{created_match_response.data["id"]}/', {
            'field_size': 10
        }, content_type='application/json')

        self.assertEqual(updated_match_response.status_code, 200, "Response status code should be 200")
        self.assertEqual(updated_match_response.data['field_size'], 10, "Field size should be 10")


    def test_update_team_sizes_less_than_zero(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        size_one = -1
        size_two = 0

        created_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
            'team_one_size': 5,
            'team_two_size': 5
        }, content_type='application/json')

        updated_match_response = self.client.patch(f'/api/match/{created_match_response.data["id"]}/', {
            'team_one_size': size_one,
            'team_two_size': size_two
        }, content_type='application/json')

        self.assertEqual(updated_match_response.status_code, 400, "Response status code should be 200")
        if size_one <= 0:
            self.assertEqual(updated_match_response.status_code, 400, "Team one size should be greater or equal to 0, was: " + str(size_one))
        if size_two <= 0:
            self.assertEqual(updated_match_response.status_code, 400, "Team two size should be greater or equal to 0, was: " + str(size_two))

    def test_update_team_sizes(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        created_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
            'team_one_size': 5,
            'team_two_size': 5
        }, content_type='application/json')

        updated_match_response = self.client.patch(f'/api/match/{created_match_response.data["id"]}/', {
            'team_one_size': 7,
            'team_two_size': 3
        }, content_type='application/json')

        self.assertEqual(updated_match_response.status_code, 200, "Response status code should be 200")
        self.assertEqual(updated_match_response.data['team_one_size'], 7, "Team one size should be 7")
        self.assertEqual(updated_match_response.data['team_two_size'], 3, "Team two size should be 3")

    def test_create_match_with_goals(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        create_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
            'team_one_goals': 1,
            'team_two_goals': 3
        }, content_type='application/json')

        self.assertEqual(create_match_response.status_code, 201, "Response status code should be 201")
        self.assertEqual(create_match_response.data['field_size'], field_size, "Field size should be equal")
        self.assertEqual(create_match_response.data['team_one_goals'], 1, "Team one goals should be 1")
        self.assertEqual(create_match_response.data['team_two_goals'], 3, "Team two goals should be 3")
        self.assertEqual(create_match_response.data['goal_difference'], -2, "Goal difference should be -2")
        self.assertEqual(create_match_response.data['winner'], 2, "Winner should be team two")

    def test_update_goals(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        created_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
            'team_one_goals': 1,
            'team_two_goals': 10
        }, content_type='application/json')

        updated_match_response = self.client.patch(f'/api/match/{created_match_response.data["id"]}/', {
            'team_one_goals': 3,
            'team_two_goals': 2
        }, content_type='application/json')

        self.assertEqual(updated_match_response.status_code, 200, "Response status code should be 200")
        self.assertEqual(updated_match_response.data['team_one_goals'], 3, "Team one goals should be 3")
        self.assertEqual(updated_match_response.data['team_two_goals'], 2, "Team two goals should be 2")
        self.assertEqual(updated_match_response.data['goal_difference'], 1, "Goal difference should be 1")
        self.assertEqual(updated_match_response.data['winner'], 1, "Winner should be team one")

    def test_match_draw(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        created_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
            'team_one_goals': 2,
            'team_two_goals': 2
        }, content_type='application/json')

        self.assertEqual(created_match_response.status_code, 201, "Response status code should be 201")
        self.assertEqual(created_match_response.data['team_one_goals'], 2, "Team one goals should be 2")
        self.assertEqual(created_match_response.data['team_two_goals'], 2, "Team two goals should be 2")
        self.assertEqual(created_match_response.data['goal_difference'], 0, "Goal difference should be 0")
        self.assertEqual(created_match_response.data['winner'], 0, "Winner should be draw")


    def test_update_goals_one_team_no_goals(self):
        field_size = random.randint(5, 11)
        date = datetime.now()

        created_match_response = self.client.post('/api/match/', {
            'date': date,
            'field_size': field_size,
        }, content_type='application/json')

        updated_match_response = self.client.patch(f'/api/match/{created_match_response.data["id"]}/', {
            'team_one_goals': 3,
            'team_two_goals': None
        }, content_type='application/json')

        self.assertEqual(updated_match_response.status_code, 200, "Response status code should be 200")
        self.assertEqual(updated_match_response.data['team_one_goals'], 3, "Team one goals should be 3")
        self.assertEqual(updated_match_response.data['team_two_goals'], None, "Team two goals should be None")
        self.assertEqual(updated_match_response.data['goal_difference'], None, "Goal difference should be None")
        self.assertEqual(updated_match_response.data['winner'], None, "Winner should be team None")