# DB2ADMIN.CHECKADDITIONALDATA

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `UNIQUEID`, `ENTITYNAME`, `FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194774

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `FIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `FLOW` | SMALLINT | NOT NULL |  |  |  |
| 4 | `BASELIST` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ATTRIBUTEKEY2` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ATTRIBUTEKEY3` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ATTRIBUTEKEY4` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ATTRIBUTEKEY5` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ATTRIBUTEKEY6` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ATTRIBUTEKEY7` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ATTRIBUTEKEY8` | SMALLINT | NOT NULL |  |  |  |
| 12 | `ATTRIBUTEKEY9` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ATTRIBUTEKEY10` | SMALLINT | NOT NULL |  |  |  |
| 14 | `PRODUCT` | SMALLINT | NOT NULL |  |  |  |
| 15 | `FULLITEMKEYDECODER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `ATTACHMENT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CHECKADDITIONALDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.ENTITYNAME,
       t.FIELDNAME,
       t.FLOW,
       t.BASELIST,
       t.ATTRIBUTEKEY2,
       t.ATTRIBUTEKEY3,
       t.ATTRIBUTEKEY4,
       t.ATTRIBUTEKEY5,
       t.ATTRIBUTEKEY6,
       t.ATTRIBUTEKEY7,
       t.ATTRIBUTEKEY8
FROM   DB2ADMIN.CHECKADDITIONALDATA t
FETCH FIRST 100 ROWS ONLY;
```
