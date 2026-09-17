# DB2ADMIN.ADSTORAGEIMPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `OWNERENTITYNAME`, `OWNERADUNIQUEID`, `NAMEENTITYNAME`, `NAMENAME`, `FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1353

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 1 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 2 | `OWNERENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `OWNERADUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `NAMEENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 5 | `NAMENAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 6 | `FIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 7 | `KEYSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 8 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 10 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 11 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 12 | `VALUEDATE` | DATE |  |  |  |  |
| 13 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 14 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 15 | `VALUETIME` | TIME |  |  |  |  |
| 16 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADSTORAGEIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTOPERATION,
       t.IMPORTSTATUS,
       t.OWNERENTITYNAME,
       t.OWNERADUNIQUEID,
       t.NAMEENTITYNAME,
       t.NAMENAME,
       t.FIELDNAME,
       t.KEYSEQUENCE,
       t.DATATYPE,
       t.VALUESTRING,
       t.VALUEINT,
       t.VALUEBOOLEAN
FROM   DB2ADMIN.ADSTORAGEIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
