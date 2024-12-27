from django.db import models
from datetime import date
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="entries")
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author, related_name="entries")
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    


"""
Adding Blog:

>>> from blog.models import Blog,Author,Entry
>>> blog1 = Blog.objects.create(name="Django Tips", tagline="All about Django")
>>> blog2 = Blog.objects.create(name="Python Hacks", tagline="Python for everyone")

Adding Authors:
>>> author1 = Author.objects.create(name="Alice", email="alice@example.com")
>>> author2 = Author.objects.create(name="Bob", email="bob@example.com")

Adding Entries:
>>> entry1 = Entry.objects.create(blog=blog1, headline = "Django ORM tips", body_text="Learb about django ORM and Q objects", pub_date=date(2024,12,1), number_of_comments = 5, number_of_pingbacks=2, rating=8)     
>>> entry2 = Entry.objects.create(blog=blog2, headline = "python tips", body_text="Top python tips for developers", pub_date=date(2024,11,28), number_of_comments = 15, number_of_pingbacks=3, rating=9)




1. Retrieving objects

a. Get all objects:

entries = Entry.objects.all()

b. Filter objects

entries = Entry.objects.filter(pub_date__year=2024)

c. Exclude objects

entries = Entry.objects.exclude(pub_date__year=2024)

d. Get a single object

entry = Entry.objects.get(id=1)

Note: get() raises DoesNotExist or MultipleObjectsReturned exceptions if 
No results or multiple results are found.


2. Field Lookups

---> Field lookups allow filtering using specific conditions.

a) Exact match
entries = Entry.objects.filter(headline__exact="Django ORM tips")

b) case-insensitive match
entries = Entry.objects.filter(headline__iexact="django orm tips")

c) partial Match
entries = Entry.objects.filter(headline__icontains="Django")

d) Range query
entries = Entry.objects.filter(pub_date__range=["2024-01-01", "2024-12-01"])

3. Ordering Results

a) Ascending order

entries = Entry.objects.order_by("pub_date")

b) descending order

entries = Entry.objects.order_by("-pub_date")

c) Multiple orderings

entries = Entry.objects.order_by("-rating", "headline")

4. Limiting Results
-> Limit the number of results returned.

a) slicing querysets

entries = Entry.objects.all()[:5]

b) Offset and Limit

entries = Entry.objects.all()[5:10]

5. Aggregations

a) Count Entries
from django.db.models import Count

entry_count = Entry.objects.aggregate(Count("id"))

b) Calculate average rating
from django.db.models import Avg
average_rating = Entry.objects.aggregate(Avg("rating"))

6. Related objects Queries
Filter across relationships (foreign keys and many-to-many fields)

a) Foreign key filtering
entries = Entry.objects.filter(blog=blog1)

b) Many-to-Many filtering
entries = Entry.objects.filter(authors=author1)

7. Annotating Querysets

a) Annotate Comment count
-> Count the number of comments for each blog

from django.db.models import Count
blogs = Blog.objects.annotate(comment_count=Count("entry__number_of_comments"))

b) Annotate Average Rating
Calculate the average rating for each blog.

blogs = Blog.objects.annotate(avg_rating=Avg("entry__rating"))

5. Prefetching Related Objects
Optimizing queries by prefetching related objects

a) Select Related
-> Retrieve entries along with their related blog objects.
entries = Entry.objects.select_related("blog")

b) Prefetch Related
-> Retrieve authors and prefetch their entries

authors = Author.objects.prefetch_related("entry_set")


*** Both Select related and prefetch related are used to optimize database queries involving related models,
but they serve different purposes.

-> select_related: Fetches related objects in the same database query using SQL JOINs. It is used for one-to-one and many-to-one relationships. (e.g: ForeignKey)
-> prefetch_related: Fetches related objects in separate queries and performs the "join" in python. It is used for many-to-many and reverse foreign key relationships.

Example:

Without select_related

entires = Entry.objects.all()
for entry in entries:
    print(entry.blog.name)

with select_related:

entries = Entry.objects.select_related("blog")


Without prefetch_related:

entries = Entry.objects.all()
for entry in entries:
    print([author.name for author in entry.authors.all()])


----------------------------------------------------------------------

Django Q objects:

1. Basic usage of Q objects.
- Q objects allow you to create more complex query conditions using &, | and ~ (Not)

Example1 OR condition:

a) Find entries with a headline containing "Django" OR rating less than 5
from django.db.models import Q
entries = Entry.objects.filter(Q(headline__icontains="Django")|Q(rating__lt=5))

b) AND conditions
entries = Entry.objects.filter(Q(pub_date__year=2024) & Q(rating__gt=7))

c) NOT conditions
entries = Entry.objects.filter(~Q(headline__icontains="Python"))


2. Combining Q objects with Keyword arguments

a) combining Q and filter
entries = Entry.objects.filter(Q(headline__icontains="Tips") | Q(rating__gt=8), blog=blog1)

b) Exclude with combined filters
entries = Entry.objects.filter(blog=blog2).exclude(Q(number_of_comments__gt=10))


*** still more to go, we will see later.
"""

