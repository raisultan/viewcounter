Basic view-counting mechanism.

### Tech Stack
- python 3.8.5
- django
- django-rest-framework
- gunicorn
- redis

### Entities
- City
- Category
- Advert - relates to city and category

### Endpoints
- `api/advert-list/` - adverts list
- `api/advert/{advert_id}/` - advert detail

### Use

Initial setup:
```bash
make setup
```

Start services:
```bash
make up
```

Stop services:
```bash
make stop
```

Flush containers:
```bash
make down
```

In order to create objects, access to admin panel needed, you must create superuser:
```bash
make createsuperuser
```

### Contact
ki.xbozz@gmail.com
