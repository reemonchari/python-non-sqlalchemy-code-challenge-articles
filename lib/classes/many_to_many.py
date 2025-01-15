class Article:
    all_articles = []  # Class-level list to store all articles

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        
        # Add this article to the class-level list
        Article.all_articles.append(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    
    
    @author.setter
    def author(self, new_author):
        self._author = new_author  # Setter for author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine 

    @classmethod
    def all(cls):
        return cls.all_articles


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name  # Allow changing the name


    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category  # Allow changing the category

    def add_article(self, article):
        self._articles.append(article) 

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None