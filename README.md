# rqlite for pyDAL

Example usage:

```python
from pydal import DAL

# required to register rqlite://
import pydal_rqlite

db = DAL("rqlite://localhost", folder="database")
# or with basic auth/custom port/https:
# db = DAL("rqlite://user:pass@localhost:4001", folder="database", driver_args={'https': True})
```

`db` should now support the same features the `sqlite3` driver
for [pyDAL](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer) does.
