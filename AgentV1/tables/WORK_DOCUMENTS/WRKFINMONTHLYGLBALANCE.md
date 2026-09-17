# DB2ADMIN.WRKFINMONTHLYGLBALANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239100

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANY` | CHAR(5) |  |  |  |  |
| 3 | `CUSTOMCOLUMN1` | CHAR(100) |  |  |  |  |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `DOCTEMPSTR` | VARCHAR(3000) |  |  |  |  |
| 6 | `BUSINESSUNITSTR` | VARCHAR(100) | NOT NULL |  |  |  |
| 7 | `DEBITAMT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `CREDITAMT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `BALANCEAMT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 11 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 12 | `GLCODE` | CHAR(12) |  |  |  |  |
| 13 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `ORDERPARTNERCODE` | CHAR(20) |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINMONTHLYGLBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.COMPANY,
       t.CUSTOMCOLUMN1,
       t.BUSINESSUNITCODE,
       t.DOCTEMPSTR,
       t.BUSINESSUNITSTR,
       t.DEBITAMT,
       t.CREDITAMT,
       t.BALANCEAMT,
       t.FROMDATE,
       t.TODATE
FROM   DB2ADMIN.WRKFINMONTHLYGLBALANCE t
FETCH FIRST 100 ROWS ONLY;
```
