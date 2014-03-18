# -*- coding: utf-8 -*-

from .user import User, User_v1
from .doumail import Doumail
from .discussion import Discussion
from .note import Note
from .album import Album
from .photo import Photo
from .online import Online
from .event import Event
from .guess import Guess
from .miniblog import Miniblog
from .book import Book, Book_v1
from .movie import Movie
from .music import Music, Music_v1


class DoubanAPI(object):

    def __repr__(self):
        return '<DoubanClient API>'

    @property
    def user(self):
        return User(self.access_token)

    @property
    def doumail(self):
        return Doumail(self.access_token)

    @property
    def discussion(self):
        return Discussion(self.access_token)

    @property
    def note(self):
        return Note(self.access_token)

    @property
    def album(self):
        return Album(self.access_token)

    @property
    def photo(self):
        return Photo(self.access_token)

    @property
    def online(self):
        return Online(self.access_token)

    @property
    def event(self):
        return Event(self.access_token)

    @property
    def guess(self):
        return Guess(self.access_token)

    @property
    def miniblog(self):
        return Miniblog(self.access_token)

    @property
    def book(self):
        return Book(self.access_token)

    @property
    def movie(self):
        return Movie(self.access_token)

    @property
    def music(self):
        return Music(self.access_token)

class DoubanAPI_v1(object):

    def __repr__(self):
        return '<DoubanClient_v1 API>'

    @property
    def user(self):
        return User_v1(self.conn)

    @property
    def book(self):
        return Book_v1(self.conn)

    @property
    def music(self):
        return Music_v1(self.conn)