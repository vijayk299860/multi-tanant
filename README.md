# Multi-Tenant

This project demonstrates two approaches to multi-tenancy in Django:

1. **Schema-based Multi-Tenancy**  
   - Implemented using PostgreSQL schemas  
   - Each tenant shares the same database but has isolated data via separate schemas

2. **Database-isolated Multi-Tenancy**  
   - Each tenant has a completely separate database  
   - Ideal for strong isolation and custom configurations per tenant

---

Built with Django, PostgreSQL, and `django-tenants`.  
Supports tenant-aware routing, middleware, and admin segregation.

