from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive')
]


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100, null=False, blank=False, db_index=True) #Add index for frequent lookups
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['price']), # Explicit index
        ]

"""
Module 1: Understanding and optimizing Model Design

1. Use Appropriate Field Type
- Choosing the correct field types reduces storage size 
and improves query speed.

ex: for max_length we will put by default 255. But for names, we dont need that much size.
We can just put, max_length=100 or even less.

2. Add Indexes for faster lookups.
-Indexes speed up queries for frequently searched, sorted or filtered fields.

3. Normalize Relationships.
- Split redundant data into related tables to avoid duplication but 
denormalize where necessary for common reads.

ex: category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

4. Use Defaults to Avoid NULL
- Avoid NULL where possible to simplify queries and ensure data consistency.


MODULE 2: Query Optimization Basics

Objectives: Write efficient queries to minimize load and reduce database hits.

1. Avoid Fetching all Data
- Fetch only what you need by filtering and slicing the queryset
Ex: Filter and limit results.

2. Use select_related for foreignkeys
- Reduces queries by joining related tables in a single query

3. Use prefetch_related for Many-to-Many relationships.
- Optimize queries involving reverse relationships or many-to-many fields.

4. Use Queryset Chaining
- Chain methods instead of combining them in python.


MODULE-3: Advanced Query Optimization
Objective: Leverage Django features to perform complex queries efficiently.

1. Aggregate and Annotate
Perform calculations like sums, counts, or averages directly in the database
- from django.db.models import Count, Avg

2. Defer or Only Specific fields
Fetch only the necessary fields to reduce the memory usage.

ex: Fetch only 'name' and 'price' fields
products = Product.objects.only('name', 'price')

ex-2: Exclude a large field
products = Product.objects.defer('description')

3. Use Raw SQL for Edge Cases
- For very complex queries, raw SQL can be faster.
- from django.db import connection


MODULE4: Profiling and Debugging Queries
Objective: Identify bottlenecks and measure query performance.

1. Use Django Debug Toolbar
Install identity bottlenecks and measure query performance.

pip install django-debug-toolbar

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

2. Use QuerySet.explain()
- understand query execution plans to identify inefficiencies.









"""