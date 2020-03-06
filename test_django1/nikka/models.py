from django.db import models
import datetime
# Create your models here.
from django.utils import timezone


class Parson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'people'


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    # class Meta:
    #     unique_together = [['first_name', 'last_name']]


class Album(models.Model):
    artist = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        verbose_name='related musician',
        related_name='tb_musician',
        related_query_name='re_musician'
    )
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        # get_latest_by = 'release_date'
        # managed = False
        # order_with_respect_to = 'artist'
        # ordering = ['-release_date'] # For descending all records by default ascending
        # ordering = ['?'] # For random
        ordering = ['release_date']  # For random
        permissions = [('can_sell_album', 'Can Sell Album')]


class MyAlbum(Album):
    class Meta:
        proxy = True
        ordering = ['-release_date']

    def data(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Parson, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    parson = models.ForeignKey(Parson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_of_join = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


class MyParson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta:
        abstract = True
        ordering = ['birth_date']

    def __str__(self):
        return self.first_name

    def baby_boomer_status(self):

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Student(MyParson):
    tag = models.CharField(max_length=5, null=False, blank=False)

    class Meta(MyParson.Meta):
        permissions = [('can_learn', 'Can Learn')]

    def save(self, *args, **kwargs):
        if self.tag is None:
            print('Not:- {}'.format(timezone.now().date().year))
            return 'Not:- {}'.format(timezone.now().date().year)
        else:
            print('Yes:- {}'.format(timezone.now().date().year))
            print(self.tag)
            super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format(self.first_name, self.birth_date.year)


class Piece(models.Model):
    pieces = models.IntegerField()


class Article(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
    article_name = models.CharField(max_length=50)


class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
    book_name = models.CharField(max_length=50)


class Review(Book, Article):
    review_date = models.DateField(timezone.now().date())


class Runner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=50)
    route_length = models.IntegerField()

    def __str__(self):
        return self.name


class Race(models.Model):
    race_cod = models.CharField(max_length=6, unique=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='b_route')

    def __str__(self):
        return self.race_cod


class Results(models.Model):
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='r_race')
    runner_id = models.ForeignKey(Runner, on_delete=models.CASCADE, related_name='r_runner')

    def __str__(self):
        return '{} - {}'.format(self.race_id, self.runner_id)


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    o = models.Manager()

    def __str__(self):
        return self.headline
