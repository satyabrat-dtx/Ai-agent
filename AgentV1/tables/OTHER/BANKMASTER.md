# DB2ADMIN.BANKMASTER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COUNTRYISOCODE`, `CLEARING`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104169

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTRYISOCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CLEARING` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 2 | `BIC` | CHAR(11) |  |  |  |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `POSTALCODE` | CHAR(10) |  |  |  |  |
| 7 | `CITY` | CHAR(30) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ISOCOUNTRY_COUNTRYISO` | `COUNTRYISOCODE` | [`ISOCOUNTRY`](../OTHER/ISOCOUNTRY.md) | `CODE` | RESTRICT | `BANKMASTER.COUNTRYISOCODE = ISOCOUNTRY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BANKMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNTRYISOCODE,
       t.CLEARING,
       t.BIC,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.POSTALCODE,
       t.CITY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BANKMASTER t
FETCH FIRST 100 ROWS ONLY;
```
