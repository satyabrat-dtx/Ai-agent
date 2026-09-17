# DB2ADMIN.TNAPARENTENTITY

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `JNDINAME`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208827

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENTITYDESCRIPTION` | CHAR(100) |  |  |  |  |
| 1 | `JNDINAME` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 2 | `FULLYQUALIFIEDNAME` | VARCHAR(100) | NOT NULL |  |  |  |
| 3 | `ACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 5 | `QUERYMETHODNAME` | CHAR(30) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TNAPARENTENTITY_ENTITY` | [`TNAACTIVITY`](../TNA/TNAACTIVITY.md) | `ENTITYJNDINAME` | `TNAACTIVITY.ENTITYJNDINAME = TNAPARENTENTITY.JNDINAME` |
| `TNAPARENTENTITY_ENTITY` | [`TNAHEADER`](../TNA/TNAHEADER.md) | `ENTITYJNDINAME` | `TNAHEADER.ENTITYJNDINAME = TNAPARENTENTITY.JNDINAME` |
| `TNAPARENTENTITY_ENTITY` | [`AUTHORIZATIONTEMPLATE`](../TNA/AUTHORIZATIONTEMPLATE.md) | `ENTITYJNDINAME` | `AUTHORIZATIONTEMPLATE.ENTITYJNDINAME = TNAPARENTENTITY.JNDINAME` |
| `TNAPARENTENTITY_ENTITY` | [`TNAAUTHORIZATIONTEMPLATE`](../TNA/TNAAUTHORIZATIONTEMPLATE.md) | `ENTITYJNDINAME` | `TNAAUTHORIZATIONTEMPLATE.ENTITYJNDINAME = TNAPARENTENTITY.JNDINAME` |

## Indexes

- `TNAPARENTENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENTITYDESCRIPTION,
       t.JNDINAME,
       t.FULLYQUALIFIEDNAME,
       t.ACTIVE,
       t.ABSUNIQUEID,
       t.QUERYMETHODNAME
FROM   DB2ADMIN.TNAPARENTENTITY t
FETCH FIRST 100 ROWS ONLY;
```
