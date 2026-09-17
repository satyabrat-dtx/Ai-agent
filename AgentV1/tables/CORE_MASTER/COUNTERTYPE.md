# DB2ADMIN.COUNTERTYPE

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'COUNTER')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CODE`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70817

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `TRANSIENTCOUNTERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `DEFAULTCOUNTERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `COUNTERLENGTH` | INTEGER | NOT NULL |  |  |  |
| 7 | `SUBSERIESTYPEREQUIRED` | CHAR(2) |  |  |  |  |
| 8 | `COUNTERSTANDARD` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COUNTERTYPE_COUNTERTYPE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COUNTERTYPECODE` | `COUNTER.COUNTERTYPECODE = COUNTERTYPE.CODE` |
| `COUNTERTYPE_COUNTERTYPE` | [`TRANSACTIONALNUMBERING`](../WAREHOUSE/TRANSACTIONALNUMBERING.md) | `COUNTERTYPECODE` | `TRANSACTIONALNUMBERING.COUNTERTYPECODE = COUNTERTYPE.CODE` |

## Indexes

- `COUNTERTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TRANSIENTCOUNTERALLOWED,
       t.DEFAULTCOUNTERALLOWED,
       t.COUNTERLENGTH,
       t.SUBSERIESTYPEREQUIRED,
       t.COUNTERSTANDARD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COUNTERTYPE t
FETCH FIRST 100 ROWS ONLY;
```
