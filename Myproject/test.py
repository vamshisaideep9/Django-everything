from django.core.cache import cache


cache.set('test_key', 'test_value', timeout=90)

value = cache.get('test_key')
print(f"cached value: {value}")

cache.delete('test_key')