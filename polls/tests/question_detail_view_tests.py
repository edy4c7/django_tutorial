from django.test import TestCase
from django.urls import reverse

from .utils import create_question


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(
            question_text="Future question.", days=5
        )
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(
            question_text="Past question.", days=-5
        )
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
