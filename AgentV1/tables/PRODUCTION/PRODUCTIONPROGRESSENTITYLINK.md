# DB2ADMIN.PRODUCTIONPROGRESSENTITYLINK

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `PRODUCTIONPROGRESSCOMPANYCODE`, `PROPROGRESSPROGRESSNUMBER`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 52856

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRODUCTIONPROGRESSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROPROGRESSPROGRESSNUMBER` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ENTITYTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `INACTIVE` | INTEGER | NOT NULL |  |  |  |
| 5 | `EXTOPCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `EXTOPCODE` | CHAR(15) |  |  |  |  |
| 7 | `EXTOPORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 9 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 10 | `PRODDEMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `PRODDEMCODE` | CHAR(15) |  |  |  |  |
| 12 | `PRODDEMSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 13 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 14 | `PRODDEMGROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRODUCTIONPROGRESS_PRODUCTIONPROGRESS` | `PRODUCTIONPROGRESSCOMPANYCODE`, `PROPROGRESSPROGRESSNUMBER` | [`PRODUCTIONPROGRESS`](../PRODUCTION/PRODUCTIONPROGRESS.md) | `COMPANYCODE`, `PROGRESSNUMBER` | RESTRICT | `PRODUCTIONPROGRESSENTITYLINK.PRODUCTIONPROGRESSCOMPANYCODE = PRODUCTIONPROGRESS.COMPANYCODE AND PRODUCTIONPROGRESSENTITYLINK.PROPROGRESSPROGRESSNUMBER = PRODUCTIONPROGRESS.PROGRESSNUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROPROGRESSENTITYLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PRODUCTIONPROGRESSCOMPANYCODE,
       t.PROPROGRESSPROGRESSNUMBER,
       t.LINENUMBER,
       t.ENTITYTYPE,
       t.INACTIVE,
       t.EXTOPCOUNTERCODE,
       t.EXTOPCODE,
       t.EXTOPORDERLINE,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.PRODDEMCOUNTERCODE,
       t.PRODDEMCODE
FROM   DB2ADMIN.PRODUCTIONPROGRESSENTITYLINK t
FETCH FIRST 100 ROWS ONLY;
```
