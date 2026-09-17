# DB2ADMIN.ADENTITYKEYFIELDS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ENTITYNAME`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62982

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `REFERENCEDKEYFIELDENTITYNAME` | CHAR(50) |  | FK | foreign_key |  |
| 2 | `JNDINAME` | VARCHAR(100) | NOT NULL |  |  |  |
| 3 | `KEYFIELDSXML` | CLOB(1000000) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITYKEYFIELDS_REFERENCEDKEYFIELD` | `REFERENCEDKEYFIELDENTITYNAME` | [`ADENTITYKEYFIELDS`](../OTHER/ADENTITYKEYFIELDS.md) | `ENTITYNAME` | RESTRICT | `ADENTITYKEYFIELDS.REFERENCEDKEYFIELDENTITYNAME = ADENTITYKEYFIELDS.ENTITYNAME` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ADENTITYKEYFIELDS_RELATEDCLASS` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `RELATEDCLASSENTITYNAME` | `ADADDITIONALDATA.RELATEDCLASSENTITYNAME = ADENTITYKEYFIELDS.ENTITYNAME` |
| `ADENTITYKEYFIELDS_REFERENCEDKEYFIELD` | [`ADENTITYKEYFIELDS`](../OTHER/ADENTITYKEYFIELDS.md) | `REFERENCEDKEYFIELDENTITYNAME` | `ADENTITYKEYFIELDS.REFERENCEDKEYFIELDENTITYNAME = ADENTITYKEYFIELDS.ENTITYNAME` |

## Indexes

- `ADENTITYKEYFIELDSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENTITYNAME,
       t.REFERENCEDKEYFIELDENTITYNAME,
       t.JNDINAME,
       t.KEYFIELDSXML,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADENTITYKEYFIELDS t
FETCH FIRST 100 ROWS ONLY;
```
