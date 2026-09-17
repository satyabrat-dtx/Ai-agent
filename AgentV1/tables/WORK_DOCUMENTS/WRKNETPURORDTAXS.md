# DB2ADMIN.WRKNETPURORDTAXS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`, `PURLINEABSUNIQUE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 240174

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `FATHERLINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `SEARCHDESC` | VARCHAR(250) |  |  |  |  |
| 4 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `CALCULATEDVALUER` | DECIMAL(18,5) |  |  |  |  |
| 6 | `PURLINEABSUNIQUE` | BIGINT | NOT NULL | PK | primary_key |  |
| 7 | `SEQ` | DECIMAL(2,0) |  |  |  |  |
| 8 | `PURHDRABSUNIQUE` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.FATHERLINENO,
       t.SEARCHDESC,
       t.VALUE,
       t.CALCULATEDVALUER,
       t.PURLINEABSUNIQUE,
       t.SEQ,
       t.PURHDRABSUNIQUE
FROM   DB2ADMIN.WRKNETPURORDTAXS t
FETCH FIRST 100 ROWS ONLY;
```
