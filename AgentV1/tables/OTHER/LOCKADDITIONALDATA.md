# DB2ADMIN.LOCKADDITIONALDATA

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `UNIQUEID`, `ENTITYNAME`, `FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194861

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `FIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `LOCKFLOW` | SMALLINT | NOT NULL |  |  |  |
| 4 | `LOCKBASELIST` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LOCKATTRIBUTEKEY2` | SMALLINT | NOT NULL |  |  |  |
| 6 | `LOCKATTRIBUTEKEY3` | SMALLINT | NOT NULL |  |  |  |
| 7 | `LOCKATTRIBUTEKEY4` | SMALLINT | NOT NULL |  |  |  |
| 8 | `LOCKATTRIBUTEKEY5` | SMALLINT | NOT NULL |  |  |  |
| 9 | `LOCKATTRIBUTEKEY6` | SMALLINT | NOT NULL |  |  |  |
| 10 | `LOCKATTRIBUTEKEY7` | SMALLINT | NOT NULL |  |  |  |
| 11 | `LOCKATTRIBUTEKEY8` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LOCKATTRIBUTEKEY9` | SMALLINT | NOT NULL |  |  |  |
| 13 | `LOCKATTRIBUTEKEY10` | SMALLINT | NOT NULL |  |  |  |
| 14 | `LOCKPRODUCT` | SMALLINT | NOT NULL |  |  |  |
| 15 | `LOCKFULLITEMKEYDECODER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `LOCKATTACHMENT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOCKADDITIONALDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.ENTITYNAME,
       t.FIELDNAME,
       t.LOCKFLOW,
       t.LOCKBASELIST,
       t.LOCKATTRIBUTEKEY2,
       t.LOCKATTRIBUTEKEY3,
       t.LOCKATTRIBUTEKEY4,
       t.LOCKATTRIBUTEKEY5,
       t.LOCKATTRIBUTEKEY6,
       t.LOCKATTRIBUTEKEY7,
       t.LOCKATTRIBUTEKEY8
FROM   DB2ADMIN.LOCKADDITIONALDATA t
FETCH FIRST 100 ROWS ONLY;
```
