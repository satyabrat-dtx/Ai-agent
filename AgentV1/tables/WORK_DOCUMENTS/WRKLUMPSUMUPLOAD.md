# DB2ADMIN.WRKLUMPSUMUPLOAD

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171323

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `RECORDSTATUS` | INTEGER | NOT NULL |  |  |  |
| 3 | `STATUSDESC` | VARCHAR(250) |  |  |  |  |
| 4 | `EMPLOYEECODE` | CHAR(25) |  |  |  |  |
| 5 | `PAYELEMENTTYPE` | CHAR(2) |  |  |  |  |
| 6 | `PAYELEMENTCODE` | CHAR(6) |  |  |  |  |
| 7 | `FROMPRLPROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 8 | `TOPRLPROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 9 | `REQUESTDATE` | DATE |  |  |  |  |
| 10 | `APPROVEDBYCODE` | CHAR(25) |  |  |  |  |
| 11 | `APPROVEDDATE` | DATE |  |  |  |  |
| 12 | `FLAGLSORFORMULA` | INTEGER | NOT NULL |  |  |  |
| 13 | `AMOUNTCALCULATED` | DECIMAL(11,4) |  |  |  |  |
| 14 | `FORMULACODE` | CHAR(6) |  |  |  |  |
| 15 | `OPERATIONALFLAG` | INTEGER | NOT NULL |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKLUMPSUMUPLOADUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.RECORDSTATUS,
       t.STATUSDESC,
       t.EMPLOYEECODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.FROMPRLPROCESSPERIOD,
       t.TOPRLPROCESSPERIOD,
       t.REQUESTDATE,
       t.APPROVEDBYCODE,
       t.APPROVEDDATE
FROM   DB2ADMIN.WRKLUMPSUMUPLOAD t
FETCH FIRST 100 ROWS ONLY;
```
