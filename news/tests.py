from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt


class EditorTestClass(TestCase):
    #setup method
    def setUp(self):
        self.hughes = Editor(first_name='Hughes',last_name='Mugera',email="mugerahughes@gmail.com")
        
    def tearDown(self):
        Editor.objects.all().delete()
    
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hughes,Editor))
        
    #Test save method
    def test_save_method(self):
        self.hughes.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
    
    def test_delete_method(self):
        self.hughes.save_editor()
        self.hughes.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)
        
    def test_display_all_saved(self):
        self.hughes.save_editor()
        self.karan = Editor(first_name='Karan',last_name='Oti',email="karanoti@gmail.com")
        self.karan.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 1)
        
        # Test for updating single object properties.
    def test_update_last_name_method(self):
        self.hughes.save_editor()
        new_name="Bwosi"
        id=1
        self.hughes.update_last_name(id,new_name)
        self.assertEquals(self.hughes.last_name,"Bwosi")
    
    
    
        
        
# class ArticleTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.hughes= Editor(first_name = 'Hughes', last_name ='Mugera', email ='hughes@gmail.com')
#         self.hughes.save_editor()

#         # Creating a new tag and saving it
#         self.new_tag = tags(name = 'testing')
#         self.new_tag.save()

#         self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.hughes)
#         self.new_article.save()

#         self.new_article.tags.add(self.new_tag)

#     def tearDown(self):
#         Editor.objects.all().delete()
#         tags.objects.all().delete()
#         Article.objects.all().delete()
        
#     def test_get_news_today(self):
#         today_news = Article.todays_news()
#         self.assertTrue(len(today_news)>0)
        
#     def test_get_news_by_date(self):
#         test_date = '2017-03-17'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         news_by_date = Article.days_news(date)
#         self.assertTrue(len(news_by_date) == 0)
