# DB2ADMIN.WRKCLAIMLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `SALESCLAIMLINECOMPANYCODE`, `SALESCLAIMLINECODE`, `SALESCLAIMLINELINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 4388

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SALESCLAIMLINECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SALESCLAIMLINECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `SALESCLAIMLINELINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 6 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 7 | `ITEMLONGDESCRIPTION` | CHAR(200) |  |  |  |  |
| 8 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `PRIMARYQTYDECNUMBER` | INTEGER | NOT NULL |  |  |  |
| 10 | `SECONDARYQTYDECNUMBER` | INTEGER | NOT NULL |  |  |  |
| 11 | `PACKAGINGQTYDECNUMBER` | INTEGER | NOT NULL |  |  |  |
| 12 | `VALUEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.SALESCLAIMLINECOMPANYCODE,
       t.SALESCLAIMLINECODE,
       t.SALESCLAIMLINELINE,
       t.ITEMCODE,
       t.ITEMLONGDESCRIPTION,
       t.QUALITYLONGDESCRIPTION,
       t.PRIMARYQTYDECNUMBER,
       t.SECONDARYQTYDECNUMBER,
       t.PACKAGINGQTYDECNUMBER
FROM   DB2ADMIN.WRKCLAIMLINE t
FETCH FIRST 100 ROWS ONLY;
```
